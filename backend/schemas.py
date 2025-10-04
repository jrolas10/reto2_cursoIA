from pydantic import BaseModel, EmailStr
from typing import Optional

class User(BaseModel):
    id: int
    name: str
    email: EmailStr
    password: str  # ⚠️ en memoria, luego se encripta con bcrypt

class UserCreate(BaseModel):
    name: str
    email: EmailStr
    password: str

class IoTData(BaseModel):
    id: int
    device_id: str
    value: float
    description: Optional[str] = None
