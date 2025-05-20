# 🏠 Madrid Real Estate Analytics Dashboard

![Dashboard Preview](assets/Madrid_castizo.png)  
*Dashboard interactivo del mercado inmobiliario de Madrid*

## 📌 Descripción

Aplicación Streamlit para análisis avanzado del mercado inmobiliario madrileño que incluye:
- 📊 Visualización interactiva de distribuciones de precios
- 📈 Evolución temporal de valores
- 🗺️ Comparativa geográfica entre distritos
- 📐 Relación precio/metros cuadrados
- 🔍 Modelo predictivo de valoración automática

## 🛠 Stack Tecnológico

| Categoría       | Tecnologías                                                                 |
|-----------------|-----------------------------------------------------------------------------|
| Frontend        | ![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?logo=streamlit)  |
| Backend         | ![Python](https://img.shields.io/badge/Python-3.9+-3776AB?logo=python)      |
| Procesamiento   | ![Pandas](https://img.shields.io/badge/Pandas-150458?logo=pandas) ![NumPy](https://img.shields.io/badge/NumPy-013243?logo=numpy) |
| Visualización   | ![Plotly](https://img.shields.io/badge/Plotly-3F4F75?logo=plotly) ![Matplotlib](https://img.shields.io/badge/Matplotlib-11557C?logo=matplotlib) |
| Machine Learning| ![Scikit-learn](https://img.shields.io/badge/scikit--learn-F7931E?logo=scikit-learn) |

## 🚀 Instalación y Ejecución

### Requisitos previos
```bash
# Clonar repositorio
git clone https://github.com/RosanaNicklas/Madrid_Real_Estate_AI_Valuation.git
cd Madrid_Real_Estate_AI_Valuation

# Crear entorno virtual (opcional pero recomendado)
python -m venv venv
source venv/bin/activate  # Linux/Mac
.\venv\Scripts\activate  # Windows

# Instalar dependencias
pip install -r requirements.txt
# Ejecutar la app
streamlit run main_app.py
La aplicación estará disponible en: http://localhost:8501




#### 1. Dashboard Principal
![Dashboard Completo](assets/screenshots/01-dashboard.png)
*Vista general con:*
- Precio medio por distrito
- Evolución temporal
- Filtros interactivos

#### 2. Módulo de Predicción
![Predicción de Valores](assets/screenshots/03-prediccion.png)
*Características:*
- Formulario de entrada de datos
- Resultados con intervalo de confianza
- Explicación de variables clave

#### 3. Objetivo del Modelo
![Explicación Técnica](assets/screenshots/04-objetivo.png)
*Incluye:*
- Arquitectura del modelo
- Métricas de rendimiento
- Limitaciones conocidas

#### 4. Sobre Esta App
![Información](assets/screenshots/05-sobre-app.png)
*Contiene:*
- Stack tecnológico completo
- Enlaces a documentación
- Datos de contacto

Conecta tu cuenta GitHub

Selecciona este repositorio

Especifica main_app.py como archivo principal

Configura las variables de entorno si es necesario

📊 Estructura del Proyecto
Madrid_Real_Estate_AI_Valuation/
├── main_app.py              # Aplicación principal
├── pages/
│   ├── 1_📊_Análisis_de_Datos.py
│   ├── 2_📈_Análisis_de_Mercado.py
│   ├── 3_🔮_Predicción.py
│   └── 4_ℹ️_Sobre_la_App.py
├── assets/
│   ├── screenshots/         # Capturas de pantalla
│   └── Madrid_castizo.png   # Imágenes estáticas
├── data/                   # Datasets
└── requirements.txt        # Dependencias


## ✉️ Contacto


**Rosana Longares**  
📧 rosana8longares@gmail.com  

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Rosana_Longares-0077B5?style=for-the-badge&logo=linkedin)](https://www.linkedin.com/in/rosanalongares)  
[![GitHub](https://img.shields.io/badge/GitHub-RosanaNicklas-181717?style=for-the-badge&logo=github)](https://github.com/RosanaNicklas)
