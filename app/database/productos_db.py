from app.database.conexion import supabase

def insertar_producto(producto: dict):
    return supabase.table("productos").insert(producto).execute()

def listar_productos():
    return supabase.table("productos").select("*").execute()

def actualizar_producto(producto_id: str, datos: dict):
    return (
        supabase
        .table("productos")
        .update(datos)
        .eq("id", producto_id)
        .execute()
    )
