import streamlit as st
from app.logic.categorias_logic import (
    registrar_categoria,
    obtener_categorias,
    editar_categoria
)


def vista_categorias():
    st.subheader("Gestión de Categorías")

    if "modo_edicion_cat" not in st.session_state:
        st.session_state.modo_edicion_cat = False
        st.session_state.categoria_sel = None

    # ===== FORMULARIO =====
    nombre = st.text_input(
        "Nombre de la categoría",
        value=st.session_state.get("cat_nombre", "")
    )
    descripcion = st.text_area(
        "Descripción",
        value=st.session_state.get("cat_desc", "")
    )

    if not st.session_state.modo_edicion_cat:
        if st.button("Registrar"):
            try:
                registrar_categoria(nombre, descripcion)
                st.success("✅ Categoría registrada correctamente")
                st.rerun()
            except ValueError as e:
                st.warning(f"⚠️ {e}")
    else:
        if st.button("Guardar"):
            try:
                editar_categoria(
                    st.session_state.categoria_sel["ID"],
                    nombre,
                    descripcion
                )
                st.success("✏️ Categoría actualizada")
                st.session_state.modo_edicion_cat = False
                st.session_state.categoria_sel = None
                st.session_state.clear()
                st.rerun()
            except ValueError as e:
                st.warning(f"⚠️ {e}")

    st.divider()

    # ===== TABLA =====
    st.subheader("Lista de categorías")

    categorias = obtener_categorias().data

    if not categorias:
        st.info("No hay categorías registradas")
        return

    tabla = []
    for c in categorias:
        tabla.append({
            "": False,
            "ID": c["id"],
            "Nombre": c["nombre"],
            "Descripción": c["descripcion"]
        })

    edited = st.data_editor(
        tabla,
        hide_index=True,
        use_container_width=True
    )

    seleccionados = [row for row in edited if row[""]]

    if not seleccionados and st.session_state.modo_edicion_cat:
        st.session_state.modo_edicion_cat = False
        st.session_state.categoria_sel = None

    col1, col2 = st.columns([8, 2])
    with col2:
        if st.button(
            "✏️ Editar",
            disabled=not seleccionados
        ):
            c = seleccionados[0]
            st.session_state.modo_edicion_cat = True
            st.session_state.categoria_sel = c
            st.session_state.cat_nombre = c["Nombre"]
            st.session_state.cat_desc = c["Descripción"]
            st.rerun()
