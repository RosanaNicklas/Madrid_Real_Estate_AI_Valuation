import streamlit as st
import pickle
from xgboost import XGBRegressor
from PIL import Image
import base64
import pandas as pd

# -------------------------------- MINIMALIST CONFIGURATION -------------------------------
st.set_page_config(
    page_title="Housing Price Prediction | Data Science",
    page_icon="🏠",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Cargar datos
@st.cache_resource
def load_model():
    try:
        with open('modelo_entrenado.pkl', 'rb') as f:
            model = pickle.load(f)
        with open("columns_order.pkl", "rb") as f:
            columnas_ordenadas = pickle.load(f)
        return model, columnas_ordenadas
    except Exception as e:
        st.error(f"Error al cargar el modelo: {e}")
        return None, None

model, columnas_ordenadas = load_model()

# Enhanced minimalist styles
st.markdown("""
    <style>
        .main {padding-top: 1.5rem; padding-bottom: 2rem;}
        h1 {color: #2e4765; text-align: center; font-weight: 600;}
        h2 {color: #3a5a78; font-weight: 500;}
        .stMarkdown {text-align: center;}
        .stImage {margin: 0 auto; display: flex; justify-content: center;}
        .block-container {padding-top: 1rem; max-width: 800px;}
        .footer {position: fixed; bottom: 0; width: 100%; text-align: center; 
                padding: 0.5rem; background: white; border-top: 1px solid #eee;}
        .feature-box {border: 1px solid #e1e4e8; border-radius: 8px; 
                     padding: 1.5rem; margin-bottom: 1.5rem;}
        hr {margin: 2rem 0; border: 0; height: 1px; 
            background-image: linear-gradient(to right, rgba(0,0,0,0), rgba(0,0,0,0.75), rgba(0,0,0,0));}
    </style>
""", unsafe_allow_html=True)

# -------------------------------- CENTERED MAIN IMAGE ----------------------------
@st.cache_data
def load_image(path):
    return Image.open(path)

try:
    imagen_principal = load_image("Madrid_castizo.png")  # Replace with your file
    st.image(imagen_principal, use_container_width=True)  # Updated parameter here
except FileNotFoundError:
    st.warning("Main image not found. Displaying placeholder.")
    # You can add an alternative placeholder image here

# -------------------------------- IMPROVED TITLE SECTION -------------------------------
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@800&family=Manrope:wght@300&display=swap');
.creative-title {
    font-family: 'Plus Jakarta Sans', sans-serif;
    font-size: 3.2rem;
    font-weight: 800;
    text-align: center;
    background: linear-gradient(90deg, #1E40AF, #9333EA);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    margin-bottom: 0.5rem;
    line-height: 1.1;
}
.creative-subtitle {
    font-family: 'Manrope', sans-serif;
    font-size: 1.2rem;
    text-align: center;
    color: #4B5563;
    margin-top: 0;
    max-width: 600px;
    margin: 0 auto;
}
.creative-highlight {
    background: rgba(147, 51, 234, 0.1);
    padding: 0.2rem 0.5rem;
    border-radius: 4px;
}
</style>

<div style="padding: 3rem 0 4rem;">
    <h1 class="creative-title">Madrid Real Estate<br>AI Valuation</h1>
    <p class="creative-subtitle">Plataforma de <span class="creative-highlight">análisis predictivo</span> para inversores y profesionales del sector</p>
</div>
""", unsafe_allow_html=True)
# -------------------------------- MINIMALIST FOOTER --------------------------------
# -------------------------------- ELEGANT FOOTER --------------------------------
st.markdown("""
    <style>
        .footer {
            position: fixed;
            bottom: 0;
            left: 0;
            right: 0;
            background: #1E293B;
            color: white;
            padding: 1rem;
            text-align: center;
            font-family: 'Montserrat', sans-serif;
            box-shadow: 0 -2px 10px rgba(0,0,0,0.1);
            z-index: 1000;
        }
        .footer-content {
            max-width: 1200px;
            margin: 0 auto;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }
        .footer-links {
            display: flex;
            gap: 1.5rem;
        }
        .footer a {
            color: #3a5a78;
            text-decoration: none;
            transition: all 0.3s ease;
            font-weight: 500;
        }
        .footer a:hover {
            color: #3a5a78;
            text-decoration: underline;
        }
        .footer-divider {
            margin: 0 0.5rem;
            color: #3a5a78;
        }
        .footer-credits {
            font-size: 0.9rem;
        }
        @media (max-width: 768px) {
            .footer-content {
                flex-direction: column;
                gap: 0.5rem;
            }
            .footer-links {
                flex-wrap: wrap;
                justify-content: center;
            }
        }
    </style>
""", unsafe_allow_html=True)

footer = """
<div class='footer'>
    <div class='footer-content'>
        <div class='footer-credits'>
            © 2023 Rosana Longares | Proyecto Final de Máster en Data Science con Nodd3r
        </div>
        <div class='footer-links'>
            <a href="https://github.com/RosanaNicklas/Madrid_Real_Estate_AI_Valuation" target="_blank">
                <i class="fab fa-github"></i> Código Fuente
            <a 
            <span class='footer-divider'>|</span>
            <a href="https://www.linkedin.com/in/rosanalongares/" target="_blank">
                <i class="fab fa-linkedin"></i> Contacto
            </a>
        </div>
    </div>
</div>

<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.3/css/all.min.css">
<link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@400;500;600&display=swap" rel="stylesheet">
"""

st.markdown(footer, unsafe_allow_html=True)


