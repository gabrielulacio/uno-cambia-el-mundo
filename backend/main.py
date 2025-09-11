from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# CORS configuration
origins = [
    "http://localhost",
    "http://localhost:5173", # <-- Asegúrate de que esta URL esté incluida
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Nuevo endpoint para el frontend
@app.get("/hello")
def say_hello():
    return {"message": "¡Hola desde FastAPI!"}