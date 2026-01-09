import streamlit as st
import re
from app.logic.productos_logic import (
    registrar_producto,
    obtener_productos,
    editar_producto
)
from app.logic.categorias_logic import obtener_categorias


# ================= VALIDADORES =================
def texto_valido(texto):
    return bool(re.fullmatch(r"[A-Za-zÁÉÍÓÚáéíóúÑñ0-9 ,.\-]*", texto))


def solo_letras(texto):
    return bool(re.fullmatch(r"[A-Za-zÁÉÍÓÚáéíóúÑñ ]*", texto))


# ================= UTIL =================
def cancelar_producto():
    st.session_state.modo_edicion_producto = False
    st.session_state.producto_sel = None
    for k in [
        "nombre", "descripcion", "precio",
        "color", "talla", "genero", "stock"
    ]:
        st.session_state.pop(k, None)


# ================= VISTA =================
def vista_productos():
    st.subheader("📦 Productos")

    # ===== ESTADOS =====
    if "modo_edicion_producto" not in st.session_state:
        st.session_state.modo_edicion_producto = False

    if "producto_sel" not in st.session_state:
        st.session_state.producto_sel = None

    # ===== CATEGORÍAS =====
    categorias = obtener_categorias().data
    if not categorias:
        st.warning("No hay categorías registradas")
        return

    cat_map = {c["nombre"]: c["id"] for c in categorias}
    categoria = st.selectbox("Categoría", list(cat_map.keys()))
    categoria_id = cat_map[categoria]

    # ===== FORMULARIO =====
    nombre = st.text_input(
        "Nombre",
        value=st.session_state.get("nombre", ""),
        help="Solo letras"
    )

    if nombre and not solo_letras(nombre):
        st.error("❌ El nombre solo puede contener letras")
        return

    descripcion = st.text_area(
        "Descripción",
        value=st.session_state.get("descripcion", "")
    )

    if descripcion and not texto_valido(descripcion):
        st.error("❌ Descripción con caracteres no permitidos")
        return

    precio = st.number_input(
        "Precio",
        min_value=0.0,
        step=0.1,
        value=float(st.session_state.get("precio", 0.0))
    )

    color = st.text_input(
        "Color",
        value=st.session_state.get("color", ""),
        help="Solo letras"
    )

    if color and not solo_letras(color):
        st.error("❌ El color solo puede contener letras")
        return

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
        step=1,
        value=int(st.session_state.get("stock", 0))
    )

    # ===== BOTONES =====
    col1, col2 = st.columns(2)

    with col1:
        if not st.session_state.modo_edicion_producto:
            if st.button("➕ Registrar producto"):
                try:
                    registrar_producto(
                        nombre,
                        precio,
                        descripcion,
                        categoria_id,
                        color,
                        talla,
                        genero,
                        stock
                    )
                    st.success("✅ Producto registrado correctamente")
                    st.rerun()
                except ValueError as e:
                    st.warning(f"⚠️ {e}")
                except Exception:
                    st.error("❌ Error inesperado")
        else:
            if st.button("💾 Guardar cambios"):
                try:
                    editar_producto(
                        st.session_state.producto_sel["ID"],
                        {
                            "nombre": nombre,
                            "precio": precio,
                            "descripcion": descripcion,
                            "categoria_id": categoria_id,
                            "color": color,
                            "talla": talla,
                            "genero": genero,
                            "stock": stock
                        }
                    )
                    st.success("✏️ Producto actualizado")
                    cancelar_producto()
                    st.rerun()
                except ValueError as e:
                    st.warning(f"⚠️ {e}")
                except Exception:
                    st.error("❌ Error al actualizar")

    with col2:
        if st.session_state.modo_edicion_producto:
            if st.button("❌ Cancelar selección"):
                cancelar_producto()
                st.rerun()

    st.divider()

    # ===== TABLA =====
    productos = obtener_productos().data
    if not productos:
        st.info("No hay productos")
        return

    tabla = []
    for p in productos:
        tabla.append({
            "Seleccionar": False,
            "ID": p["id"],
            "Nombre": p["nombre"],
            "Categoría": p["categorias"]["nombre"],
            "Color": p["color"],
            "Talla": p["talla"],
            "Género": p["genero"],
            "Stock": p["stock"],
            "Precio": p["precio"]
        })

    edited = st.data_editor(
        tabla,
        hide_index=True,
        use_container_width=True
    )

    seleccionados = [r for r in edited if r["Seleccionar"]]

    if st.button("✏️ Editar", disabled=not seleccionados):
        p = seleccionados[0]
        st.session_state.modo_edicion_producto = True
        st.session_state.producto_sel = p

        st.session_state.nombre = p["Nombre"]
        st.session_state.precio = p["Precio"]
        st.session_state.stock = p["Stock"]

        st.rerun()
