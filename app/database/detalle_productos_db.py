from app.database.conexion import supabase

def insertar_detalle_producto(detalle: dict):
    return supabase.table("detalle_productos").insert(detalle).execute()

def listar_detalles():
    return (
        supabase
        .table("detalle_productos")
        .select(
            "id, producto_id, color, talla, genero, stock, estado, fecha_creacion"
        )
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
