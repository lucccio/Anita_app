import streamlit as st
from app.logic.detalle_productos_logic import (
    registrar_detalle,
    obtener_detalles,
    editar_detalle
)
from app.logic.productos_logic import obtener_productos

def vista_detalle_productos():
    st.subheader("📦 Detalle de Productos")

    # ===== ESTADOS =====
    if "modo_edicion_det" not in st.session_state:
        st.session_state.modo_edicion_det = False

    if "detalle_sel" not in st.session_state:
        st.session_state.detalle_sel = None

    productos = obtener_productos().data
    if not productos:
        st.warning("Primero registra productos")
        return

    prod_map = {f'{p["nombre"]} (ID {p["id"]})': p["id"] for p in productos}

    producto = st.selectbox("Producto", prod_map.keys())
    producto_id = prod_map[producto]

    color = st.text_input("Color", st.session_state.get("color", ""))
    talla = st.selectbox(
        "Talla",
        ["34","35","36","37","38","39","40","41","42","43","44","45",
         "XS","S","M","L","XL","pequeña","mediana","grande",
         "small","medium","large"],
        index=0
    )
    genero = st.selectbox("Género", ["hombre", "mujer", "unisex"])
    stock = st.number_input("Stock", min_value=0, step=1)

    # ===== BOTONES =====
    col1, col2 = st.columns(2)

    with col1:
        if not st.session_state.modo_edicion_det:
            if st.button("Registrar detalle"):
                try:
                    registrar_detalle(producto_id, color, talla, genero, stock)
                    st.success("Detalle registrado")
                    st.rerun()
                except Exception as e:
                    st.warning(str(e))
        else:
            if st.button("Guardar cambios"):
                editar_detalle(
                    st.session_state.detalle_sel["ID"],
                    color, talla, genero, stock
                )
                st.success("Detalle actualizado")
                cancelar_detalle()
                st.rerun()

    with col2:
        if st.button("❌ Cancelar selección"):
            cancelar_detalle()
            st.rerun()

    st.divider()

    # ===== TABLA =====
    detalles = obtener_detalles().data
    if not detalles:
        st.info("No hay detalles registrados")
        return

    tabla = []
    for d in detalles:
        tabla.append({
            "": False,
            "ID": d["id"],
            "Producto": d["producto_id"],
            "Color": d["color"],
            "Talla": d["talla"],
            "Género": d["genero"],
            "Stock": d["stock"]
        })

    edited = st.data_editor(tabla, hide_index=True, use_container_width=True)

    seleccionados = [r for r in edited if r[""]]

    if st.button("✏️ Editar", disabled=not seleccionados):
        d = seleccionados[0]
        st.session_state.modo_edicion_det = True
        st.session_state.detalle_sel = d

        st.session_state.color = d["Color"]
        st.session_state.stock = d["Stock"]

        st.rerun()


def cancelar_detalle():
    st.session_state.modo_edicion_det = False
    st.session_state.detalle_sel = None
    for k in ["color", "stock"]:
        st.session_state.pop(k, None)
