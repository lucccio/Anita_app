from app.database.conexion import supabase

def insertar_venta(venta: dict):
    return supabase.table("ventas").insert(venta).execute()

def actualizar_venta(venta_id: int, data: dict):
    return (
        supabase
        .table("ventas")
        .update(data)
        .eq("id", venta_id)
        .execute()
    )

def listar_ventas():
    return (
        supabase
        .table("ventas")
        .select("""
            id,
            fecha_venta,
            cantidad,
            precio_unitario,
            total,
            estado,
            usuarios(nombre, apellido),
            productos(nombre)
        """)
        .order("fecha_venta", desc=True)
        .execute()
    )
