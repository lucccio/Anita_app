from app.database.conexion import supabase

# LISTAR DETALLES POR PRODUCTO
def listar_detalles_producto(producto_id: str):
    return (
        supabase
        .table("detalle_productos")
        .select("*")
        .eq("producto_id", producto_id)
        .execute()
    )

# INSERTAR DETALLE
def insertar_detalle_producto(detalle: dict):
    return (
        supabase
        .table("detalle_productos")
        .insert(detalle)
        .execute()
    )

# ACTUALIZAR DETALLE
def actualizar_detalle_producto(detalle_id: str, datos: dict):
    return (
        supabase
        .table("detalle_productos")
        .update(datos)
        .eq("id", detalle_id)
        .execute()
    )

# ELIMINAR DETALLE
def eliminar_detalle_producto(detalle_id: str):
    return (
        supabase
        .table("detalle_productos")
        .delete()
        .eq("id", detalle_id)
        .execute()
    )
