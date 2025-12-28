from app.database.detalle_productos_db import (
    listar_detalles_producto,
    insertar_detalle_producto,
    actualizar_detalle_producto,
    eliminar_detalle_producto
)

def obtener_detalles_producto(producto_id):
    if not producto_id:
        raise ValueError("Producto inválido")
    return listar_detalles_producto(producto_id)

def registrar_detalle_producto(producto_id, color, talla, genero, stock):
    if not all([producto_id, color, talla, genero]):
        raise ValueError("Todos los campos son obligatorios")

    if stock < 0:
        raise ValueError("El stock no puede ser negativo")

    data = {
        "producto_id": producto_id,
        "color": color,
        "talla": talla,
        "genero": genero,
        "stock": stock
    }

    return insertar_detalle_producto(data)

def editar_detalle_producto(detalle_id, datos):
    return actualizar_detalle_producto(detalle_id, datos)

def borrar_detalle_producto(detalle_id):
    return eliminar_detalle_producto(detalle_id)
