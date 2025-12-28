import streamlit as st
from app.logic.detalle_productos_logic import (
    obtener_detalles_producto,
    registrar_detalle_producto,
    borrar_detalle_producto
)

# ===============================
#   VISTA DETALLE DE PRODUCTOS
# ===============================
def vista_detalle_productos(producto_id=None):

    st.title("🧩 Detalle del Producto")

    # -----------------------------
    # VALIDAR PRODUCTO ID
    # -----------------------------
    if not producto_id:
        st.error("❌ No se ha recibido el ID del producto.")
        st.info("Este módulo debe abrirse desde la vista de productos.")
        return

    st.success(f"Producto seleccionado ID: {producto_id}")

    st.subheader("Registrar variación")

    # -----------------------------
    # FORMULARIO
    # -----------------------------
    with st.form("form_detalle"):
        color = st.selectbox(
            "Color",
            ["negro","blanco","rojo","azul","verde","amarillo",
             "rosado","marrón","gris","beige","celeste","morado"]
        )

        talla = st.selectbox(
            "Talla",
            [
                "34","35","36","37","38","39","40","41","42","43","44","45",
                "XS","S","M","L","XL",
                "pequeña","mediana","grande",
                "small","medium","large"
            ]
        )

        genero = st.selectbox("Género", ["hombre", "mujer", "unisex"])

        stock = st.number_input("Stock", min_value=0, step=1)

        submitted = st.form_submit_button("Guardar detalle")

        if submitted:
            try:
                registrar_detalle_producto(
                    producto_id,
                    color,
                    talla,
                    genero,
                    stock
                )
                st.success("✔️ Detalle registrado correctamente")
                st.rerun()
            except Exception as e:
                st.error(f"❌ Error: {e}")

    st.divider()

    # -----------------------------
    # LISTA DE DETALLES
    # -----------------------------
    st.subheader("Variaciones registradas")

    detalles = obtener_detalles_producto(producto_id).data

    if not detalles:
        st.info("ℹ️ Este producto no tiene variaciones registradas todavía.")
        return

    for d in detalles:
        with st.container(border=True):
            st.write(
                f"🎨 **Color:** {d['color']} | "
                f"📏 **Talla:** {d['talla']} | "
                f"🚻 **Género:** {d['genero']} | "
                f"📦 **Stock:** {d['stock']}"
            )

            eliminar = st.button("🗑️ Eliminar", key=d["id"])

            if eliminar:
                borrar_detalle_producto(d["id"])
                st.success("Variación eliminada correctamente")
                st.rerun()
