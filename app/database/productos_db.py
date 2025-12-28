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
        .select("*")
        .order("fecha_creacion", desc=True)
        .execute()
    )

# OBTENER PRODUCTO POR ID
def obtener_producto_por_id(producto_id: str):
    return (
        supabase
        .table("productos")
        .select("*")
        .eq("id", producto_id)
        .single()
        .execute()
    )

# BUSCAR POR NOMBRE (opcional pero útil)
def buscar_producto_por_nombre(nombre: str):
    return (
        supabase
        .table("productos")
        .select("id")
        .ilike("nombre", nombre)
        .execute()
    )

# ACTUALIZAR PRODUCTO
def actualizar_producto(producto_id: str, datos: dict):
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
