import streamlit as st
import pandas as pd
import numpy as np
import pickle
import json
from streamlit_lottie import st_lottie
import pydeck as pdk  # Importar PyDeck

# ----------------------------- CONFIGURACIÓN --------------------------------

st.set_page_config(page_title="Predicción de Vivienda", layout="wide")

# CSS para reducir espacios
st.markdown("""
    <style>
        .block-container {padding-top: 1rem; padding-bottom: 1rem;}
        .stButton>button {width: 100%;}
    </style>
""", unsafe_allow_html=True)

# Inicializar historial en session_state
if 'historial' not in st.session_state:
    st.session_state.historial = []

# ----------------------------- CARGA DEL MODELO -----------------------------

@st.cache_resource
def load_xgboost_model(path):
    try:
        with open(path, 'rb') as f:
            return pickle.load(f)
    except Exception as e:
        st.error(f"Error al cargar el modelo: {e}")
        return None

xg_reg = load_xgboost_model("modelo_entrenado.pkl")
if xg_reg is None:
    st.stop()

# ----------------------------- ANIMACIÓN LOTTIE -----------------------------

def load_lottiefile(filepath: str):
    try:
        with open(filepath, "r") as f:
            return json.load(f)
    except Exception as e:
        st.warning(f"No se pudo cargar la animación: {e}")
        return None

lottie_house = load_lottiefile("house_animation.json")

# ----------------------------- INTERFAZ -------------------------------------

c1, c2 = st.columns([1, 3])
with c1:
    if lottie_house:
        st_lottie(lottie_house, width=150, height=150, quality="low")
with c2:
    st.title("Predicción de Precio de Vivienda - Madrid")
    st.markdown("Completa los datos del inmueble para estimar su valor.")

# ----------------------------- SELECTORES -----------------------------------

metros_cuadrados_opciones = list(range(20, 301, 10))
habitaciones_opciones = list(range(1, 6))
banos_opciones = list(range(1, 4))
planta_opciones = ["-2", "-1", "0", "0.5", "1", "2", "3", "4", "5", "6", "7", "8", "9", "99"]
tipo_casa_opciones = ["Pisos", "Dúplex", "Áticos", "Casa o chalet"]
boolean_opciones = ["No", "Sí"]
distrito_opciones_dict = {
    1: "Centro", 2: "Arganzuela", 3: "Retiro", 4: "Salamanca", 5: "Chamartín", 6: "Tetuán",
    7: "Chamberí", 8: "Fuencarral-El Pardo", 9: "Moncloa-Aravaca", 10: "Latina",
    11: "Carabanchel", 12: "Usera", 13: "Puente de Vallecas", 14: "Moratalaz",
    15: "Ciudad Lineal", 16: "Hortaleza", 17: "Villaverde", 18: "Villa de Vallecas",
    19: "Vicálvaro", 20: "San Blas-Canillejas", 21: "Barajas"
}

# Mapeo de tipo de casa a one-hot encoding
tipo_casa_mapping = {
    "Pisos": [1, 0, 0, 0],
    "Dúplex": [0, 1, 0, 0],
    "Áticos": [0, 0, 1, 0],
    "Casa o chalet": [0, 0, 0, 1]
}

# ----------------------------- FORMULARIO COMPACTO --------------------------

col1, col2 = st.columns(2)
with col1:
    metros_cuadrados = st.selectbox("Metros Cuadrados", metros_cuadrados_opciones)
    habitaciones = st.selectbox("Habitaciones", habitaciones_opciones)
    banos = st.selectbox("Baños", banos_opciones)
    planta = st.selectbox("Planta", planta_opciones)
    tipo_casa = st.selectbox("Tipo de Vivienda", tipo_casa_opciones)
    distrito_nombre = st.selectbox("Distrito", list(distrito_opciones_dict.values()))

with col2:
    calefaccion_individual = st.selectbox("Calefacción Individual", boolean_opciones)
    aire_acondicionado = st.selectbox("Aire Acondicionado", boolean_opciones)
    armarios_empotrados = st.selectbox("Armarios Empotrados", boolean_opciones)
    jardin = st.selectbox("Jardín", boolean_opciones)
    piscina = st.selectbox("Piscina", boolean_opciones)
    terraza = st.selectbox("Terraza", boolean_opciones)

# Campos adicionales opcionales
with st.expander("Más opciones"):
    balcon = st.selectbox("Balcón", boolean_opciones)
    trastero = st.selectbox("Trastero", boolean_opciones)
    accesible = st.selectbox("Accesible", boolean_opciones)
    zonas_verdes = st.selectbox("Zonas Verdes", boolean_opciones)
    ascensor = st.selectbox("Ascensor", boolean_opciones)
    exterior = st.selectbox("Es Exterior", boolean_opciones)
    piso_bajo = st.selectbox("Piso Bajo", boolean_opciones)
    nuevo_desarrollo = st.selectbox("Nuevo Desarrollo", boolean_opciones)
    necesita_reforma = st.selectbox("Necesita Reforma", boolean_opciones)

