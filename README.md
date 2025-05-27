# 🏠 Madrid Real Estate Analytics Dashboard

![Dashboard Preview](Madrid_castizo.png)  
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

                  

# 🖼️ Galería de la Aplicación

## 📚 Tabla de contenidos

- [🚪 Pantallas principales](#-pantallas-principales)
  - [🔐 Inicio de sesión](#-inicio-de-sesión)
  - [🏠 Dashboard principal](#-dashboard-principal)
- [📊 Análisis de datos](#-análisis-de-datos)
  - [📈 Distribuciones estadísticas](#-distribuciones-estadísticas)
  - [💶 Precios por m²](#-precios-por-m²)
- [🏘️ Análisis de mercado](#-análisis-de-mercado)
  - [📊 Estadísticas del mercado 1](#-estadísticas-del-mercado-1)
  - [📊 Estadísticas del mercado 2](#-estadísticas-del-mercado-2)
- [🧠 Funcionalidades avanzadas](#-funcionalidades-avanzadas)
  - [🤖 Modelo de predicción](#-modelo-de-predicción)
  - [🗺️ Mapa interactivo](#-mapa-interactivo)
- [ℹ️ Información](#️-información)
  - [📱 Sobre la app](#-sobre-la-app)

---

## 🚪 Pantallas principales

### 🔐 Inicio de sesión
![Dashboard](assets/dashboard.png)

### 🏠 Dashboard principal
![Vista general del mercado madrileño](assets/proyecto.png)

---


## 📊 Análisis de datos

### 📈 Distribuciones estadísticas
![Análisis de datos 1](assets/analisis1.png)

### 💶 Precios por m²
![Análisis de datos 2](assets/analisis2.png)



## 🏘️ Análisis de mercado

### 📊 Estadísticas del mercado 1
![Análisis de mercado 1](assets/analisismercado1.png)

### 📊 Estadísticas del mercado 2
![Análisis de mercado 2](assets/analisismercado2.png)



## 🧠 Funcionalidades avanzadas

### 🤖 Modelo de predicción
![Pantalla de predicción](assets/prediccion1.png)

### 🗺️ Mapa interactivo
![Visualización geográfica](assets/prediccion2.png)
## 🚪 Pantallas principales



| Pantalla            | Vista                                                                 |
|---------------------|-----------------------------------------------------------------------|
| 🔐 Inicio de sesión  | <img src="assets/dashboard.png" alt="Dashboard" width="300"/>        |
| 🏠 Dashboard principal | <img src="assets/proyecto.png" alt="Vista general del mercado madrileño" width="300"/> |

## 📊 Análisis de datos

| Pantalla                    | Vista                                                      |
|-----------------------------|------------------------------------------------------------|
| 📈 Distribuciones estadísticas | <img src="assets/analisis1.png" alt="Análisis de datos 1" width="300"/>          |
| 💶 Precios por m²            | <img src="assets/analisis2.png" alt="Análisis de datos 2" width="300"/>             |

## 🏘️ Análisis de mercado

| Pantalla                        | Vista                                                        |
|---------------------------------|--------------------------------------------------------------|
| 📊 Estadísticas del mercado 1   | <img src="assets/analisismercado1.png" alt="Análisis de mercado 1" width="300"/>        |
| 📊 Estadísticas del mercado 2   | <img src="assets/analisismercado2.png" alt="Análisis de mercado 2" width="300"/>        |

## 🧠 Funcionalidades avanzadas

| Funcionalidad               | Vista                                                           |
|-----------------------------|-----------------------------------------------------------------|
| 🤖 Modelo de predicción     | <img src="assets/prediccion1.png" alt="Pantalla de predicción" width="300"/>              |
| 🗺️ Mapa interactivo         | <img src="assets/prediccion2.png" alt="Visualización geográfica" width="300"/>            |

## ℹ️ Información

| Sección            | Vista                                                           |
|--------------------|-----------------------------------------------------------------|
| 📱 Sobre la app     | <img src="assets/app.png" alt="Información y contacto" width="300"/>                      |






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
