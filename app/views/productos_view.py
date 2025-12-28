import streamlit as st
from app.logic.productos_logic import registrar_producto, obtener_productos

def vista_productos():
    st.subheader("Gestión de Productos")

    st.write("Formulario de registro")

    nombre = st.text_input("Nombre del producto")
    descripcion = st.text_area("Descripción")
    precio = st.number_input("Precio", min_value=0.0, step=0.1)
    from app.logic.categorias_logic import obtener_categorias

    # Obtener categorías
    categorias = obtener_categorias().data

    # Validar si hay categorías
    if not categorias:
        st.warning("No hay categorías registradas. Registra una primero.")
        return

    # Crear diccionario: Nombre visible -> ID real
    opciones = {c["nombre"]: c["id"] for c in categorias}

    categoria_seleccionada = st.selectbox(
        "Seleccionar Categoría",
        list(opciones.keys())
    )

    categoria_id = opciones[categoria_seleccionada]


    if st.button("Registrar producto"):
        try:
            registrar_producto(nombre, descripcion, precio, categoria_id)
            st.success("Producto registrado correctamente")
            st.rerun()
        except Exception as e:
            st.error(str(e))

    st.divider()

    st.subheader("📦 Lista de productos")

    productos = obtener_productos().data

    if not productos:
        st.info("No hay productos registrados")
        return

    tabla = []
    for p in productos:
        tabla.append({
            "ID": p["id"],
            "Nombre": p["nombre"],
            "Descripción": p["descripcion"],
            "Precio": p["precio"],
            "Categoría": p["categoria_id"],
        })

    st.dataframe(tabla, use_container_width=True)
