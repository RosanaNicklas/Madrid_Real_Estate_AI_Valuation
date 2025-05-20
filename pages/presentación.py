import streamlit as st

st.title("🔍 Insights Clave del Proyecto")

st.header("1. Objetivo del Modelo")
st.markdown("""
    El modelo fue entrenado para predecir **precios de viviendas** basado en:
    - Metros cuadrados.
    - Número de habitaciones.
    - Ubicación (zona).
""")

st.header("2. Resultados Importantes")
st.subheader("📌 Feature Importance")
st.image("Madrid_blackwhite.jpeg", caption="Variables más relevantes según el modelo.")

st.subheader("📌 Métricas de Rendimiento")
st.table({
    "Métrica": ["MAE", "RMSE", "R²"],
    "Valor": [45.2, 62.8, 0.89]
})

st.header("3. Conclusiones")
st.markdown("""
    - 🎯 El modelo logra un **R² de 0.89**, lo que indica un buen ajuste.
    - 📌 La variable **`metros_cuadrados`** es la más influyente.
    - ⚠️ Las casas en **zonas rurales** tienen menor valor predictivo.
""")