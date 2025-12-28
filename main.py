import streamlit as st
from app.views.usuarios_view import vista_usuarios

st.set_page_config(page_title="Anita New Style", layout="wide")

# 🔒 SIMULACIÓN DE ROL
if "rol" not in st.session_state:
    st.session_state.rol = "admin"  # simulamos admin

st.sidebar.title("Menú")

if st.session_state.rol == "admin":
    opcion = st.sidebar.radio(
        "Panel Admin",
        ["Usuarios", "Categorías", "Productos", "Ventas"]
    )
else:
    opcion = st.sidebar.radio(
        "Menú",
        ["Catálogo"]
    )

st.title("Anita New Style")

if opcion == "Usuarios":
    vista_usuarios()
    
elif opcion == "Categorías":
    st.info("Módulo categorías")

elif opcion == "Productos":
    st.info("Módulo productos")

elif opcion == "Ventas":
    st.info("Módulo ventas")
