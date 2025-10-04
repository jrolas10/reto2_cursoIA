# backend/main.py
import sys, os
sys.path.append(os.path.dirname(__file__))

from fastapi import FastAPI
import users
import iot
from database import init_db  # ✅ corregido

app = FastAPI(title="SmartCity API")

# Inicializar base de datos al arrancar
@app.on_event("startup")
def startup_event():
    init_db()

# Rutas
app.include_router(users.router, prefix="/users", tags=["users"])
app.include_router(iot.router, prefix="/iot", tags=["iot"])

@app.get("/")
def root():
    return {"message": "SmartCity API is running 🚀"}
