from app.database.productos_db import (
    insertar_producto,
    listar_productos,
    actualizar_producto
)


def registrar_producto(
    nombre,
    precio,
    descripcion,
    categoria_id,
    color,
    talla,
    genero,
    stock
):
    producto = {
        "nombre": nombre,
        "precio": precio,
        "descripcion": descripcion,
        "categoria_id": int(categoria_id),  # ✅ FORZADO A INT
        "color": color,
        "talla": talla,
        "genero": genero,
        "stock": int(stock)                 # ✅ FORZADO A INT
    }

    return insertar_producto(producto)


def obtener_productos():
    return listar_productos()


def editar_producto(producto_id, datos: dict):
    if not producto_id:
        raise ValueError("Producto inválido")

    return actualizar_producto(producto_id, datos)
