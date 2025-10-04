# ---- Imagen base ----
FROM python:3.11-slim

# ---- Directorio de trabajo ----
WORKDIR /app

# ---- Copiar requerimientos ----
COPY requirements.txt .   

# ---- Instalar dependencias ----
RUN pip install --no-cache-dir -r requirements.txt

# ---- Copiar el frontend ----
COPY . .

# ---- Exponer puerto de Streamlit ----
EXPOSE 8501

# ---- Comando de arranque ----
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
