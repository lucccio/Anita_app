from app.database.usuarios_db import (
    insertar_usuario,
    buscar_usuario_por_email,
    listar_usuarios,
    actualizar_usuario
)
import hashlib


def registrar_usuario(nombre, apellido, dni, telefono, email, password):
    # limpiar espacios
    nombre = nombre.strip()
    apellido = apellido.strip()
    dni = dni.strip()
    telefono = telefono.strip()
    email = email.strip()
    password = password.strip()

    # validaciones
    if not all([nombre, apellido, dni, telefono, email, password]):
        raise ValueError("No se permiten campos vacíos")

    if not dni.isdigit() or len(dni) != 8:
        raise ValueError("El DNI debe tener exactamente 8 dígitos")

    if not telefono.isdigit() or len(telefono) != 9:
        raise ValueError("El teléfono debe tener exactamente 9 dígitos")

    if not email.endswith("@gmail.com"):
        raise ValueError("Solo se permiten correos @gmail.com")

    existe = buscar_usuario_por_email(email)
    if existe.data:
        raise ValueError("El correo ya está registrado")

    password_hash = hashlib.sha256(password.encode()).hexdigest()

    usuario = {
        "nombre": nombre,
        "apellido": apellido,
        "dni": dni,
        "telefono": telefono,
        "email": email,
        "password": password_hash
    }

    return insertar_usuario(usuario)


def obtener_usuarios():
    return listar_usuarios()


def editar_usuario(usuario_id, nombre, apellido, dni, telefono, email):
    if not usuario_id:
        raise ValueError("Usuario inválido")

    nombre = nombre.strip()
    apellido = apellido.strip()
    dni = dni.strip()
    telefono = telefono.strip()
    email = email.strip()

    if not all([nombre, apellido, dni, telefono, email]):
        raise ValueError("No se permiten campos vacíos")

    if not dni.isdigit() or len(dni) != 8:
        raise ValueError("El DNI debe tener exactamente 8 dígitos")

    if not telefono.isdigit() or len(telefono) != 9:
        raise ValueError("El teléfono debe tener exactamente 9 dígitos")

    if not email.endswith("@gmail.com"):
        raise ValueError("Solo se permiten correos @gmail.com")

    datos_actualizados = {
        "nombre": nombre,
        "apellido": apellido,
        "dni": dni,
        "telefono": telefono,
        "email": email
    }

    return actualizar_usuario(usuario_id, datos_actualizados)

