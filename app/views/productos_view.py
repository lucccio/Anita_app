import streamlit as st
from app.logic.productos_logic import (
    registrar_producto,
    obtener_productos
)
from app.logic.categorias_logic import obtener_categorias


def vista_productos():
    st.subheader("📦 Gestión de Productos")

    # ========== FORMULARIO ==========
    st.write("Formulario de registro")

    nombre = st.text_input("Nombre del producto")
    descripcion = st.text_area("Descripción")

    precio = st.number_input(
        "Precio",
        min_value=0.0,
        step=0.1,
        format="%.2f"
    )

    # Obtener categorías
    categorias = obtener_categorias().data

    if not categorias:
        st.warning("⚠️ No hay categorías registradas. Registra una primero.")
        return

    # Diccionario: nombre_visible -> id_real
    opciones = {c["nombre"]: c["id"] for c in categorias}

    categoria_nombre = st.selectbox(
        "Seleccionar categoría",
        list(opciones.keys())
    )

    categoria_id = opciones[categoria_nombre]

    if st.button("Registrar producto"):
        try:
            registrar_producto(
                nombre,
                descripcion,
                precio,
                categoria_id
            )
            st.success("✅ Producto registrado correctamente")
            st.rerun()

        except ValueError as e:
            st.warning(f"⚠️ {e}")
        except Exception as e:
            st.error("❌ Error inesperado")
            st.write(e)

    st.divider()

    # ========== TABLA ==========
    st.subheader("📋 Lista de productos")

    productos = obtener_productos().data

    if not productos:
        st.info("No hay productos registrados")
        return

    # Mapa categoria_id -> nombre
    map_categorias = {c["id"]: c["nombre"] for c in categorias}

    tabla = []
    for p in productos:
        tabla.append({
            "ID": p["id"],
            "Nombre": p["nombre"],
            "Descripción": p["descripcion"],
            "Precio": p["precio"],
            "Categoría": map_categorias.get(p["categoria_id"], "Sin categoría")
        })

    st.dataframe(tabla, use_container_width=True)
