from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import json
import os

app = FastAPI()

# Configuración de CORS para permitir peticiones desde tu frontend
origins = [
    "http://localhost:5173",
    "https://uno-cambia-el-mundo.vercel.app/",
    "https://www.unocambiaelmundo.org/",
    "https://unocambiaelmundo.org/"
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# --- Conexión a Google Sheets ---
def get_gspread_client():
    scope = ["https://spreadsheets.google.com/feeds", 'https://www.googleapis.com/auth/drive']
    
    # Las credenciales se leen desde una variable de entorno en Vercel
    creds_json = json.loads(os.environ.get("GOOGLE_CREDENTIALS_JSON"))
    
    creds = ServiceAccountCredentials.from_json_keyfile_dict(creds_json, scope)
    client = gspread.authorize(creds)
    return client

# --- Endpoints de la API ---

@app.get("/api/donation-status")
def get_donation_status():
    """
    Obtiene el estado de la donación (meta y actual) desde la hoja 'Status'.
    """
    try:
        client = get_gspread_client()
        sheet = client.open("UnoCambiaElMundoDB").worksheet("Status") # Asegúrate que el nombre del archivo sea correcto
        
        goal = sheet.acell('B1').value
        current = sheet.acell('B2').value
        
        return {"goal": int(goal), "current": int(current)}
    except Exception as e:
        # Devuelve datos de ejemplo si falla la conexión para que la web no se rompa
        print(f"Error fetching from Google Sheets: {e}")
        return {"goal": 100000, "current": 75000}


@app.get("/api/payment-methods")
def get_payment_methods():
    """
    Obtiene la lista de métodos de pago desde la hoja 'PaymentMethods'.
    """
    try:
        client = get_gspread_client()
        sheet = client.open("UnoCambiaElMundoDB").worksheet("PaymentMethods") # Asegúrate que el nombre del archivo sea correcto
        
        records = sheet.get_all_records()
        
        # Convierte el string de 'fields' a un objeto JSON real
        for record in records:
            if isinstance(record.get('fields'), str):
                try:
                    record['fields'] = json.loads(record['fields'])
                except json.JSONDecodeError:
                    record['fields'] = [] # O un valor por defecto si el JSON es inválido
            else:
                record['fields'] = []


        return records
    except Exception as e:
        # Devuelve datos de ejemplo si falla la conexión
        print(f"Error fetching from Google Sheets: {e}")
        return []

# Endpoint raíz para verificar que la API funciona
@app.get("/api")
def read_root():
    return {"message": "API de 'Uno Cambia el Mundo' funcionando"}