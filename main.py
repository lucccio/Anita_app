import streamlit as st

from app.views.usuarios_view import vista_usuarios

# ================= CONFIGURACIÓN =================
st.set_page_config(
    page_title="Anita New Style",
    layout="wide"
)

st.title("🛍️ Anita New Style")

# ================= SIDEBAR =================
st.sidebar.title("Menú principal")

opcion = st.sidebar.radio(
    "Selecciona una opción:",
    [
        "Usuarios",
        "Categorías",
        "Productos",
        "Ventas",
        "Reportes"
    ]
)

# ================= CONTENIDO =================
if opcion == "Usuarios":
    vista_usuarios()

elif opcion == "Categorías":
    st.subheader("Categorías")
    st.info("🚧 Módulo en proceso de desarrollo")
    
elif opcion == "Productos":
    st.subheader("📦 Productos")
    st.info("🚧 Módulo en proceso de desarrollo")

elif opcion == "Ventas":
    st.subheader("💰 Ventas")
    st.info("🚧 Módulo en proceso de desarrollo")

elif opcion == "Reportes":
    st.subheader("📊 Reportes")
    st.info("🚧 Módulo en proceso de desarrollo")
