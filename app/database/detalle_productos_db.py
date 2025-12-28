from app.database.conexion import supabase

def insertar_detalle_producto(detalle: dict):
    return (
        supabase
        .table("detalle_productos")
        .insert(detalle)
        .execute()
    )

def listar_detalles():
    return (
        supabase
        .table("detalle_productos")
        .select("*")
        .order("id")
        .execute()
    )

def listar_detalles_por_producto(producto_id: int):
    return (
        supabase
        .table("detalle_productos")
        .select("*")
        .eq("producto_id", producto_id)
        .order("id")
        .execute()
    )

def actualizar_detalle(detalle_id: int, datos: dict):
    return (
        supabase
        .table("detalle_productos")
        .update(datos)
        .eq("id", detalle_id)
        .execute()
    )

def eliminar_detalle(detalle_id: int):
    return (
        supabase
        .table("detalle_productos")
        .delete()
        .eq("id", detalle_id)
        .execute()
    )
