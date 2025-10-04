# ---- Imagen base ----
FROM python:3.11-slim

# ---- Directorio de trabajo ----
WORKDIR /app

# ---- Copiar archivos ----
COPY requirements.txt .   
# ---- Copiar el resto del código ----
COPY . .


# ---- Instalar dependencias ----
RUN pip install --no-cache-dir -r requirements.txt



# ---- Exponer puerto ----
EXPOSE 8000

# ---- Comando de arranque ----
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
