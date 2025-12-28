import streamlit as st

from app.views.usuarios_view import vista_usuarios
from app.views.categorias_view import vista_categorias
from app.views.productos_view import vista_productos
from app.views.detalle_productos_view import vista_detalle_productos

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
        "Detalles de Productos",
        "Ventas",
        "Reportes"
    ]
)

# ================= CONTENIDO =================
if opcion == "Usuarios":
    vista_usuarios()

elif opcion == "Categorías":
    st.subheader("Categorías")
    vista_categorias()
    
elif opcion == "Productos":
    st.subheader("📦 Productos")
    vista_productos()

elif opcion == "Detalles de Productos":
    st.subheader("📦 Detalles de Productos")
    vista_detalle_productos()

elif opcion == "Ventas":
    st.subheader("💰 Ventas")
    st.info("🚧 Módulo en proceso de desarrollo")

elif opcion == "Reportes":
    st.subheader("📊 Reportes")
    st.info("🚧 Módulo en proceso de desarrollo")
