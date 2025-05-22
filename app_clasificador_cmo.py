
import streamlit as st
import joblib

# Cargar el modelo
modelo = joblib.load("clasificador_cmo_modelo.pkl")

st.title("Clasificador de Intervenciones Farmacéuticas - Modelo CMO")
st.write("Introduce una intervención farmacéutica para clasificarla como Capacidad, Motivación u Oportunidad:")

# Entrada de usuario
texto_usuario = st.text_area("Texto de la intervención:", "")

if st.button("Clasificar"):
    if texto_usuario.strip() == "":
        st.warning("Por favor, introduce una intervención.")
    else:
        prediccion = modelo.predict([texto_usuario])[0]
        st.success(f"Clasificación CMO: **{prediccion}**")
