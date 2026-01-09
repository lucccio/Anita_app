import streamlit as st
import re
from app.logic.categorias_logic import (
    registrar_categoria,
    editar_categoria,
    obtener_categorias
)

# ================= VALIDADORES FRONTEND =================
def solo_letras(texto):
    return bool(re.fullmatch(r"[A-Za-zÁÉÍÓÚáéíóúÑñ ]*", texto))

def descripcion_valida(texto):
    return bool(re.fullmatch(r"[A-Za-zÁÉÍÓÚáéíóúÑñ0-9 ,.\-\n]*", texto))


def vista_categorias():
    st.subheader("📚 Gestión de Categorías")

    # ========= ESTADOS =========
    if "modo_edicion_cat" not in st.session_state:
        st.session_state.modo_edicion_cat = False

    if "categoria_seleccionada" not in st.session_state:
        st.session_state.categoria_seleccionada = None

    # ========= FORMULARIO =========
    nombre = st.text_input(
        "Nombre",
        value=st.session_state.get("cat_nombre", ""),
        help="Solo letras (obligatorio)"
    )

    if nombre and not solo_letras(nombre):
        st.error("❌ El nombre solo puede contener letras")
        return

    descripcion = st.text_area(
        "Descripción",
        value=st.session_state.get("cat_descripcion", ""),
        help="Texto libre (sin símbolos extraños)"
    )

    if descripcion and not descripcion_valida(descripcion):
        st.error("❌ La descripción contiene caracteres no permitidos")
        return

    col_a, col_b = st.columns(2)

    # ========= BOTONES =========
    with col_a:
        if not st.session_state.modo_edicion_cat:
            if st.button("➕ Registrar"):
                try:
                    registrar_categoria(nombre, descripcion)
                    st.success("✅ Categoría registrada correctamente")
                    st.rerun()
                except ValueError as e:
                    st.warning(f"⚠️ {e}")
                except Exception:
                    st.error("❌ Error inesperado")
        else:
            if st.button("💾 Guardar cambios"):
                try:
                    editar_categoria(
                        st.session_state.categoria_seleccionada["ID"],
                        nombre,
                        descripcion
                    )
                    st.success("✏️ Categoría actualizada correctamente")
                    limpiar_estado_categoria()
                    st.rerun()
                except ValueError as e:
                    st.warning(f"⚠️ {e}")
                except Exception:
                    st.error("❌ Error al actualizar")

    with col_b:
        if st.session_state.modo_edicion_cat:
            if st.button("❌ Cancelar selección"):
                limpiar_estado_categoria()
                st.rerun()

    st.divider()

    # ========= TABLA =========
    categorias = obtener_categorias().data

    if not categorias:
        st.info("No hay categorías registradas")
        return

    tabla = []
    for c in categorias:
        tabla.append({
            "Seleccionar": False,
            "ID": c["id"],
            "Nombre": c["nombre"],
            "Descripción": c["descripcion"]
        })

    edited = st.data_editor(
        tabla,
        hide_index=True,
        use_container_width=True
    )

    seleccionados = [row for row in edited if row["Seleccionar"]]

    col1, col2 = st.columns([8, 2])
    with col2:
        if st.button("✏️ Editar", disabled=not seleccionados):
            c = seleccionados[0]
            st.session_state.modo_edicion_cat = True
            st.session_state.categoria_seleccionada = c
            st.session_state.cat_nombre = c["Nombre"]
            st.session_state.cat_descripcion = c["Descripción"]
            st.rerun()


# ================= UTIL =================
def limpiar_estado_categoria():
    st.session_state.modo_edicion_cat = False
    st.session_state.categoria_seleccionada = None
    for k in ["cat_nombre", "cat_descripcion"]:
        st.session_state.pop(k, None)
