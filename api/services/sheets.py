import os
import json
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import logging

logger = logging.getLogger(__name__)

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
        logger.error("Falta la variable GOOGLE_CREDENTIALS_JSON")
        raise RuntimeError("Falta la variable GOOGLE_CREDENTIALS_JSON")
    
    # Manejo de comillas simples o dobles en el env
    if creds_env.startswith("'") and creds_env.endswith("'"):
        creds_env = creds_env[1:-1]

    try:
        creds_json = json.loads(creds_env)
        creds = ServiceAccountCredentials.from_json_keyfile_dict(creds_json, scope)
        _gspread_client = gspread.authorize(creds)
        return _gspread_client
    except Exception as e:
        logger.error(f"Error autorizando gspread: {e}")
        raise RuntimeError(f"Error autorizando gspread: {e}")

def get_spreadsheet():
    global _spreadsheet
    if _spreadsheet:
        return _spreadsheet
    
    client = get_gspread_client()
    sheet_id = os.environ.get("GOOGLE_SHEET_ID")
    if not sheet_id:
        logger.error("La variable de entorno GOOGLE_SHEET_ID es obligatoria.")
        raise RuntimeError("La variable de entorno GOOGLE_SHEET_ID es obligatoria para conectar con la base de datos.")
        
    try:
        _spreadsheet = client.open_by_key(sheet_id)
        return _spreadsheet
    except Exception as e:
        logger.error(f"Error abriendo la hoja por ID: {e}")
        raise RuntimeError(f"Error abriendo la hoja por ID: {e}")
