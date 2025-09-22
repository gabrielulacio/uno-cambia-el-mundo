from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import json
import os
import time
from typing import Any, Dict, List, Optional

# Important: root_path makes FastAPI aware it's mounted at `/api` behind Vercel
app = FastAPI(root_path="/api")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def get_gspread_client():
    # Prefer read-only scopes
    scope = [
        "https://www.googleapis.com/auth/spreadsheets.readonly",
        "https://www.googleapis.com/auth/drive.readonly",
    ]
    creds_env = os.environ.get("GOOGLE_CREDENTIALS_JSON")
    if not creds_env:
        raise RuntimeError("Missing GOOGLE_CREDENTIALS_JSON env var")
    creds_json = json.loads(creds_env)
    creds = ServiceAccountCredentials.from_json_keyfile_dict(creds_json, scope)
    client = gspread.authorize(creds)
    return client


def get_spreadsheet(client: gspread.Client):
    sheet_id = os.environ.get("GOOGLE_SHEET_ID")
    sheet_name = os.environ.get("GOOGLE_SHEET_NAME", "UnoCambiaElMundoDB")
    if sheet_id:
        return client.open_by_key(sheet_id)
    return client.open(sheet_name)


def _parse_int(value: Any, default: int = 0) -> int:
    try:
        if value is None:
            return default
        if isinstance(value, (int, float)):
            return int(value)
        s = str(value).replace(",", "").strip()
        return int(float(s))
    except Exception:
        return default


_cache: Dict[str, Dict[str, Any]] = {
    "donation_status": {"ts": 0, "data": None},
    "payment_methods": {"ts": 0, "data": None},
}
_TTL = int(os.environ.get("SHEETS_CACHE_TTL", "60"))


def _get_cached(key: str) -> Optional[Any]:
    now = time.time()
    entry = _cache.get(key)
    if not entry:
        return None
    if now - entry.get("ts", 0) <= _TTL and entry.get("data") is not None:
        return entry["data"]
    return None


def _set_cached(key: str, data: Any) -> None:
    _cache[key] = {"ts": time.time(), "data": data}

@app.get("/donation-status")
def get_donation_status():
    cached = _get_cached("donation_status")
    if cached is not None:
        return cached

    SHEET_STATUS_NAME = os.environ.get("GOOGLE_STATUS_SHEET", "Status")
    try:
        client = get_gspread_client()
        ss = get_spreadsheet(client)
        sheet = ss.worksheet(SHEET_STATUS_NAME)
        goal = _parse_int(sheet.acell("B1").value, 100000)
        current = _parse_int(sheet.acell("B2").value, 75000)
        result = {"goal": goal, "current": current}
        _set_cached("donation_status", result)
        return result
    except Exception as e:
        print(f"Error fetching from Google Sheets (donation-status): {e}")
        return {"goal": 100000, "current": 75000}

@app.get("/payment-methods")
def get_payment_methods():
    cached = _get_cached("payment_methods")
    if cached is not None:
        return cached

    SHEET_PAYMENTS_NAME = os.environ.get("GOOGLE_PAYMENTS_SHEET", "PaymentMethods")
    try:
        client = get_gspread_client()
        ss = get_spreadsheet(client)
        sheet = ss.worksheet(SHEET_PAYMENTS_NAME)
        records: List[Dict[str, Any]] = sheet.get_all_records()
        normalized: List[Dict[str, Any]] = []
        for record in records:
            rec = dict(record)
            fields_val = rec.get("fields")
            if isinstance(fields_val, str) and fields_val.strip():
                try:
                    rec["fields"] = json.loads(fields_val)
                except json.JSONDecodeError:
                    rec["fields"] = []
            elif isinstance(fields_val, list):
                rec["fields"] = fields_val
            else:
                rec["fields"] = []
            normalized.append(rec)
        _set_cached("payment_methods", normalized)
        return normalized
    except Exception as e:
        print(f"Error fetching from Google Sheets (payment-methods): {e}")
        return []

@app.get("/")
def read_root():
    return {"message": "API de 'Uno Cambia el Mundo' funcionando"}

# Simple health/hello endpoint used by frontend sample
@app.get("/hello")
def say_hello():
    return {"message": "¡Hola desde FastAPI!"}