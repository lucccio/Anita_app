from app.database.ventas_db import (
    insertar_venta,
    listar_ventas,
    actualizar_venta
)


def registrar_venta(usuario_id, producto_id, cantidad, precio_unitario):
    # ===== VALIDACIONES =====
    if not usuario_id:
        raise ValueError("Usuario inválido")

    if not producto_id:
        raise ValueError("Producto inválido")

    try:
        cantidad = int(cantidad)
    except:
        raise ValueError("La cantidad debe ser un número entero")

    if cantidad <= 0:
        raise ValueError("La cantidad debe ser mayor a cero")

    try:
        precio_unitario = float(precio_unitario)
    except:
        raise ValueError("El precio unitario debe ser un número")

    if precio_unitario <= 0:
        raise ValueError("El precio unitario debe ser mayor a cero")

    total = cantidad * precio_unitario

    venta = {
        "usuario_id": int(usuario_id),
        "producto_id": int(producto_id),
        "cantidad": cantidad,
        "precio_unitario": precio_unitario,
        "total": total
    }

    return insertar_venta(venta)


def editar_venta(venta_id, usuario_id, producto_id, cantidad, precio_unitario):
    if not venta_id:
        raise ValueError("Venta inválida")

    if not usuario_id:
        raise ValueError("Usuario inválido")

    if not producto_id:
        raise ValueError("Producto inválido")

    try:
        cantidad = int(cantidad)
    except:
        raise ValueError("La cantidad debe ser un número entero")

    if cantidad <= 0:
        raise ValueError("La cantidad debe ser mayor a cero")

    try:
        precio_unitario = float(precio_unitario)
    except:
        raise ValueError("El precio unitario debe ser un número")

    if precio_unitario <= 0:
        raise ValueError("El precio unitario debe ser mayor a cero")

    total = cantidad * precio_unitario

    data = {
        "usuario_id": int(usuario_id),
        "producto_id": int(producto_id),
        "cantidad": cantidad,
        "precio_unitario": precio_unitario,
        "total": total
    }

    return actualizar_venta(venta_id, data)


def obtener_ventas():
    return listar_ventas()
