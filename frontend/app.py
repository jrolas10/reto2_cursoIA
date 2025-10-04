# frontend/app.py
import streamlit as st
import requests
import pandas as pd
import plotly.express as px

# URL del backend (cuando esté en docker-compose será http://backend:8000)
BACKEND_URL = "http://backend:8000"

# Estado de sesión
if "authenticated" not in st.session_state:
    st.session_state.authenticated = False


# ----- Login -----
def login_screen():
    st.title("🔐 SmartCity - Login")

    username = st.text_input("Usuario")
    password = st.text_input("Contraseña", type="password")

    if st.button("Iniciar sesión"):
        # Validación mock (puedes cambiarlo luego por JWT contra backend)
        if username == "admin" and password == "admin":
            st.session_state.authenticated = True
            st.success("¡Login exitoso!")
        else:
            st.error("Usuario o contraseña incorrectos")


# ----- Dashboard -----
def dashboard():
    st.title("📊 SmartCity Dashboard")

    # --- Usuarios ---
    st.subheader("👥 Usuarios registrados")
    try:
        res = requests.get(f"{BACKEND_URL}/users/")
        if res.status_code == 200:
            users = res.json()
            df_users = pd.DataFrame(users)
            st.dataframe(df_users)
        else:
            st.error("Error al obtener usuarios")
    except Exception as e:
        st.error(f"No se pudo conectar al backend: {e}")

    # --- IoT ---
    st.subheader("🌐 Datos IoT")
    try:
        res = requests.get(f"{BACKEND_URL}/iot/")
        if res.status_code == 200:
            iot = res.json()
            df_iot = pd.DataFrame(iot)
            st.dataframe(df_iot)

            if not df_iot.empty:
                fig = px.scatter(df_iot, x="device", y="value",
                                 color="type", size="value",
                                 title="Valores IoT")
                st.plotly_chart(fig)
        else:
            st.error("Error al obtener datos IoT")
    except Exception as e:
        st.error(f"No se pudo conectar al backend: {e}")


# ----- App -----
if not st.session_state.authenticated:
    login_screen()
else:
    dashboard()
