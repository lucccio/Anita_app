import streamlit as st
from app.database.conexion import supabase

st.set_page_config(
    page_title="Anita New Style",
    layout="centered"
)

st.title("Anita New Style – Test Supabase")

def test_conexion():
    try:
        response = supabase.table("usuarios").select("*").limit(1).execute()
        st.success("Conexión exitosa con Supabase")
        st.write(response.data)
    except Exception as e:
        st.error("Error de conexión")
        st.write(e)

test_conexion()
