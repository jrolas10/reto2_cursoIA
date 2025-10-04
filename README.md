# 🌆 SmartCity Dashboard

Proyecto desarrollado con **FastAPI (Backend)** y **Streamlit (Frontend)** para visualizar y gestionar datos de **usuarios** e **IoT** de una ciudad inteligente.  
Todo el entorno se ejecuta mediante **Docker Compose**, sin necesidad de configuraciones manuales.

---

## 🧱 Estructura del Proyecto

Reto2/
│
├── backend/
│ ├── main.py
│ ├── users.py
│ ├── iot.py
│ ├── database.py
│ ├── models.py
│ ├── auth.py
│ ├── schemas.py
│ ├── init_db.py
│ ├── requirements.txt
│ └── Dockerfile
│
├── frontend/
│ ├── app.py
│ ├── requirements.txt
│ └── Dockerfile
│
├── test/
│ ├── test_users.py
│ └── test_iot.py
│
├── docker-compose.yml
├── README.md
└── smartcity.db

Reto2/
│
├── backend/
│ ├── main.py
│ ├── users.py
│ ├── iot.py
│ ├── database.py
│ ├── models.py
│ ├── auth.py
│ ├── schemas.py
│ ├── init_db.py
│ ├── requirements.txt
│ └── Dockerfile
│
├── frontend/
│ ├── app.py
│ ├── requirements.txt
│ └── Dockerfile
│
├── test/
│ ├── test_users.py
│ └── test_iot.py
│
├── docker-compose.yml
├── README.md
└── smartcity.db

Esto levantará:

Servicio	Tecnología	URL
🧠 Backend	FastAPI	http://localhost:8000

📊 Frontend	Streamlit	http://localhost:8501

🔐 Credenciales de acceso

Para entrar al Dashboard:

Usuario: admin  
Contraseña: admin

⚠️ Nota importante:
Al iniciar sesión por primera vez puede ser necesario intentar dos veces.
El primer intento valida las credenciales y el segundo permite el acceso completo.

🧩 Endpoints principales (Swagger UI)

Accede a la documentación interactiva:
👉 http://localhost:8000/docs

🔹 Usuarios (/users)

POST /users/ → Crear usuario

{
  "name": "Laura Gómez",
  "email": "laura.gomez@smartcity.mx",
  "password": "1234"
}


GET /users/ → Listar usuarios

🔹 Datos IoT (/iot)

POST /iot/ → Registrar dato IoT

{
  "device": "Sensor_Temp_CDMX",
  "type": "Temperatura",
  "value": 26.4,
  "unit": "°C"
}


GET /iot/ → Listar todos los datos IoT

📊 Interfaz Web (Streamlit)

Una vez levantado el proyecto, abre:
👉 http://localhost:8501

Podrás visualizar:

👥 Tabla de usuarios registrados

🌡️ Tabla de datos IoT

📈 Gráfico interactivo con los valores de sensores

🧪 Pruebas unitarias (opcional)

Para ejecutar pruebas locales:

pytest test/ -v

✅ Resumen rápido
Elemento	URL / Comando	Descripción
Backend (API)	http://localhost:8000/docs
	Swagger UI con endpoints
Frontend (App)	http://localhost:8501
	Dashboard de Streamlit
Credenciales	admin / admin	Acceso inicial
Base de datos	smartcity.db	SQLite (persistente dentro del contenedor)
🧾 Notas del desarrollador

💡 Datos iniciales recomendados para pruebas:

[
  {
    "device": "Sensor_Hum_Puebla",
    "type": "Humedad",
    "value": 68.5,
    "unit": "%"
  },
  {
    "device": "AQ_Monterrey",
    "type": "Calidad del aire (PM2.5)",
    "value": 32.1,
    "unit": "µg/m³"
  },
  {
    "device": "Noise_CentroGDL",
    "type": "Ruido ambiental",
    "value": 58.2,
    "unit": "dB"
  },
  {
    "device": "Light_CDMX_Park",
    "type": "Luminosidad",
    "value": 742,
    "unit": "lux"
  }
]

Ejecutar manualmente
# Backend
uvicorn backend.main:app --reload

# Frontend
streamlit run frontend/app.py


🐳 Ejecución rápida con Docker
🔹 1. Clonar el repositorio
git clone https://github.com/jrolas10/reto2_cursoIA.git
cd reto2_cursoIA

🔹 2. Levantar todo el entorno
docker-compose up --build

🔐 Credenciales de acceso

⚠️ Nota importante:
El sistema de login requiere ingresar la contraseña dos veces:
la primera valida la autenticación y la segunda permite el ingreso.

Usuario: admin
Contraseña: admin