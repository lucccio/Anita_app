import streamlit as st
from app.logic.productos_logic import (
    registrar_producto,
    editar_producto,
    obtener_productos
)
from app.logic.categorias_logic import obtener_categorias

def vista_productos():
    st.subheader("📦 Gestión de Productos")

    # ================= ESTADOS =================
    if "modo_edicion_producto" not in st.session_state:
        st.session_state.modo_edicion_producto = False

    if "producto_seleccionado" not in st.session_state:
        st.session_state.producto_seleccionado = None

    # ================= FORM =================
    nombre = st.text_input(
        "Nombre",
        value=st.session_state.get("nombre_producto", "")
    )

    descripcion = st.text_area(
        "Descripción",
        value=st.session_state.get("descripcion_producto", "")
    )

    precio = st.number_input(
        "Precio",
        min_value=0.0,
        step=0.1,
        value=st.session_state.get("precio_producto", 0.0)
    )

    categorias = obtener_categorias().data
    if not categorias:
        st.warning("⚠️ Registra una categoría primero")
        return

    opciones = {c["nombre"]: c["id"] for c in categorias}

    categoria_nombre = st.selectbox(
        "Categoría",
        opciones.keys(),
        index=(
            list(opciones.values()).index(
                st.session_state.get("categoria_id_producto")
            ) if st.session_state.get("categoria_id_producto") in opciones.values() else 0
        )
    )

    categoria_id = opciones[categoria_nombre]

    # ================= ACCIONES =================
    col1, col2 = st.columns(2)

    if not st.session_state.modo_edicion_producto:
        with col1:
            if st.button("Registrar"):
                try:
                    registrar_producto(
                        nombre, descripcion, precio, categoria_id
                    )
                    st.success("✅ Producto registrado")
                    st.rerun()
                except ValueError as e:
                    st.warning(f"⚠️ {e}")
    else:
        with col1:
            if st.button("Guardar cambios"):
                try:
                    editar_producto(
                        st.session_state.producto_seleccionado["ID"],
                        nombre, descripcion, precio, categoria_id
                    )
                    st.success("✏️ Producto actualizado")

                    cancelar_edicion_producto()
                    st.rerun()

                except ValueError as e:
                    st.warning(f"⚠️ {e}")

        with col2:
            if st.button("❌ Cancelar selección"):
                cancelar_edicion_producto()
                st.rerun()

    st.divider()

    # ================= TABLA =================
    productos = obtener_productos().data
    if not productos:
        st.info("No hay productos registrados")
        return

    tabla = []
    for p in productos:
        tabla.append({
            "": False,
            "ID": p["id"],
            "Nombre": p["nombre"],
            "Descripción": p["descripcion"],
            "Precio": p["precio"],
            "Categoría": p["categoria_id"]
        })

    edited = st.data_editor(
        tabla,
        hide_index=True,
        use_container_width=True
    )

    seleccionados = [r for r in edited if r[""]]

    # ================= BOTONES =================
    col1, col2 = st.columns([8, 2])

    with col2:
        if st.button("✏️ Editar", disabled=not seleccionados):
            p = seleccionados[0]
            st.session_state.modo_edicion_producto = True
            st.session_state.producto_seleccionado = p

            st.session_state.nombre_producto = p["Nombre"]
            st.session_state.descripcion_producto = p["Descripción"]
            st.session_state.precio_producto = p["Precio"]
            st.session_state.categoria_id_producto = p["Categoría"]

            st.rerun()


# ================= HELPERS =================
def cancelar_edicion_producto():
    st.session_state.modo_edicion_producto = False
    st.session_state.producto_seleccionado = None

    for k in [
        "nombre_producto",
        "descripcion_producto",
        "precio_producto",
        "categoria_id_producto"
    ]:
        st.session_state.pop(k, None)
