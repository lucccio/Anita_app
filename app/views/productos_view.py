import streamlit as st
from app.logic.productos_logic import (
    registrar_producto,
    obtener_productos
)
from app.logic.categorias_logic import obtener_categorias


def vista_productos():
    st.subheader("Gestión de Productos")

    # ========== FORMULARIO ==========
    st.write("Formulario de registro")

    # ========= FORM ==========
    nombre = st.text_input("Nombre del producto")
    descripcion = st.text_area("Descripción")

    precio = st.number_input(
        "Precio",
        min_value=0.0,
        step=0.1,
        format="%.2f"
    )

    # Obtener categorías
    categorias = obtener_categorias().data

    if not categorias:
        st.warning("⚠️ No hay categorías registradas. Registra una primero.")
        return

    opciones = {c["nombre"]: c["id"] for c in categorias}

    categoria_nombre = st.selectbox(
        "Seleccionar categoría",
        list(opciones.keys())
    )
                precio,
                categoria_id
            )
            st.success("✅ Producto registrado correctamente")
            st.rerun()

        except ValueError as e:
            st.warning(f"⚠️ {e}")
        except Exception as e:
            st.error("❌ Error inesperado")
            st.write(e)

    st.divider()

    productos = obtener_productos().data

    if not productos:
        st.info("No hay productos registrados")
        return

    map_categorias = {c["id"]: c["nombre"] for c in categorias}

    tabla = []
    for p in productos:
        tabla.append({
            "ID": p["id"],
            "Nombre": p["nombre"],
            "Descripción": p["descripcion"],
            "Precio": p["precio"],
            "Categoría": map_categorias.get(p["categoria_id"], "Sin categoría")
        })

    st.dataframe(tabla, use_container_width=True)
