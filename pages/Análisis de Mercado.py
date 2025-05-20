
import streamlit as st
import pandas as pd
import numpy as np
import pickle
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# Configuración de la página
st.set_page_config(page_title="Madrid Real Estate Analytics", layout="wide")

# Cargar el modelo XGBoost
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

# Datos para las opciones
metros_cuadrados_opciones = list(range(20, 301, 10))
habitaciones_opciones = list(range(1, 6))
banos_opciones = list(range(1, 4))
planta_opciones = ["-2", "-1", "0", "0.5", "1", "2", "3", "4", "5", "6", "7", "8", "9", "99"]
distrito_opciones_dict = {
    1: "Centro",
    2: "Arganzuela",
    3: "Retiro",
    4: "Salamanca",
    5: "Chamartín",
    6: "Tetuán",
    7: "Chamberí",
    8: "Fuencarral-El Pardo",
    9: "Moncloa-Aravaca",
    10: "Latina",
    11: "Carabanchel",
    12: "Usera",
    13: "Puente de Vallecas",
    14: "Moratalaz",
    15: "Ciudad Lineal",
    16: "Hortaleza",
    17: "Villaverde",
    18: "Villa de Vallecas",
    19: "Vicálvaro",
    20: "San Blas-Canillejas",
    21: "Barajas"
}
tipo_casa_opciones = ["Pisos", "Dúplex", "Áticos", "Casa o chalet"]
boolean_opciones = ["No", "Sí"]

# Función para convertir Sí/No a 1/0
def bool_to_int(val):
    return 1 if val == "Sí" else 0

