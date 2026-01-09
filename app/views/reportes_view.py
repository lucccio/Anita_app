import streamlit as st
from app.logic.reportes_logic import (
    obtener_reporte_general,
    obtener_reporte_por_fecha
)


def vista_reportes():
    st.subheader("📈📉 Reportes de Ventas")

    opcion = st.selectbox(
        "🧾 Tipo de reporte",
        ["General", "Por Fecha"]
    )

    ventas = []

    if opcion == "General":
        try:
            ventas = obtener_reporte_general().data
        except Exception:
            st.error("❌ Error al obtener el reporte general")
            return

    elif opcion == "Por Fecha":
        col1, col2 = st.columns(2)

        with col1:
            inicio = st.date_input("Fecha inicio")
        with col2:
            fin = st.date_input("Fecha fin")

        if inicio > fin:
            st.error("❌ La fecha inicio no puede ser mayor que la fecha fin")
            return

        if st.button("📊 Generar reporte"):
            try:
                ventas = obtener_reporte_por_fecha(
                    str(inicio),
                    str(fin)
                ).data
            except ValueError as e:
                st.warning(f"⚠️ {e}")
                return
            except Exception:
                st.error("❌ Error al generar el reporte")
                return

    st.divider()

    if not ventas:
        st.info("No hay datos para mostrar")
        return

    # ===== TABLA =====
    tabla = []
    for v in ventas:
        tabla.append({
            "ID": v["id"],
            "Cliente": f'{v["usuarios"]["nombre"]} {v["usuarios"]["apellido"]}',
            "Producto": v["productos"]["nombre"],
            "Fecha": v["fecha_venta"],
            "Total (S/)": v["total"]
        })

    st.dataframe(tabla, use_container_width=True)

    # ===== TOTAL =====
    total_vendido = sum(v["Total (S/)"] for v in tabla)
    st.success(f"💰 TOTAL VENDIDO: **S/ {total_vendido:.2f}**")
