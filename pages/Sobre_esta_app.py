# pages/acerca_de.py
import streamlit as st




st.title("ℹ️ Acerca de esta App")




st.markdown(
    """
    ¡Bienvenido a la aplicación de análisis del valor inmobiliario en Madrid!

    Esta aplicación es el resultado de un proyecto de fin de máster en Data Science,
    desarrollado con el objetivo de analizar y predecir los precios de la vivienda
    en la capital española.

    **¿Qué puedes encontrar en esta app?**

    * **Análisis Exploratorio de Datos (EDA):** Una exploración visual de los datos
        del mercado inmobiliario de Madrid para identificar patrones clave y tendencias.
    * **Entendimiento de los Datos:** Visualizaciones detalladas de las distribuciones
        de las características importantes y el análisis de las correlaciones entre ellas.
    * **Modelado Predictivo:** Información sobre el modelo de Machine Learning utilizado
        para predecir los precios de la vivienda y cómo se evaluó su rendimiento.
    * **Predicción de Precios:** Una herramienta interactiva donde puedes introducir
        características de una propiedad y obtener una predicción de su precio estimado.
    * **Evaluación del Modelo:** Métricas detalladas sobre la precisión y el rendimiento
        del modelo predictivo, así como análisis de los errores (residuales) y la
        importancia de las características.

    **Tecnologías Utilizadas:**

    * **Python:** El lenguaje de programación principal.
    * **Pandas:** Para la manipulación y el análisis de datos.
    * **NumPy:** Para operaciones numéricas.
    * **Matplotlib y Seaborn:** Para la visualización de datos estática.
    * **Plotly Express:** Para la creación de gráficos interactivos.
    * **Scikit-learn (sklearn):** Para las herramientas de Machine Learning (modelado,
        evaluación, preprocesamiento).
    * **XGBoost:** El algoritmo de gradient boosting utilizado para la predicción.
    * **Streamlit:** El framework utilizado para construir y desplegar esta aplicación web interactiva.

    **Sobre el Desarrollador:**

    Este proyecto ha sido desarrollado por **Rosana Longares** como trabajo final del
    **Máster en Data Science** con **Nodd3r**.

    Puedes encontrar el código fuente de esta aplicación en [GitHub](https://github.com/RosanaNicklas/Madrid_Real_Estate_AI_Valuation) (reemplaza con tu repositorio real).

    ¡Espero que esta aplicación te sea útil e informativa! Si tienes alguna pregunta o comentario, no dudes en contactarme.
    """,
    unsafe_allow_html=True,
)

# ------------------- Información adicional -------------------
st.markdown("---")
st.subheader("📌 Sobre el Modelo")

tab1, tab2, tab3 = st.tabs(["📊 Modelo", "📈 Datos", "ℹ️ Ayuda"])

with tab1:
    st.markdown("""
    **🧠 Características del modelo predictivo:**
    - Algoritmo: XGBoost Regressor
    - Precisión: ~94.7% (R² score)
    - Entrenado con más de 20,000 propiedades
    - Actualizado: Enero 2024
    """)
    
    st.progress(0.947, text="Precisión del modelo: 94.7%")

with tab2:
    st.markdown("""
    **📚 Fuente de datos:**
    - Dataset original: 21,742 anuncios de vivienda
    - Periodo: 2022-2023
    - Variables principales consideradas:
        - Superficie, habitaciones, baños
        - Distrito y características de la zona
        - Comodidades y estado de la propiedad
    """)
   

with tab3:
    st.markdown("""
    **❓ Cómo usar esta herramienta:**
    1. Completa los datos de la propiedad en el panel izquierdo
    2. Haz clic en "Calcular Precio"
    3. Explora los resultados y comparativas
    
    **💡 Consejos:**
    - Para mayor precisión, completa todos los campos
    - Las predicciones son estimaciones basadas en datos históricos
    - Consulta con un profesional para valoraciones oficiales
    """)
    
    st.image("https://cdn-icons-png.flaticon.com/512/2232/2232688.png", width=100)


st.markdown("---")
st.subheader("Contacto")
st.write("Tu dirección de correo electrónico (rosana8longares@gmail.com)")
st.write("Tu perfil de LinkedIn (https://www.linkedin.com/in/rosanalongares/)")
# ... cualquier otra información de contacto que desees incluir

# ------------------- Footer -------------------
st.markdown("""
<hr style="margin-top: 3rem;">
<div style='text-align: center; color: gray; font-size: 0.9rem;'>
    Desarrollado por [Rosana Longares Herrero] • © 2025
</div>
""", unsafe_allow_html=True)


