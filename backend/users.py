# backend/users.py
from fastapi import APIRouter
from schemas import User, UserCreate
from auth import hash_password

from database import get_connection

router = APIRouter()

@router.post("/", response_model=User)
def create_user(user: UserCreate):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO users (name, email, password) VALUES (?, ?, ?)
    """, (user.name, user.email, hash_password(user.password)))

    conn.commit()
    user_id = cursor.lastrowid
    conn.close()

    return {"id": user_id, "name": user.name, "email": user.email, "password": "********"}

@router.get("/", response_model=list[User])
def list_users():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT id, name, email, password FROM users")
    rows = cursor.fetchall()
    conn.close()

    return [dict(row) for row in rows]