# ----------------------------- PREDICCIÓN -----------------------------------

def bool_to_int(val):
    return 1 if val == "Sí" else 0

def validate_inputs():
    if metros_cuadrados <= 0:
        st.error("Los metros cuadrados deben ser positivos")
        return False
    if habitaciones <= 0:
        st.error("El número de habitaciones debe ser positivo")
        return False
    return True

if st.button("Predecir Precio"):
    if not validate_inputs():
        st.stop()
    
    try:
        planta_num = float(planta)
        distrito_codigo = [k for k, v in distrito_opciones_dict.items() if v == distrito_nombre][0]
        
        # Obtener one-hot encoding para el tipo de casa
        tipo_casa_encoded = tipo_casa_mapping.get(tipo_casa, [0, 0, 0, 0])
        
        caracteristicas = [
            metros_cuadrados,
            habitaciones,
            banos,
            planta_num,
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
            *tipo_casa_encoded,  # Desempaquetar el one-hot encoding
            distrito_codigo,
            bool_to_int(piso_bajo)
        ]

        input_data = np.array([caracteristicas])
        
        with st.spinner("Calculando precio estimado..."):
            prediccion = xg_reg.predict(input_data)
            precio_est = round(prediccion[0], 2)
            
            st.success(f"💰 Precio estimado: **{precio_est:,.2f} €**")
            
            # Guardar en el historial
            st.session_state.historial.append({
                "m²": metros_cuadrados,
                "Hab.": habitaciones,
                "Baños": banos,
                "Distrito": distrito_nombre,
                "Tipo": tipo_casa,
                "Precio (€)": precio_est
            })
            
    except Exception as e:
        st.error(f"Error al realizar la predicción: {e}")

# Mostrar el mapa siempre y actualizarlo basado en la selección
st.subheader("🗺️ Ubicación Aproximada del Distrito")

distrito_coords = {
    'Centro': (40.4168, -3.7038),
    'Arganzuela': (40.405, -3.705),
    'Retiro': (40.414, -3.68),
    'Salamanca': (40.4297, -3.6774),
    'Chamartín': (40.45, -3.68),
    'Tetuán': (40.46, -3.70),
    'Chamberí': (40.435, -3.703),
    'Fuencarral-El Pardo': (40.50, -3.72),
    'Moncloa-Aravaca': (40.45, -3.75),
    'Latina': (40.40, -3.75),
    'Carabanchel': (40.38, -3.73),
    'Usera': (40.37, -3.70),
    'Puente de Vallecas': (40.38, -3.67),
    'Moratalaz': (40.40, -3.65),
    'Ciudad Lineal': (40.43, -3.65),
    'Hortaleza': (40.47, -3.63),
    'Villaverde': (40.35, -3.68),
    'Villa de Vallecas': (40.37, -3.62),
    'Vicálvaro': (40.39, -3.58),
    'San Blas-Canillejas': (40.43, -3.62),
    'Barajas': (40.476, -3.577)
}

if distrito_nombre in distrito_coords:
    lat, lon = distrito_coords[distrito_nombre]
    st.pydeck_chart(pdk.Deck(
        map_style='mapbox://styles/mapbox/light-v9',
        initial_view_state=pdk.ViewState(
            latitude=lat,
            longitude=lon,
            zoom=12,
            pitch=50,
        ),
        layers=[
            pdk.Layer(
                'ScatterplotLayer',
                data=[{"position": [lon, lat]}],
                get_position='position',
                get_color='[255, 0, 0, 160]',
                get_radius=300,
            ),
        ],
    ))
else:
    st.info("Coordenadas no disponibles para este distrito.")

# ------------------- Historial -------------------
if 'historial' not in st.session_state:
    st.session_state['historial'] = []

if st.sidebar.button('Guardar esta predicción') and 'precio_est' in locals(): #Verifico si existe la variable
    st.session_state['historial'].append({
        'zona': distrito_nombre,
        'precio': precio_est
    })

if st.session_state['historial']:
    st.subheader("🕘 Historial de Predicciones")
    df_hist = pd.DataFrame(st.session_state['historial'])
    st.table(df_hist)

    # Botón para limpiar historial
    if st.sidebar.button("🧹 Limpiar historial"):
        st.session_state.historial = []
        st.rerun()

    # Botón de descarga
    csv = df_hist.to_csv(index=False).encode('utf-8')
    st.sidebar.download_button(
        label="📥 Descargar historial como CSV",
        data=csv,
        file_name='predicciones_vivienda.csv',
        mime='text/csv'
    )
    
