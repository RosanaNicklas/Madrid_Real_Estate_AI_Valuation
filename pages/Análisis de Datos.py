# Analisis de Datos
import streamlit as st
import pandas as pd
import numpy as np
import pickle
import plotly.express as px
from PIL import Image

# Configuración de la página
st.set_page_config(page_title="Madrid Real Estate Analytics", layout="wide")

# Cargar el modelo
@st.cache_resource
def load_model():
    try:
        with open('modelo_entrenado.pkl', 'rb') as f:
            model = pickle.load(f)
        return model
    except Exception as e:
        st.error(f"Error al cargar el modelo: {e}")
        return None

xg_reg = load_model()

# Datos para las opciones (igual que en tu código original)
metros_cuadrados_opciones = list(range(20, 301, 10))
habitaciones_opciones = list(range(1, 6))
banos_opciones = list(range(1, 4))
planta_opciones = ["-2", "-1", "0", "0.5", "1", "2", "3", "4", "5", "6", "7", "8", "9", "99"]
distrito_opciones_dict = {
    1: "Centro", 2: "Arganzuela", 3: "Retiro", 4: "Salamanca", 5: "Chamartín",
    6: "Tetuán", 7: "Chamberí", 8: "Fuencarral-El Pardo", 9: "Moncloa-Aravaca",
    10: "Latina", 11: "Carabanchel", 12: "Usera", 13: "Puente de Vallecas",
    14: "Moratalaz", 15: "Ciudad Lineal", 16: "Hortaleza", 17: "Villaverde",
    18: "Villa de Vallecas", 19: "Vicálvaro", 20: "San Blas-Canillejas", 21: "Barajas"
}
tipo_casa_opciones = ["Pisos", "Dúplex", "Áticos", "Casa o chalet"]
boolean_opciones = ["No", "Sí"]

# Función de conversión booleana
def bool_to_int(val):
    return 1 if val == "Sí" else 0

# Página de Predicción
def prediction_page():
    st.title("Predicción de Precio de Vivienda en Madrid")
    
    # Organización en columnas
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Características Principales")
        metros_cuadrados = st.selectbox("Metros Cuadrados", metros_cuadrados_opciones)
        habitaciones = st.selectbox("Número de Habitaciones", habitaciones_opciones)
        banos = st.selectbox("Número de Baños", banos_opciones)
        planta = st.selectbox("Planta", planta_opciones)
        distrito_nombre = st.selectbox("Distrito", list(distrito_opciones_dict.values()))
        distrito_codigo = [k for k, v in distrito_opciones_dict.items() if v == distrito_nombre][0]
        tipo_casa = st.selectbox("Tipo de Casa", tipo_casa_opciones)
    
    with col2:
        st.subheader("Comodidades")
        calefaccion_individual = st.selectbox("Calefacción Individual", boolean_opciones)
        aire_acondicionado = st.selectbox("Aire Acondicionado", boolean_opciones)
        armarios_empotrados = st.selectbox("Armarios Empotrados", boolean_opciones)
        ascensor = st.selectbox("Ascensor", boolean_opciones)
        exterior = st.selectbox("Es Exterior", boolean_opciones)
        piso_bajo = st.selectbox("Piso Bajo", boolean_opciones)
    
    with st.expander("Otras Características", expanded=False):
        col3, col4 = st.columns(2)
        with col3:
            jardin = st.selectbox("Jardín", boolean_opciones)
            piscina = st.selectbox("Piscina", boolean_opciones)
            terraza = st.selectbox("Terraza", boolean_opciones)
            balcon = st.selectbox("Balcón", boolean_opciones)
        with col4:
            trastero = st.selectbox("Trastero", boolean_opciones)
            accesible = st.selectbox("Accesible", boolean_opciones)
            zonas_verdes = st.selectbox("Zonas Verdes", boolean_opciones)
            nuevo_desarrollo = st.selectbox("Nuevo Desarrollo", boolean_opciones)
            necesita_reforma = st.selectbox("Necesita Reforma", boolean_opciones)
    
    # Botón de predicción
    if st.button("Calcular Precio Estimado", type="primary"):
        # Preparar el vector de características en el ORDEN CORRECTO
        features = [
            metros_cuadrados,
            habitaciones,
            banos,
            float(planta),
            bool_to_int(aire_acondicionado),
            bool_to_int(armarios_empotrados),
            bool_to_int(ascensor),
            bool_to_int(exterior),
            bool_to_int(jardin),
            bool_to_int(piscina),
            bool_to_int(terraza),
            bool_to_int(balcon),
            bool_to_int(trastero),
            bool_to_int(accesible),
            bool_to_int(zonas_verdes),
            bool_to_int(nuevo_desarrollo),
            bool_to_int(necesita_reforma),
            bool_to_int(calefaccion_individual),
            1 if tipo_casa == "Pisos" else 0,
            1 if tipo_casa == "Dúplex" else 0,
            1 if tipo_casa == "Áticos" else 0,
            1 if tipo_casa == "Casa o chalet" else 0,
            distrito_codigo,
            bool_to_int(piso_bajo)
        ]
        
        # Convertir a array numpy
        input_data = np.array([features])
        
        # Realizar predicción
        try:
            prediccion = xg_reg.predict(input_data)
            precio_estimado = prediccion[0]
            
            # Mostrar resultados
            st.success(f"## Precio estimado: {precio_estimado:,.2f} €")
            
            # Mostrar detalles
            with st.expander("Detalles de la predicción"):
                st.metric("Precio por m²", f"{precio_estimado/metros_cuadrados:,.2f} €/m²")
                
                # Comparativa con distrito (datos historicos 2025)
                avg_price_m2 = {
                    "Centro": 6994,
                    "Arganzuela": 5776,
                    "Retiro": 7208,
                    "Salamanca": 9589,
                    "Chamartín": 7110,
                    "Tetuán": 5502,
                    "Chamberí": 7871,
                    "Fuencarral-El Pardo": 5106,
                    "Moncloa-Aravaca": 6413,
                    "Latina": 3388,
                    "Carabanchel": 3204,
                    "Usera": 3012,
                    "Puente de Vallecas": 2819,
                    "Moratalaz": 3748,
                    "Ciudad Lineal": 5015,
                    "Hortaleza": 4833,
                    "Villaverde": 2409,
                    "Villa de Vallecas": 2927,
                    "Vicálvaro": 3613,
                    "San Blas-Canillejas": 3445,
                    "Barajas": 4080
                }.get(distrito_nombre, 4000)
                
                st.write(f"Comparativa con {distrito_nombre}:")
                col_comp1, col_comp2 = st.columns(2)
                col_comp1.metric("Precio/m² estimado", f"{precio_estimado/metros_cuadrados:,.0f} €")
                col_comp2.metric(f"Media en {distrito_nombre}", f"{avg_price_m2:,.0f} €")
                
                # Gráfico de comparación
                fig = px.bar(
                    x=["Tu propiedad", f"Media {distrito_nombre}"],
                    y=[precio_estimado/metros_cuadrados, avg_price_m2],
                    labels={'x': '', 'y': 'Precio/m² (€)'},
                    title="Comparación con el mercado"
                )
                st.plotly_chart(fig, use_container_width=True)
                
        except Exception as e:
            st.error(f"Error al realizar la predicción: {e}")

