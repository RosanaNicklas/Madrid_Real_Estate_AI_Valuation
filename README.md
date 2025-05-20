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


Ejecutar la aplicación
bash
streamlit run main_app.py
La aplicación estará disponible en: http://localhost:8501

🖼️ Galería de la Aplicación


### Pantalla de inicio de sesión
![Dashboard Principal	Vista general del mercado madrileño	Dashboard](screen/dashboard.png)

### Proyecto
![Objetivo del proyecto](screen/proyecto.png)

### Análisis de Datos
![Análisis de Datos Distribuciones estadísticas y precios por m²](screen/analisis1.png)

### Análisis de Datos
![Análisis de Datos Distribuciones estadísticas y precios por m²](screen/analisis2.png)

### Análisis de Mercado
![Análisis de Datos Distribuciones estadísticas del mercado madrileño](screen/analisismercado1.png)


### Análisis de Mercado
![Análisis de Datos Distribuciones estadísticas del mercado madrileño](screen/analisismercado2.png)

### Predicción
![Predicción	Modelo de valoración automática	Predicción](screen/prediccion1.png)

### Mapa
![Mapa Interactivo	Visualización geográfica por distritos](screen/prediccion2.png)
### Proyecto
![Objetivo del proyecto](screen/proyecto.png)

### Sobre la app
![Información y contacto](screen/app.png)



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
├── models/                 # Modelos entrenados
└── requirements.txt        # Dependencias

✉️ Contacto

Rosana Longares

📧 rosana8longares@gmail.com

LinkedIn https://www.linkedin.com/in/rosanalongares/
GitHub  https://github.com/RosanaNicklas
