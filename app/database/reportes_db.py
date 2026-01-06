from app.database.conexion import supabase

def reporte_ventas_general():
    return (
        supabase.table("ventas")
        .select("""
            id,
            fecha_venta,
            total,
            usuarios(nombre, apellido),
            productos(nombre)
        """)
        .order("fecha_venta", desc=True)
        .execute()
    )

def reporte_ventas_por_fecha(fecha_inicio, fecha_fin):
    return (
        supabase.table("ventas")
        .select("""
            id,
            fecha_venta,
            total,
            usuarios(nombre, apellido),
            productos(nombre)
        """)
        .gte("fecha_venta", fecha_inicio)
        .lte("fecha_venta", fecha_fin)
        .order("fecha_venta", desc=True)
        .execute()
    )

def reporte_totales():
    return (
        supabase.rpc("reporte_totales")  # ← función SQL opcional
        .execute()
    )
