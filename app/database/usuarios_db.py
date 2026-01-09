from app.database.conexion import supabase

# ========== INSERTAR ==========
def insertar_usuario(usuario: dict):
    return (
        supabase
        .table("usuarios")
        .insert(usuario)
        .execute()
    )

# ========== LISTAR ==========
def listar_usuarios():
    return (
        supabase
        .table("usuarios")
        .select(
            "id, nombre, apellido, dni, telefono, email, fecha_creacion"
        )
        .order("id")
        .execute()
    )

# ========== OBTENER POR ID (para selección / edición) ==========
def obtener_usuario_por_id(usuario_id: int):
    return (
        supabase
        .table("usuarios")
        .select("*")
        .eq("id", usuario_id)
        .single()
        .execute()
    )

# ========== BUSCAR ==========
def buscar_usuario_por_email(email: str):
    return (
        supabase
        .table("usuarios")
        .select("id")
        .eq("email", email)
        .execute()
    )

def buscar_usuario_por_dni(dni: str):
    return (
        supabase
        .table("usuarios")
        .select("id")
        .eq("dni", dni)
        .execute()
    )

# ========== ACTUALIZAR ==========
def actualizar_usuario(usuario_id: int, datos: dict):
    return (
        supabase
        .table("usuarios")
        .update(datos)
        .eq("id", usuario_id)
        .execute()
    )

# ========== ELIMINAR ==========
def eliminar_usuario(usuario_id: int):
    return (
        supabase
        .table("usuarios")
        .delete()
        .eq("id", usuario_id)
        .execute()
    )
