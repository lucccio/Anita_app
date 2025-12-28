from app.database.productos_db import insertar_producto, listar_productos, actualizar_producto

def registrar_producto(nombre, descripcion, precio, stock, categoria_id):
    if not all([nombre, descripcion]):
        raise ValueError("No se permiten campos vacíos")

    if precio <= 0:
        raise ValueError("El precio debe ser mayor a 0")

    if stock < 0:
        raise ValueError("El stock no puede ser negativo")

    producto = {
        "nombre": nombre.strip(),
        "descripcion": descripcion.strip(),
        "precio": float(precio),
        "stock": int(stock),
        "categoria_id": categoria_id,
        "estado": True
    }

    return insertar_producto(producto)

def obtener_productos():
    return listar_productos()

def editar_producto(producto_id, nombre, descripcion, precio, stock, categoria_id, estado):
    if not producto_id:
        raise ValueError("Producto inválido")

    datos = {
        "nombre": nombre,
        "descripcion": descripcion,
        "precio": float(precio),
        "stock": int(stock),
        "categoria_id": categoria_id,
        "estado": estado
    }

    return actualizar_producto(producto_id, datos)
