import streamlit as st
from app.logic.reportes_logic import (
    obtener_reporte_general,
    obtener_reporte_por_fecha
)

def vista_reportes():
    st.subheader("📈 📉  Reportes de Ventas")

    opcion = st.selectbox(
        "🧾 Selecciona tipo de reporte",
        ["General", "Por Fecha"]
    )

    if opcion == "General":
        ventas = obtener_reporte_general().data

    elif opcion == "Por Fecha":
        col1, col2 = st.columns(2)
        with col1:
            inicio = st.date_input("Fecha inicio")
        with col2:
            fin = st.date_input("Fecha fin")

        if st.button("Generar reporte"):
            ventas = obtener_reporte_por_fecha(
                str(inicio),
                str(fin)
            ).data
        else:
            ventas = []

    st.divider()

    if not ventas:
        st.info("No hay datos para mostrar")
        return

    tabla = []
    for v in ventas:
        tabla.append({
            "ID": v["id"],
            "Cliente": f'{v["usuarios"]["nombre"]} {v["usuarios"]["apellido"]}',
            "Producto": v["productos"]["nombre"],
            "Fecha": v["fecha_venta"],
            "Total": v["total"]
        })

    st.dataframe(tabla, use_container_width=True)

    total = sum(v["Total"] for v in tabla)
    st.success(f"💰 TOTAL VENDIDO: S/ {total:.2f}")
