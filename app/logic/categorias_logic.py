from app.database.categorias_db import (
    insertar_categoria,
    listar_categorias,
    actualizar_categoria,
    buscar_categoria_por_nombre
)
import re


# ================= VALIDADORES =================
def validar_nombre_categoria(nombre):
    if not re.fullmatch(r"[A-Za-zÁÉÍÓÚáéíóúÑñ ]+", nombre):
        raise ValueError("El nombre de la categoría solo debe contener letras")


def validar_descripcion(descripcion):
    if descripcion and not re.fullmatch(r"[A-Za-zÁÉÍÓÚáéíóúÑñ0-9 ,.\-\n]+", descripcion):
        raise ValueError("La descripción contiene caracteres no permitidos")


# ================= REGISTRAR =================
def registrar_categoria(nombre, descripcion):
    nombre = nombre.strip().lower()
    descripcion = descripcion.strip()

    if not nombre:
        raise ValueError("El nombre de la categoría es obligatorio")

    validar_nombre_categoria(nombre)
    validar_descripcion(descripcion)

    existe = buscar_categoria_por_nombre(nombre)
    if existe.data:
        raise ValueError("La categoría ya existe")

    categoria = {
        "nombre": nombre,
        "descripcion": descripcion
    }

    return insertar_categoria(categoria)


# ================= LISTAR =================
def obtener_categorias():
    return listar_categorias()


# ================= EDITAR =================
def editar_categoria(categoria_id, nombre, descripcion):
    if not categoria_id:
        raise ValueError("Categoría inválida")

    nombre = nombre.strip().lower()
    descripcion = descripcion.strip()

    if not nombre:
        raise ValueError("El nombre es obligatorio")

    validar_nombre_categoria(nombre)
    validar_descripcion(descripcion)

    datos = {
        "nombre": nombre,
        "descripcion": descripcion
    }

    return actualizar_categoria(categoria_id, datos)