# Página de Predicción
def prediction_page():
    st.title("🔮 Predicción del Precio de Vivienda en Madrid")
    st.markdown("""
    Completa las características de la vivienda para obtener una estimación de precio basada en nuestro modelo predictivo.
    """)
    
    with st.expander("📋 Formulario de Características", expanded=True):
        col1, col2 = st.columns(2)
        
        with col1:
            metros_cuadrados = st.selectbox("Metros Cuadrados", metros_cuadrados_opciones)
            habitaciones = st.selectbox("Número de Habitaciones", habitaciones_opciones)
            banos = st.selectbox("Número de Baños", banos_opciones)
            planta = st.selectbox("Planta", planta_opciones)
            distrito_nombre = st.selectbox("Distrito", list(distrito_opciones_dict.values()))
            distrito_codigo = [k for k, v in distrito_opciones_dict.items() if v == distrito_nombre][0]
            tipo_casa = st.selectbox("Tipo de Casa", tipo_casa_opciones)
            
        with col2:
            calefaccion_individual = st.selectbox("Calefacción Individual", boolean_opciones)
            aire_acondicionado = st.selectbox("Aire Acondicionado", boolean_opciones)
            armarios_empotrados = st.selectbox("Armarios Empotrados", boolean_opciones)
            jardin = st.selectbox("Jardín", boolean_opciones)
            piscina = st.selectbox("Piscina", boolean_opciones)
            terraza = st.selectbox("Terraza", boolean_opciones)
            balcon = st.selectbox("Balcón", boolean_opciones)
    
    with st.expander("⚙️ Características Adicionales", expanded=False):
        col3, col4 = st.columns(2)
        
        with col3:
            trastero = st.selectbox("Trastero", boolean_opciones)
            accesible = st.selectbox("Accesible", boolean_opciones)
            zonas_verdes = st.selectbox("Zonas Verdes", boolean_opciones)
            
        with col4:
            ascensor = st.selectbox("Ascensor", boolean_opciones)
            exterior = st.selectbox("Es Exterior", boolean_opciones)
            piso_bajo = st.selectbox("Piso Bajo", boolean_opciones)
            nuevo_desarrollo = st.selectbox("Nuevo Desarrollo", boolean_opciones)
            necesita_reforma = st.selectbox("Necesita Reforma", boolean_opciones)
    
    if st.button("🏠 Calcular Precio Estimado", use_container_width=True):
        # Crear el vector de características
        caracteristicas = [
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
            tipo_casa_opciones.index(tipo_casa) == 0,  # Pisos
            tipo_casa_opciones.index(tipo_casa) == 1,  # Dúplex
            tipo_casa_opciones.index(tipo_casa) == 2,  # Áticos
            tipo_casa_opciones.index(tipo_casa) == 3,  # Casa o chalet
            distrito_codigo,
            bool_to_int(piso_bajo)
        ]
        
        # Realizar la predicción
        input_data = np.array([caracteristicas])
        prediccion = xg_reg.predict(input_data)
        
        # Mostrar resultado
        st.success(f"""
        ## Precio estimado: {prediccion[0]:,.0f} €
        - Precio por m²: {prediccion[0]/metros_cuadrados:,.0f} €/m²
        """)
        
        # Mostrar comparativa con el distrito
        st.markdown("---")
        st.subheader("📊 Comparativa con el Mercado")
        
        # Datos históricos 2025)
        
        avg_price_district = {
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
        comparison = pd.DataFrame({
            'Métrica': ['Precio Total', 'Precio por m²'],
            'Tu Vivienda': [prediccion[0], prediccion[0]/metros_cuadrados],
            f'Media en {distrito_nombre}': [
                avg_price_district * metros_cuadrados,
                avg_price_district
            ]
        })
        
        st.dataframe(comparison.style.format({
            'Tu Vivienda': '{:,.0f} €',
            f'Media en {distrito_nombre}': '{:,.0f} €'
        }))

# Página de EDA
def eda_page():
    st.title("📊 Análisis Exploratorio del Mercado Inmobiliario")
    st.markdown("""
    Explora las tendencias y patrones del mercado inmobiliario de Madrid a través de visualizaciones interactivas.
    """)
    
    # Cargar datos simulados
    @st.cache_data
    def load_eda_data():
        # Generar datos simulados basados en los distritos y características disponibles
        np.random.seed(42)
        n = 500
        data = {
            'barrio': np.random.choice(list(distrito_opciones_dict.values()), n),
            'precio': np.random.normal(300000, 150000, n).clip(80000, 1000000),
            'metros_cuadrados': np.random.randint(50, 200, n),
            'habitaciones': np.random.choice(habitaciones_opciones, n),
            'baños': np.random.choice(banos_opciones, n),
            'tipo': np.random.choice(tipo_casa_opciones, n),
            'ascensor': np.random.choice(boolean_opciones, n, p=[0.3, 0.7]),
            'terraza': np.random.choice(boolean_opciones, n, p=[0.5, 0.5]),
            'parking': np.random.choice(boolean_opciones, n, p=[0.6, 0.4])
        }
        df = pd.DataFrame(data)
        df['precio_m2'] = df['precio'] / df['metros_cuadrados']
        return df
    
    df = load_eda_data()
    
    # Filtros
    st.sidebar.header("🔍 Filtros de Análisis")
    barrios_seleccionados = st.sidebar.multiselect(
        "Barrios:",
        options=df['barrio'].unique(),
        default=df['barrio'].unique()[:3]
    )
    
    rango_precios = st.sidebar.slider(
        "Rango de precios (€):",
        min_value=int(df['precio'].min()),
        max_value=int(df['precio'].max()),
        value=(int(df['precio'].quantile(0.25)), int(df['precio'].quantile(0.75)))
    )
    
    # Aplicar filtros
    df_filtrado = df[
        (df['barrio'].isin(barrios_seleccionados)) &
        (df['precio'].between(rango_precios[0], rango_precios[1]))
    ]
    
    # Métricas clave
    st.subheader("📌 Resumen del Mercado")
    col1, col2, col3 = st.columns(3)
    col1.metric("Propiedades", len(df_filtrado))
    col2.metric("Precio promedio", f"{df_filtrado['precio'].mean():,.0f} €")
    col3.metric("Precio/m² promedio", f"{df_filtrado['precio_m2'].mean():,.0f} €")
    
    # Visualizaciones
    st.markdown("---")
    st.subheader("📈 Visualizaciones Interactivas")
    
    tab1, tab2, tab3 = st.tabs(["Distribuciones", "Comparativas", "Relaciones"])
    
    with tab1:
        fig = make_subplots(rows=1, cols=2, subplot_titles=("Distribución de Precios", "Precio por m² por Barrio"))
        
        fig.add_trace(
            go.Histogram(x=df_filtrado['precio'], nbinsx=20, name="Precios"),
            row=1, col=1
        )
        
        fig.add_trace(
            go.Box(x=df_filtrado['barrio'], y=df_filtrado['precio_m2'], name="Precio/m²"),
            row=1, col=2
        )
        
        fig.update_layout(height=500, showlegend=False)
        st.plotly_chart(fig, use_container_width=True)
    
    with tab2:
        fig = px.bar(
            df_filtrado.groupby(['barrio', 'tipo'])['precio'].mean().reset_index(),
            x='barrio', y='precio', color='tipo',
            title='Precio Promedio por Barrio y Tipo',
            barmode='group'
        )
        st.plotly_chart(fig, use_container_width=True)
        
        fig = px.sunburst(
            df_filtrado.groupby(['barrio', 'tipo', 'ascensor']).size().reset_index(name='count'),
            path=['barrio', 'tipo', 'ascensor'], values='count',
            title='Distribución de Características'
        )
        st.plotly_chart(fig, use_container_width=True)
    
    with tab3:
        fig = px.scatter(
            df_filtrado, x='metros_cuadrados', y='precio',
            color='barrio', size='habitaciones',
            hover_data=['tipo', 'baños', 'ascensor'],
            title='Relación entre Metros Cuadrados y Precio'
        )
        st.plotly_chart(fig, use_container_width=True)
        
        fig = px.density_heatmap(
            df_filtrado, x='habitaciones', y='precio_m2',
            nbinsx=5, marginal_x="histogram", marginal_y="histogram",
            title='Densidad: Habitaciones vs Precio/m²'
        )
        st.plotly_chart(fig, use_container_width=True)

# Navegación entre páginas
st.sidebar.title("Navegación")
page = st.sidebar.radio("Selecciona una página:", ["📈 Análisis de Mercado", "🔮 Predictor de Precios"])

if page == "📈 Análisis de Mercado":
    eda_page()
else:
    if xg_reg:
        prediction_page()
    else:
        st.error("El modelo predictivo no está disponible. Por favor, contacta al administrador.")