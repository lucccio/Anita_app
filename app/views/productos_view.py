import streamlit as st
from app.logic.productos_logic import registrar_producto, obtener_productos

def vista_productos():
    st.subheader("Gestión de Productos")

    st.write("Formulario de registro")

    nombre = st.text_input("Nombre del producto")
    descripcion = st.text_area("Descripción")
    precio = st.number_input("Precio", min_value=0.0, step=0.1)
    stock = st.number_input("Stock", min_value=0, step=1)
    categoria_id = st.text_input("ID Categoría")

    if st.button("Registrar producto"):
        try:
            registrar_producto(nombre, descripcion, precio, stock, categoria_id)
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
            "Stock": p["stock"],
            "Categoría": p["categoria_id"],
            "Estado": "Activo" if p["estado"] else "Inactivo"
        })

    st.dataframe(tabla, use_container_width=True)
