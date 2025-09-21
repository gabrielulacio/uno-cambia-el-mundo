from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import json
import os

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def get_gspread_client():
    scope = ["https://spreadsheets.google.com/feeds", 'https://www.googleapis.com/auth/drive']
    creds_json = json.loads(os.environ.get("GOOGLE_CREDENTIALS_JSON"))
    creds = ServiceAccountCredentials.from_json_keyfile_dict(creds_json, scope)
    client = gspread.authorize(creds)
    return client

@app.get("/donation-status")
def get_donation_status():
    """
    Obtiene el estado de la donación (meta y actual) desde la hoja 'Status'.
    """
    try:
        client = get_gspread_client()
        sheet = client.open("UnoCambiaElMundoDB").worksheet("Status")
        
        goal = sheet.acell('B1').value
        current = sheet.acell('B2').value
        
        return {"goal": int(goal), "current": int(current)}
    except Exception as e:
        print(f"Error fetching from Google Sheets: {e}")
        return {"goal": 100000, "current": 75000}


@app.get("/payment-methods") 
def get_payment_methods():
    """
    Obtiene la lista de métodos de pago desde la hoja 'PaymentMethods'.
    """
    try:
        client = get_gspread_client()
        sheet = client.open("UnoCambiaElMundoDB").worksheet("PaymentMethods")
        
        records = sheet.get_all_records()
        
        for record in records:
            if isinstance(record.get('fields'), str):
                try:
                    record['fields'] = json.loads(record['fields'])
                except json.JSONDecodeError:
                    record['fields'] = []
            else:
                record['fields'] = []

        return records
    except Exception as e:
        print(f"Error fetching from Google Sheets: {e}")
        return []

# Endpoint raíz para verificar que la API funciona
@app.get("/")
def read_root():
    return {"message": "API de 'Uno Cambia el Mundo' funcionando"}