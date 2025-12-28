from app.database.detalle_productos_db import (
    insertar_detalle_producto,
    listar_detalles_por_producto
)

def registrar_detalle_producto(
    producto_id,
    color,
    talla,
    genero,
    stock
):
    if not producto_id:
        raise ValueError("Producto inválido")

    if not all([color, talla, genero]):
        raise ValueError("No se permiten campos vacíos")

    if stock < 0:
        raise ValueError("El stock no puede ser negativo")

    detalle = {
        "producto_id": producto_id,
        "color": color.strip().lower(),
        "talla": talla,
        "genero": genero,
        "stock": stock
    }

    return insertar_detalle_producto(detalle)

def obtener_detalles_por_producto(producto_id: int):
    return listar_detalles_por_producto(producto_id)
