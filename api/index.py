from dotenv import load_dotenv
import os
import time
import json
import logging
from typing import Any, Dict, List, Optional
from fastapi import FastAPI, HTTPException, BackgroundTasks, Request
from fastapi.middleware.cors import CORSMiddleware
from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.util import get_remote_address
from slowapi.errors import RateLimitExceeded
import gspread

# Importaciones locales (usando rutas relativas para Vercel)
try:
    from api.models.payment import PaymentReport
    from api.services.sheets import get_spreadsheet
    from api.services.email_service import send_email_notification
except ImportError:
    from models.payment import PaymentReport
    from services.sheets import get_spreadsheet
    from services.email_service import send_email_notification

# Cargar variables locales
load_dotenv()

# Configuración de Logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Configuración de Rate Limiting
limiter = Limiter(key_func=get_remote_address)
app = FastAPI(root_path="/api")
app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)

# --- VALIDACIÓN INICIAL ---
EMAIL_CONFIGURED = bool(os.environ.get("EMAIL_SENDER") and os.environ.get("EMAIL_PASSWORD"))

if not EMAIL_CONFIGURED:
    logger.warning("EMAIL_SENDER o EMAIL_PASSWORD no configurados. Las notificaciones no funcionarán.")

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "https://unocambiaelmundo.org",
        "https://www.unocambiaelmundo.org"
    ], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# --- ENDPOINTS ---

@app.get("/health")
def health_check():
    """Endpoint para verificar el estado de la API."""
    return {
        "status": "healthy", 
        "timestamp": time.time(),
        "environment": os.environ.get("VERCEL_ENV", "development")
    }

@app.post("/report-payment")
@limiter.limit("3/minute") # Limita a 3 reportes por minuto por IP para evitar spam
def report_payment(report: PaymentReport, request: Request, background_tasks: BackgroundTasks):
    # --- VALIDACIÓN DE ORIGEN (Anti-CSRF) ---
    if os.environ.get("VERCEL_ENV") == "production":
        origin = request.headers.get("origin")
        referer = request.headers.get("referer")
        trusted = ["https://unocambiaelmundo.org", "https://www.unocambiaelmundo.org"]
        
        origin_ok = origin and any(origin.startswith(o) for o in trusted)
        referer_ok = referer and any(referer.startswith(o) for o in trusted)
        
        if not (origin_ok or referer_ok):
            logger.warning(f"Intento de acceso denegado por origen no confiable: {origin} / {referer}")
            raise HTTPException(status_code=403, detail="Acceso denegado: Petición de origen no confiable.")

    try:
        ss = get_spreadsheet()
        
        # Busca la hoja "Reportes" o créala si no existe
        try:
            sheet = ss.worksheet("Reportes")
        except gspread.exceptions.WorksheetNotFound:
            logger.info("Hoja 'Reportes' no encontrada. Creándola...")
            sheet = ss.add_worksheet(title="Reportes", rows="1000", cols="10")
            sheet.append_row(["Fecha", "Proyecto", "Nombre", "Email", "Monto", "Moneda", "Método", "Referencia", "Anónimo", "Estado"])

        # Agregar la fila
        sheet.append_row([
            time.strftime("%Y-%m-%d %H:%M:%S"),
            report.project,
            report.name,
            report.email,
            report.amount,
            report.currency,
            report.method,
            report.reference,
            "Sí" if report.anonymous else "No",
            "Pendiente"
        ])

        # 2. Enviar Correo en segundo plano
        background_tasks.add_task(send_email_notification, report)

        return {
            "status": "success", 
            "message": "Reporte recibido correctamente",
            "warning": None if EMAIL_CONFIGURED else "email_not_configured"
        }

    except Exception as e:
        logger.error(f"Error procesando reporte: {e}", exc_info=True)
        raise HTTPException(status_code=500, detail="Error interno procesando el reporte.")

@app.get("/donation-status")
def get_donation_status():
    try:
        ss = get_spreadsheet()
        sheet = ss.worksheet("Status")
        records = sheet.get_all_records()
        
        projects_status = []
        total_goal = 0
        total_current = 0

        for row in records:
            try:
                goal = float(str(row.get("goal", 0)).replace(",", ""))
                current = float(str(row.get("current", 0)).replace(",", ""))
                proj_name = row.get("proyecto", "Sin Nombre")
                
                slug = row.get("slug")
                if not slug:
                    slug = proj_name.lower().replace(" ", "-")
                
                projects_status.append({
                    "id": str(slug),
                    "name": proj_name,
                    "goal": goal,
                    "current": current,
                    "image": row.get("image", ""),
                    "percentage": round((current / goal * 100), 2) if goal > 0 else 0
                })
                
                total_goal += goal
                total_current += current
            except (ValueError, TypeError):
                continue

        return {
            "projects": projects_status,
            "total_goal": total_goal,
            "total_current": total_current
        }
    except Exception as e:
        logger.error(f"Error cargando status: {e}")
        return {
            "projects": [],
            "total_goal": 100000, 
            "total_current": 75000
        }

@app.get("/payment-methods")
def get_payment_methods():
    try:
        ss = get_spreadsheet()
        sheet = ss.worksheet("PaymentMethods")
        records = sheet.get_all_records()
        
        methods = []
        for row in records:
            fields_data = []
            fields_raw = row.get("fields", "[]")
            try:
                if fields_raw:
                    fields_data = json.loads(fields_raw)
            except json.JSONDecodeError:
                logger.error(f"Error parseando fields para {row.get('name')}")
            
            currency_raw = str(row.get("currency", "USD")).strip()
            currencies = []
            
            if currency_raw:
                try:
                    currencies = json.loads(currency_raw.replace("'", '"'))
                except json.JSONDecodeError:
                    clean_text = currency_raw.replace("[", "").replace("]", "").replace("'", "").replace('"', "")
                    if "," in clean_text:
                        currencies = [c.strip() for c in clean_text.split(",")]
                    else:
                        currencies = [clean_text]
            
            if not isinstance(currencies, list):
                currencies = [str(currencies)]
            
            currencies = [c for c in currencies if c]
            if not currencies:
                currencies = ["USD"]

            methods.append({
                "id": str(row.get("id")),
                "name": str(row.get("name")),
                "icon": str(row.get("logo", "💰")),
                "description": str(row.get("description", "")),
                "details": fields_data,
                "currencies": currencies
            })
        
        return {"methods": methods}
    except Exception as e:
        logger.error(f"Error cargando métodos: {e}")
        return {
            "methods": [
                {
                    "id": "zelle",
                    "name": "Zelle",
                    "icon": "🇺🇸",
                    "details": [
                        {"label": "donations.methods.email", "value": "zelle@rotarysc.org", "copyable": True},
                        {"label": "donations.methods.holder", "value": "Rotary San Cristóbal", "copyable": False}
                    ],
                    "currencies": ["USD"]
                }
            ]
        }

@app.get("/")
def read_root():
    return {"message": "API Operativa"}
