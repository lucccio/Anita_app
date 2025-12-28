import streamlit as st
from app.logic.usuarios_logic import (
    registrar_usuario,
    editar_usuario,
    obtener_usuarios
)

def vista_usuarios():
    st.subheader("👤 Gestión de Usuarios")

    # ================= ESTADOS =================
    if "modo_edicion" not in st.session_state:
        st.session_state.modo_edicion = False

    if "usuario_seleccionado" not in st.session_state:
        st.session_state.usuario_seleccionado = None

    # ================= FORMULARIO =================
    nombre = st.text_input("Nombre", value=st.session_state.get("nombre", ""))
    apellido = st.text_input("Apellido", value=st.session_state.get("apellido", ""))
    dni = st.text_input("DNI", value=st.session_state.get("dni", ""), max_chars=8)
    telefono = st.text_input("Teléfono", value=st.session_state.get("telefono", ""), max_chars=9)
    email = st.text_input("Email", value=st.session_state.get("email", ""))
    password = st.text_input("Password", type="password")

    col1, col2 = st.columns(2)

    # ========= REGISTRAR =========
    if not st.session_state.modo_edicion:
        with col1:
            if st.button("➕ Registrar"):
                try:
                    registrar_usuario(nombre, apellido, dni, telefono, email, password)
                    st.success("✅ Usuario registrado correctamente")
                    st.rerun()
                except ValueError as e:
                    st.warning(f"⚠️ {e}")
                except Exception:
                    st.error("❌ Error inesperado")

    # ========= EDITAR =========
    else:
        with col1:
            if st.button("💾 Guardar cambios"):
                try:
                    editar_usuario(
                        st.session_state.usuario_seleccionado["ID"],
                        nombre, apellido, dni, telefono, email
                    )
                    st.success("✏️ Usuario actualizado correctamente")
                    limpiar_estado_usuario()
                    st.rerun()
                except ValueError as e:
                    st.warning(f"⚠️ {e}")
                except Exception:
                    st.error("❌ Error al actualizar")

        with col2:
            if st.button("❌ Cancelar selección"):
                limpiar_estado_usuario()
                st.rerun()

    st.divider()

    # ================= TABLA =================
    st.subheader("📋 Lista de usuarios")

    usuarios = obtener_usuarios().data

    if not usuarios:
        st.info("No hay usuarios registrados")
        return

    tabla = []
    for u in usuarios:
        tabla.append({
            "Seleccionar": False,
            "ID": u["id"],
            "Nombre": u["nombre"],
            "Apellido": u["apellido"],
            "DNI": u["dni"],
            "Teléfono": u["telefono"],
            "Email": u["email"],
        })

    edited = st.data_editor(
        tabla,
        hide_index=True,
        use_container_width=True
    )

    seleccionados = [row for row in edited if row["Seleccionar"]]

    col_a, col_b = st.columns([8, 2])
    with col_b:
        if st.button("✏️ Editar", disabled=not seleccionados):
            u = seleccionados[0]
            st.session_state.modo_edicion = True
            st.session_state.usuario_seleccionado = u

            st.session_state.nombre = u["Nombre"]
            st.session_state.apellido = u["Apellido"]
            st.session_state.dni = u["DNI"]
            st.session_state.telefono = u["Teléfono"]
            st.session_state.email = u["Email"]

            st.rerun()


# ================= UTIL =================
def limpiar_estado_usuario():
    st.session_state.modo_edicion = False
    st.session_state.usuario_seleccionado = None

    for k in ["nombre", "apellido", "dni", "telefono", "email"]:
        st.session_state.pop(k, None)
