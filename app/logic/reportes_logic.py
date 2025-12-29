from app.database.reportes_db import (
    reporte_ventas_general,
    reporte_ventas_por_fecha,
    reporte_totales
)

def obtener_reporte_general():
    return reporte_ventas_general()

def obtener_reporte_por_fecha(fecha_inicio, fecha_fin):
    return reporte_ventas_por_fecha(fecha_inicio, fecha_fin)

def obtener_totales():
    return reporte_totales()
