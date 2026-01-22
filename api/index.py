from dotenv import load_dotenv
import os
import time
import json
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from typing import Any, Dict, List, Optional
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import gspread
from oauth2client.service_account import ServiceAccountCredentials

# Cargar variables locales
load_dotenv()

app = FastAPI(root_path="/api")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# --- MODELOS DE DATOS ---
class PaymentReport(BaseModel):
    project: str
    name: str
    email: str
    amount: float
    currency: str
    reference: str
    anonymous: bool

# --- FUNCIONES DE GOOGLE SHEETS ---
def get_gspread_client():
    # CAMBIO IMPORTANTE: Quitamos .readonly para poder ESCRIBIR
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
    client = gspread.authorize(creds)
    return client

def get_spreadsheet(client):
    sheet_id = os.environ.get("GOOGLE_SHEET_ID")
    if sheet_id:
        return client.open_by_key(sheet_id)
    return client.open("UnoCambiaElMundoDB")

# --- FUNCIONES DE CORREO ---
def send_email_notification(report: PaymentReport):
    sender = os.environ.get("EMAIL_SENDER")
    password = os.environ.get("EMAIL_PASSWORD")
    receiver = sender # Te envías el correo a ti mismo (o cambia esto por otro email)

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
        # No lanzamos error para no detener la respuesta al usuario

# --- ENDPOINTS ---

@app.post("/report-payment")
def report_payment(report: PaymentReport):
    try:
        # 1. Guardar en Google Sheets
        client = get_gspread_client()
        ss = get_spreadsheet(client)
        
        # Busca la hoja "Reportes" o créala si no existe
        try:
            sheet = ss.worksheet("Reportes")
        except:
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

        # 2. Enviar Correo (Nivel 1)
        send_email_notification(report)

        return {"status": "success", "message": "Reporte recibido correctamente"}

    except Exception as e:
        print(f"Error procesando reporte: {e}")
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/donation-status")
def get_donation_status():
    # (Mantén tu lógica anterior aquí o usa esta simplificada)
    try:
        client = get_gspread_client()
        ss = get_spreadsheet(client)
        sheet = ss.worksheet("Status")
        goal = int(sheet.acell("A2").value.replace(",",""))
        current = int(sheet.acell("B2").value.replace(",",""))
        return {"goal": goal, "current": current}
    except:
        return {"goal": 100000, "current": 75000} # Fallback

@app.get("/")
def read_root():
    return {"message": "API Operativa"}