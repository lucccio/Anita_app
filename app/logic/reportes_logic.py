from app.database.reportes_db import (
    reporte_ventas_general,
    reporte_ventas_por_fecha,
    reporte_totales
)
from datetime import date


def obtener_reporte_general():
    return reporte_ventas_general()


def obtener_reporte_por_fecha(fecha_inicio, fecha_fin):
    if not fecha_inicio or not fecha_fin:
        raise ValueError("Debe seleccionar ambas fechas")

    if fecha_inicio > fecha_fin:
        raise ValueError("La fecha inicio no puede ser mayor que la fecha fin")

    return reporte_ventas_por_fecha(fecha_inicio, fecha_fin)


def obtener_totales():
    return reporte_totales()
