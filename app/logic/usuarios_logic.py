from app.database.usuarios_db import (
    insertar_usuario,
    buscar_usuario_por_email,
    listar_usuarios,
    actualizar_usuario
)
import hashlib
import re


# ================= VALIDADORES =================
def validar_texto(campo, nombre_campo):
    if not re.fullmatch(r"[A-Za-zÁÉÍÓÚáéíóúÑñ ]+", campo):
        raise ValueError(f"{nombre_campo} solo debe contener letras")


def validar_email(email):
    patron = r"^[\w\.-]+@gmail\.com$"
    if not re.match(patron, email):
        raise ValueError("Correo inválido (solo @gmail.com)")


def validar_password(password):
    if len(password) < 8:
        raise ValueError("La contraseña debe tener mínimo 8 caracteres")
    if not any(c.isdigit() for c in password):
        raise ValueError("La contraseña debe contener al menos un número")


# ================= REGISTRAR =================
def registrar_usuario(nombre, apellido, dni, telefono, email, password):
    nombre = nombre.strip()
    apellido = apellido.strip()
    dni = dni.strip()
    telefono = telefono.strip()
    email = email.strip()
    password = password.strip()

    if not all([nombre, apellido, dni, telefono, email, password]):
        raise ValueError("No se permiten campos vacíos")

    validar_texto(nombre, "Nombre")
    validar_texto(apellido, "Apellido")

    if not dni.isdigit() or len(dni) != 8:
        raise ValueError("El DNI debe tener exactamente 8 dígitos")

    if not telefono.isdigit() or len(telefono) != 9:
        raise ValueError("El teléfono debe tener exactamente 9 dígitos")

    validar_email(email)
    validar_password(password)

    if buscar_usuario_por_email(email).data:
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


# ================= LISTAR =================
def obtener_usuarios():
    return listar_usuarios()


# ================= EDITAR =================
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

    validar_texto(nombre, "Nombre")
    validar_texto(apellido, "Apellido")

    if not dni.isdigit() or len(dni) != 8:
        raise ValueError("El DNI debe tener exactamente 8 dígitos")

    if not telefono.isdigit() or len(telefono) != 9:
        raise ValueError("El teléfono debe tener exactamente 9 dígitos")

    validar_email(email)

    datos_actualizados = {
        "nombre": nombre,
        "apellido": apellido,
        "dni": dni,
        "telefono": telefono,
        "email": email
    }

    return actualizar_usuario(usuario_id, datos_actualizados)
