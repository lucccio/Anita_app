import streamlit as st
from app.logic.productos_logic import (
    registrar_producto,
    obtener_productos,
    editar_producto
)
from app.logic.categorias_logic import obtener_categorias


def vista_productos():
    st.subheader("📦 Gestión de Productos")

    # ================= ESTADOS =================
    if "modo_edicion_producto" not in st.session_state:
        st.session_state.modo_edicion_producto = False

    if "producto_seleccionado" not in st.session_state:
        st.session_state.producto_seleccionado = None

    # ================= CATEGORÍAS =================
    categorias = obtener_categorias().data
    if not categorias:
        st.warning("⚠️ No hay categorías registradas")
        return

    map_nombre_id = {c["nombre"]: c["id"] for c in categorias}
    map_id_nombre = {c["id"]: c["nombre"] for c in categorias}

    # ================= FORMULARIO =================
    nombre = st.text_input(
        "Nombre",
        value=st.session_state.get("nombre", "")
    )

    descripcion = st.text_area(
        "Descripción",
        value=st.session_state.get("descripcion", "")
    )

    precio = st.number_input(
        "Precio",
        min_value=0.0,
        step=0.1,
        value=float(st.session_state.get("precio", 0.0))
    )

    categoria_nombre = st.selectbox(
        "Categoría",
        options=list(map_nombre_id.keys()),
        index=list(map_nombre_id.keys()).index(
            st.session_state.get("categoria_nombre",
            list(map_nombre_id.keys())[0])
        )
    )

    categoria_id = map_nombre_id[categoria_nombre]

    # ================= BOTONES =================
    if not st.session_state.modo_edicion_producto:
        if st.button("Registrar producto"):
            try:
                registrar_producto(
                    nombre,
                    descripcion,
                    precio,
                    categoria_id
                )
                st.success("✅ Producto registrado")
                st.rerun()
            except ValueError as e:
                st.warning(f"⚠️ {e}")
            except Exception as e:
                st.error("❌ Error inesperado")
                st.write(e)
    else:
        if st.button("Guardar cambios"):
            try:
                editar_producto(
                    st.session_state.producto_seleccionado["ID"],
                    nombre,
                    descripcion,
                    precio,
                    categoria_id
                )
                st.success("✏️ Producto actualizado")

                # limpiar estados
                st.session_state.modo_edicion_producto = False
                st.session_state.producto_seleccionado = None
                for k in ["nombre", "descripcion", "precio", "categoria_nombre"]:
                    st.session_state.pop(k, None)

                st.rerun()
            except Exception as e:
                st.error("❌ Error al actualizar")
                st.write(e)

    st.divider()

    # ================= TABLA =================
    st.subheader("📋 Lista de productos")

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
            "Categoría": map_id_nombre.get(p["categoria_id"], "Sin categoría")
        })

    edited = st.data_editor(
        tabla,
        hide_index=True,
        use_container_width=True
    )

    seleccionados = [row for row in edited if row[""]]

    col1, col2 = st.columns([8, 2])
    with col2:
        if st.button("✏️ Editar", disabled=not seleccionados):
            p = seleccionados[0]

            st.session_state.modo_edicion_producto = True
            st.session_state.producto_seleccionado = p

            st.session_state.nombre = p["Nombre"]
            st.session_state.descripcion = p["Descripción"]
            st.session_state.precio = p["Precio"]
            st.session_state.categoria_nombre = p["Categoría"]

            st.rerun()
