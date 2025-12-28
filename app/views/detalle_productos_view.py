import streamlit as st
from app.logic.productos_logic import obtener_productos
from app.logic.detalle_productos_logic import (
    registrar_detalle_producto,
    obtener_detalles_por_producto
)

def vista_detalle_productos():
    st.subheader("📦 Detalle de Productos")

    productos = obtener_productos().data

    if not productos:
        st.warning("No hay productos registrados")
        return

    # Diccionario: nombre → id
    opciones = {
        f'{p["nombre"]} (ID {p["id"]})': p["id"]
        for p in productos
    }

    producto_seleccionado = st.selectbox(
        "Selecciona un producto",
        list(opciones.keys())
    )

    producto_id = opciones[producto_seleccionado]

    st.divider()
    st.write("### Registrar detalle")

    color = st.text_input("Color")
    talla = st.selectbox(
        "Talla",
        [
            '34','35','36','37','38','39','40','41','42','43','44','45',
            'XS','S','M','L','XL',
            'pequeña','mediana','grande',
            'small','medium','large'
        ]
    )

    genero = st.selectbox(
        "Género",
        ["hombre", "mujer", "unisex"]
    )

    stock = st.number_input(
        "Stock",
        min_value=0,
        step=1
    )

    if st.button("Registrar detalle"):
        try:
            registrar_detalle_producto(
                producto_id,
                color,
                talla,
                genero,
                stock
            )
            st.success("✅ Detalle registrado correctamente")
            st.rerun()
        except ValueError as e:
            st.warning(f"⚠️ {e}")
        except Exception as e:
            st.error("❌ Error inesperado")
            st.write(e)

    st.divider()
    st.write("### Detalles registrados")

    detalles = obtener_detalles_por_producto(producto_id).data

    if not detalles:
        st.info("Este producto no tiene detalles registrados")
        return

    st.dataframe(detalles, use_container_width=True)
