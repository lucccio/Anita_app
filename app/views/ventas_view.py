import streamlit as st
from app.logic.ventas_logic import (
    registrar_venta,
    obtener_ventas,
    editar_venta
)
from app.logic.usuarios_logic import obtener_usuarios
from app.logic.productos_logic import obtener_productos


# =========================
# CANCELAR SELECCIÓN
# =========================
def cancelar_venta():
    st.session_state.modo_edicion_venta = False
    st.session_state.venta_sel = None

    for k in [
        "usuario_id",
        "producto_id",
        "cantidad",
        "precio_unitario"
    ]:
        st.session_state.pop(k, None)


# =========================
# VISTA VENTAS
# =========================
def vista_ventas():
    st.subheader("💸 Gestión de Ventas")

    # ===== ESTADOS =====
    if "modo_edicion_venta" not in st.session_state:
        st.session_state.modo_edicion_venta = False

    if "venta_sel" not in st.session_state:
        st.session_state.venta_sel = None

    # ===== USUARIOS =====
    usuarios = obtener_usuarios().data
    if not usuarios:
        st.warning("⚠️ No hay usuarios registrados")
        return

    user_map = {
        f'{u["nombre"]} {u["apellido"]} (ID {u["id"]})': u["id"]
        for u in usuarios
    }

    user_keys = list(user_map.keys())
    user_index = 0

    if st.session_state.modo_edicion_venta and "usuario_id" in st.session_state:
        for i, k in enumerate(user_keys):
            if user_map[k] == st.session_state.usuario_id:
                user_index = i
                break

    usuario = st.selectbox(
        "Usuario",
        user_keys,
        index=user_index
    )
    usuario_id = user_map[usuario]

    # ===== PRODUCTOS =====
    productos = obtener_productos().data
    if not productos:
        st.warning("⚠️ No hay productos registrados")
        return

    prod_map = {
        f'{p["nombre"]} | S/ {p["precio"]}': p
        for p in productos
    }

    prod_keys = list(prod_map.keys())
    prod_index = 0

    if st.session_state.modo_edicion_venta and "producto_id" in st.session_state:
        for i, k in enumerate(prod_keys):
            if prod_map[k]["id"] == st.session_state.producto_id:
                prod_index = i
                break

    producto = st.selectbox(
        "Producto",
        prod_keys,
        index=prod_index
    )

    producto_data = prod_map[producto]
    producto_id = producto_data["id"]
    precio_base = float(producto_data["precio"])

    # ===== FORMULARIO =====
    cantidad = st.number_input(
        "Cantidad",
        min_value=1,
        step=1,
        value=int(st.session_state.get("cantidad", 1))
    )

    precio_unitario = st.number_input(
        "Precio unitario (S/)",
        min_value=0.01,
        step=0.1,
        value=float(st.session_state.get("precio_unitario", precio_base))
    )

    # ===== VALIDACIONES VISUALES =====
    if cantidad <= 0:
        st.error("❌ La cantidad debe ser mayor a cero")
        return

    if precio_unitario <= 0:
        st.error("❌ El precio unitario debe ser mayor a cero")
        return

    total = cantidad * precio_unitario
    st.info(f"💰 Total de la venta: **S/ {total:.2f}**")

    # ===== BOTONES =====
    col1, col2 = st.columns(2)

    with col1:
        if not st.session_state.modo_edicion_venta:
            if st.button("➕ Registrar venta"):
                try:
                    registrar_venta(
                        usuario_id,
                        producto_id,
                        cantidad,
                        precio_unitario
                    )
                    st.success("✅ Venta registrada correctamente")
                    st.rerun()
                except ValueError as e:
                    st.warning(f"⚠️ {e}")
                except Exception:
                    st.error("❌ Error inesperado al registrar la venta")
        else:
            if st.button("💾 Guardar cambios"):
                try:
                    editar_venta(
                        st.session_state.venta_sel["ID"],
                        usuario_id,
                        producto_id,
                        cantidad,
                        precio_unitario
                    )
                    st.success("✏️ Venta actualizada correctamente")
                    cancelar_venta()
                    st.rerun()
                except ValueError as e:
                    st.warning(f"⚠️ {e}")
                except Exception:
                    st.error("❌ Error al actualizar la venta")

    with col2:
        if st.session_state.modo_edicion_venta:
            if st.button("❌ Cancelar selección"):
                cancelar_venta()
                st.rerun()

    st.divider()

    # ===== TABLA =====
    ventas = obtener_ventas().data
    if not ventas:
        st.info("No hay ventas registradas")
        return

    tabla = []
    for v in ventas:
        tabla.append({
            "Seleccionar": False,
            "ID": v["id"],
            "Usuario": f'{v["usuarios"]["nombre"]} {v["usuarios"]["apellido"]}',
            "Producto": v["productos"]["nombre"],
            "Cantidad": v["cantidad"],
            "Precio": v["precio_unitario"],
            "Total": v["total"],
            "Fecha": v["fecha_venta"]
        })

    edited = st.data_editor(
        tabla,
        hide_index=True,
        use_container_width=True
    )

    seleccionados = [r for r in edited if r["Seleccionar"]]

    if st.button("✏️ Editar", disabled=not seleccionados):
        v = seleccionados[0]

        st.session_state.modo_edicion_venta = True
        st.session_state.venta_sel = v

        st.session_state.usuario_id = next(
            u["id"] for u in usuarios
            if f'{u["nombre"]} {u["apellido"]}' == v["Usuario"]
        )

        st.session_state.producto_id = next(
            p["id"] for p in productos
            if p["nombre"] == v["Producto"]
        )

        st.session_state.cantidad = v["Cantidad"]
        st.session_state.precio_unitario = v["Precio"]

        st.rerun()
