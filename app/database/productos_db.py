from app.database.conexion import supabase

def insertar_producto(producto: dict):
    return (
        supabase
        .table("productos")
        .insert(producto)
        .execute()
    )

def listar_productos():
    return (
        supabase
        .table("productos")
        .select(
            "id, nombre, descripcion, precio, categoria_id, estado, fecha_creacion"
        )
        .order("id")
        .execute()
    )

def actualizar_producto(producto_id: int, datos: dict):
    return (
        supabase
        .table("productos")
        .update(datos)
        .eq("id", producto_id)
        .execute()
    )
