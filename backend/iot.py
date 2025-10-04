# backend/iot.py
from fastapi import APIRouter, HTTPException
from database import get_connection  # ✅ corregido, sin "backend."
from pydantic import BaseModel
from typing import List

router = APIRouter()

class IoTData(BaseModel):
    id: int | None = None
    device: str
    type: str
    value: float
    unit: str


@router.post("/", response_model=IoTData)
def create_iot(data: IoTData):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO iot_data (device, type, value, unit) VALUES (?, ?, ?, ?)",
        (data.device, data.type, data.value, data.unit),
    )
    conn.commit()
    data.id = cursor.lastrowid
    conn.close()
    return data


@router.get("/", response_model=List[IoTData])
def list_iot():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM iot_data")
    rows = cursor.fetchall()
    conn.close()
    return [dict(row) for row in rows]
