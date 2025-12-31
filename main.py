from operator import imod
import streamlit as st

from app.views.usuarios_view import vista_usuarios
from app.views.categorias_view import vista_categorias
from app.views.productos_view import vista_productos
from app.views.reportes_view import vista_reportes
from app.views.ventas_view import vista_ventas


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
    vista_categorias()
    
elif opcion == "Productos":
    vista_productos()

elif opcion == "Ventas":
    vista_ventas()

elif opcion == "Reportes":
    vista_reportes()
