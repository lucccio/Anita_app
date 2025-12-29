from app.database.ventas_db import (
    insertar_venta,
    listar_ventas,
    actualizar_venta
)

def registrar_venta(usuario_id, producto_id, cantidad, precio_unitario):
    total = cantidad * precio_unitario

    venta = {
        "usuario_id": usuario_id,
        "producto_id": producto_id,
        "cantidad": cantidad,
        "precio_unitario": precio_unitario,
        "total": total
    }

    return insertar_venta(venta)

def editar_venta(venta_id, usuario_id, producto_id, cantidad, precio_unitario):
    total = cantidad * precio_unitario

    data = {
        "usuario_id": usuario_id,
        "producto_id": producto_id,
        "cantidad": cantidad,
        "precio_unitario": precio_unitario,
        "total": total
    }

    return actualizar_venta(venta_id, data)

def obtener_ventas():
    return listar_ventas()