# Página de EDA con tus datos
def eda_page():
    st.title("Análisis Exploratorio de Datos")
    
    # Cargar tus datos reales (ajusta esto)
    @st.cache_data
    def load_data():
        # Reemplaza esto con la carga de tus datos reales
        # Ejemplo: pd.read_csv('tus_datos.csv')
        return pd.DataFrame({
            'barrio': np.random.choice(list(distrito_opciones_dict.values()), 1000),
            'precio': np.random.normal(300000, 150000, 1000).clip(50000, 1000000),
            'metros_cuadrados': np.random.randint(30, 200, 1000),
            'habitaciones': np.random.choice([1,2,3,4,5], 1000),
            'tipo': np.random.choice(tipo_casa_opciones, 1000)
        })
    
    df = load_data()
    df['precio_m2'] = df['precio'] / df['metros_cuadrados']
    
    # Filtros
    st.sidebar.header("Filtros")
    barrios = st.sidebar.multiselect(
        "Barrios",
        options=df['barrio'].unique(),
        default=df['barrio'].unique()[:3]
    )
    
    rango_precio = st.sidebar.slider(
        "Rango de precio (€)",
        min_value=int(df['precio'].min()),
        max_value=int(df['precio'].max()),
        value=(int(df['precio'].quantile(0.25)), int(df['precio'].quantile(0.75)))
    )
    
    # Aplicar filtros
    df_filtrado = df[
        (df['barrio'].isin(barrios)) & 
        (df['precio'].between(*rango_precio))
    ]
    
    # Visualizaciones
    st.subheader("Distribución de Precios")
    tab1, tab2 = st.tabs(["Histograma", "Boxplot"])
    
    with tab1:
        fig = px.histogram(df_filtrado, x='precio', nbins=30)
        st.plotly_chart(fig, use_container_width=True)
    
    with tab2:
        fig = px.box(df_filtrado, x='barrio', y='precio')
        st.plotly_chart(fig, use_container_width=True)
    
    st.subheader("Relación Precio - Metros Cuadrados")
    fig = px.scatter(
        df_filtrado, 
        x='metros_cuadrados', 
        y='precio', 
        color='barrio',
        trendline="lowess"
    )
    st.plotly_chart(fig, use_container_width=True)

# Navegación
st.sidebar.title("Navegación")
pagina = st.sidebar.radio("Selecciona página:", ["Análisis de Datos", "Predicción"])

if pagina == "Análisis de Datos":
    if xg_reg:
        eda_page()
    else:
        st.error("Modelo no disponible. Contacta al administrador.")
else:
    prediction_page()