# backend/database.py
import sqlite3

DB_NAME = "smartcity.db"

def get_connection():
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row  # Para devolver diccionarios en lugar de tuplas
    return conn

def init_db():
    conn = get_connection()
    cursor = conn.cursor()

    # Crear tabla de usuarios
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        email TEXT NOT NULL,
        password TEXT NOT NULL
    )
    """)

    # Crear tabla IoT
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS iot_data (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        device TEXT NOT NULL,
        type TEXT NOT NULL,
        value REAL NOT NULL,
        unit TEXT NOT NULL
    )
    """)

    conn.commit()
    conn.close()
