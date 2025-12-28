from app.database.categorias_db import (
    insertar_categoria,
    listar_categorias,
    actualizar_categoria,
    buscar_categoria_por_nombre
)


def registrar_categoria(nombre, descripcion):
    nombre = nombre.strip()
    descripcion = descripcion.strip()

    if not nombre:
        raise ValueError("El nombre de la categoría es obligatorio")

    existe = buscar_categoria_por_nombre(nombre)
    if existe.data:
        raise ValueError("La categoría ya existe")

    categoria = {
        "nombre": nombre,
        "descripcion": descripcion
    }

    return insertar_categoria(categoria)


def obtener_categorias():
    return listar_categorias()


def editar_categoria(categoria_id, nombre, descripcion):
    if not categoria_id:
        raise ValueError("Categoría inválida")

    nombre = nombre.strip()
    descripcion = descripcion.strip()

    if not nombre:
        raise ValueError("El nombre es obligatorio")

    datos_actualizados = {
        "nombre": nombre,
        "descripcion": descripcion
    }

    return actualizar_categoria(categoria_id, datos_actualizados)
