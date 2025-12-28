from app.database.conexion import supabase

# INSERTAR PRODUCTO
def insertar_producto(producto: dict):
    return (
        supabase
        .table("productos")
        .insert(producto)
        .execute()
    )

# LISTAR PRODUCTOS
def listar_productos():
    return (
        supabase
        .table("productos")
    return (
        supabase
        .table("productos")
        .update(datos)
        .eq("id", producto_id)
        .execute()
    )

# ELIMINAR PRODUCTO (por si luego lo necesitas)
def eliminar_producto(producto_id: str):
    return (
        supabase
        .table("productos")
        .delete()
        .eq("id", producto_id)
        .execute()
    )
