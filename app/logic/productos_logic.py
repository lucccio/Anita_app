from app.database.productos_db import (
    insertar_producto,
    listar_productos,
    actualizar_producto
)


def _validar_nombre(nombre: str):
    if not nombre or not nombre.strip():
        raise ValueError("El nombre es obligatorio")

    if not nombre.replace(" ", "").isalpha():
        raise ValueError("El nombre solo debe contener letras")


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
    _validar_nombre(nombre)

    producto = {
        "nombre": nombre.strip(),
        "precio": float(precio),
        "descripcion": descripcion.strip(),
        "categoria_id": int(categoria_id),
        "color": color.strip(),
        "talla": talla,
        "genero": genero,
        "stock": int(stock)
    }

    return insertar_producto(producto)


def editar_producto(producto_id, datos: dict):
    if not producto_id:
        raise ValueError("Producto inválido")

    if "nombre" in datos:
        _validar_nombre(datos["nombre"])
        datos["nombre"] = datos["nombre"].strip()

    if "stock" in datos:
        datos["stock"] = int(datos["stock"])

    if "precio" in datos:
        datos["precio"] = float(datos["precio"])

    return actualizar_producto(producto_id, datos)


def obtener_productos():
    return listar_productos()
