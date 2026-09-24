import streamlit as st
import requests

st.title("Dashboard conectado a FastAPI")

# 1. Llamada al endpoint raíz
try:
    respuesta_root = requests.get("http://127.0.0.1:8000/").json()
    st.success(f"Respuesta del backend: {respuesta_root.get('mensaje')}")
except Exception as e:
    st.error("No se pudo conectar con el servidor FastAPI")

# 2. Llamada dinámica al endpoint con ID
item_id = st.slider("Selecciona el ID del Item", 1, 100, 10)

if st.button("Consultar Item en FastAPI"):
    url = f"http://127.0.0.1:8000/items/{item_id}"
    respuesta_item = requests.get(url, params={"q": "consulta_desde_streamlit"}).json()
    
    st.json(respuesta_item)