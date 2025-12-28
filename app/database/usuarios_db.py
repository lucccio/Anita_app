from app.database.conexion import supabase

def insertar_usuario(usuario: dict):
    return supabase.table("usuarios").insert(usuario).execute()

def buscar_usuario_por_email(email: str):
    return (
        supabase
        .table("usuarios")
        .select("id")
        .eq("email", email)
        .execute()
    )

def actualizar_usuario(usuario_id: int, datos: dict):
    return (
        supabase
        .table("usuarios")
        .update(datos)
        .eq("id", usuario_id)
        .execute()
    )

def listar_usuarios():
    return supabase.table("usuarios").select("*").execute()
