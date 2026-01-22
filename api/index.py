from dotenv import load_dotenv
import os
import time
import json
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from typing import Any, Dict, List, Optional
from fastapi import FastAPI, HTTPException, BackgroundTasks, Request
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, EmailStr, Field
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.util import get_remote_address
from slowapi.errors import RateLimitExceeded

# Cargar variables locales
load_dotenv()

# Configuración de Rate Limiting
limiter = Limiter(key_func=get_remote_address)
app = FastAPI(root_path="/api")
app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)

app.add_middleware(
    CORSMiddleware,
    # En producción, cambia "*" por tu dominio real
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# --- MODELOS DE DATOS ---
class PaymentReport(BaseModel):
    project: str = Field(..., min_length=3, max_length=50)
    name: str = Field(..., min_length=2, max_length=100)
    email: EmailStr
    amount: float = Field(..., gt=0)
    currency: str = Field(..., min_length=3, max_length=5)
    reference: str = Field(..., min_length=4, max_length=100)
    anonymous: bool

# --- CACHE / SINGLETONS ---
_gspread_client = None
_spreadsheet = None

def get_gspread_client():
    global _gspread_client
    if _gspread_client:
        return _gspread_client

    scope = [
        "https://www.googleapis.com/auth/spreadsheets",
        "https://www.googleapis.com/auth/drive",
    ]
    creds_env = os.environ.get("GOOGLE_CREDENTIALS_JSON")
    if not creds_env:
        raise RuntimeError("Falta la variable GOOGLE_CREDENTIALS_JSON")
    
    # Manejo de comillas simples o dobles en el env
    if creds_env.startswith("'") and creds_env.endswith("'"):
        creds_env = creds_env[1:-1]

    creds_json = json.loads(creds_env)
    creds = ServiceAccountCredentials.from_json_keyfile_dict(creds_json, scope)
    _gspread_client = gspread.authorize(creds)
    return _gspread_client

def get_spreadsheet():
    global _spreadsheet
    if _spreadsheet:
        return _spreadsheet
    
    client = get_gspread_client()
    sheet_id = os.environ.get("GOOGLE_SHEET_ID")
    if sheet_id:
        _spreadsheet = client.open_by_key(sheet_id)
    else:
        _spreadsheet = client.open("UnoCambiaElMundoDB")
    return _spreadsheet

# --- FUNCIONES DE CORREO ---
def send_email_notification(report: PaymentReport):
    sender = os.environ.get("EMAIL_SENDER")
    password = os.environ.get("EMAIL_PASSWORD")
    receiver = sender 

    if not sender or not password:
        print("⚠️ Advertencia: No hay credenciales de correo configuradas.")
        return

    message = MIMEMultipart("alternative")
    message["Subject"] = f"💰 Nuevo Aporte: {report.amount} {report.currency} - {report.project}"
    message["From"] = sender
    message["To"] = receiver

    text = f"""
    Nuevo reporte de donación recibido:
    
    Donante: {report.name} ({'Anónimo' if report.anonymous else 'Público'})
    Email: {report.email}
    Monto: {report.amount} {report.currency}
    Referencia: {report.reference}
    Proyecto: {report.project}
    
    Verifica la transacción en el banco y en el Google Sheet.
    """
    
    message.attach(MIMEText(text, "plain"))

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(sender, password)
            server.send_message(message)
        print("✅ Correo de notificación enviado.")
    except Exception as e:
        print(f"❌ Error enviando correo: {e}")

# --- ENDPOINTS ---

@app.post("/report-payment")
@limiter.limit("3/minute") # Limita a 3 reportes por minuto por IP para evitar spam
def report_payment(report: PaymentReport, request: Request, background_tasks: BackgroundTasks):
    try:
        ss = get_spreadsheet()
        
        # Busca la hoja "Reportes" o créala si no existe
        try:
            sheet = ss.worksheet("Reportes")
        except gspread.exceptions.WorksheetNotFound:
            sheet = ss.add_worksheet(title="Reportes", rows="1000", cols="10")
            sheet.append_row(["Fecha", "Proyecto", "Nombre", "Email", "Monto", "Moneda", "Referencia", "Anónimo", "Estado"])

        # Agregar la fila
        sheet.append_row([
            time.strftime("%Y-%m-%d %H:%M:%S"),
            report.project,
            report.name,
            report.email,
            report.amount,
            report.currency,
            report.reference,
            "Sí" if report.anonymous else "No",
            "Pendiente"
        ])

        # 2. Enviar Correo en segundo plano
        background_tasks.add_task(send_email_notification, report)

        return {"status": "success", "message": "Reporte recibido correctamente"}

    except Exception as e:
        print(f"Error procesando reporte: {e}")
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/donation-status")
def get_donation_status():
    try:
        ss = get_spreadsheet()
        sheet = ss.worksheet("Status")
        # Leemos el rango A2:B2 de una vez para evitar múltiples peticiones HTTP
        values = sheet.get("A2:B2")
        if not values or len(values[0]) < 2:
            raise ValueError("Datos de status insuficientes")
            
        goal = int(values[0][0].replace(",",""))
        current = int(values[0][1].replace(",",""))
        return {"goal": goal, "current": current}
    except Exception as e:
        print(f"Error cargando status: {e}")
        return {"goal": 100000, "current": 75000} # Fallback

@app.get("/payment-methods")
def get_payment_methods():
    # Esto permite mover la configuración al backend si se desea a futuro
    # Por ahora devolvemos la estructura estática pero centralizada
    return {
        "methods": [
            {
                "id": "zelle",
                "name": "Zelle",
                "icon": "🇺🇸",
                "details": [
                    {"label": "donations.methods.email", "value": "zelle@rotarysc.org", "copyable": True},
                    {"label": "donations.methods.holder", "value": "Rotary San Cristóbal", "copyable": False}
                ]
            },
            {
                "id": "pagomovil",
                "name": "Pago Móvil",
                "icon": "⿽",
                "details": [
                    {"label": "donations.methods.bank", "value": "Bancamiga (0172)", "copyable": False},
                    {"label": "donations.methods.phone", "value": "04141234567", "copyable": True},
                    {"label": "donations.methods.rif", "value": "J-123456789", "copyable": True}
                ]
            },
            {
                "id": "binance",
                "name": "Binance Pay",
                "icon": "🔶",
                "details": [
                    {"label": "donations.methods.pay_id", "value": "123456789", "copyable": True},
                    {"label": "donations.methods.email", "value": "binance@rotarysc.org", "copyable": False}
                ]
            }
        ]
    }

@app.get("/")
def read_root():
    return {"message": "API Operativa"}
