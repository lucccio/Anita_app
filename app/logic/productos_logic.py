from app.database.productos_db import (
    insertar_producto,
    listar_productos,
    actualizar_producto
)

def registrar_producto(nombre, descripcion, precio, categoria_id):
    nombre = nombre.strip()
    descripcion = descripcion.strip()

    if not nombre or not descripcion:
        raise ValueError("No se permiten campos vacíos")

    if precio <= 0:
        raise ValueError("El precio debe ser mayor a 0")

    if not categoria_id:
        raise ValueError("Categoría inválida")

    producto = {
        "nombre": nombre,
        "descripcion": descripcion,
        "precio": float(precio),
        "categoria_id": categoria_id
    }

    return insertar_producto(producto)

def obtener_productos():
    return listar_productos()

def editar_producto(producto_id, nombre, descripcion, precio, categoria_id):
    if not producto_id:
        raise ValueError("Producto inválido")

    nombre = nombre.strip()
    descripcion = descripcion.strip()

    if not nombre or not descripcion:
        raise ValueError("No se permiten campos vacíos")

    if precio <= 0:
        raise ValueError("El precio debe ser mayor a 0")

    datos = {
        "nombre": nombre,
        "descripcion": descripcion,
        "precio": float(precio),
        "categoria_id": categoria_id
    }

    return actualizar_producto(producto_id, datos)
