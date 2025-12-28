from app.database.detalle_productos_db import (
    insertar_detalle_producto,
    listar_detalles,
    actualizar_detalle
)

def registrar_detalle(producto_id, color, talla, genero, stock):
    if not all([producto_id, color, talla, genero]):
        raise ValueError("No se permiten campos vacíos")

    if stock < 0:
        raise ValueError("El stock no puede ser negativo")

    detalle = {
        "producto_id": producto_id,
        "color": color.strip().lower(),
        "talla": talla,
        "genero": genero,
        "stock": int(stock)
    }

    return insertar_detalle_producto(detalle)

def obtener_detalles():
    return listar_detalles()

def editar_detalle(detalle_id, color, talla, genero, stock):
    if not detalle_id:
        raise ValueError("Detalle inválido")

    datos = {
        "color": color.strip().lower(),
        "talla": talla,
        "genero": genero,
        "stock": int(stock)
    }

    return actualizar_detalle(detalle_id, datos)
