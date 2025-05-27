# 🏠 Dashboard Analítico de Mercado Inmobiliario de Madrid

![Banner del proyecto](Madrid_castizo.png)  
*Proyecto de Fin de Máster en Data Science - Análisis predictivo del mercado inmobiliario madrileño*

---

## 🌟 Características Principales

### 1. 🖥️ Pantalla Principal
<div align="center">
  <img src="assets/dashboard.png" alt="Interfaz principal" width="80%">
</div>

### 2. 📊 Análisis Exploratorio (EDA)
<div align="center">
  <img src="assets/analisis1.png" alt="Análisis estadístico 1" width="45%">
  <img src="assets/analisis2.png" alt="Análisis estadístico 2" width="45%">
</div>

### 3. 🗺 Mapa Interactivo
<div align="center">
  <img src="assets/prediccion2.png" alt="Mapa de distritos" width="80%">
</div>

### 4. 📈 Tendencias de Mercado
<div align="center">
  <img src="assets/analisismercado1.png" alt="Evolución temporal 1" width="45%">
  <img src="assets/analisismercado2.png" alt="Evolución temporal 2" width="45%">
</div>

### 5. 🤖 Módulo de Predicción
<div align="center">
  <img src="assets/prediccion1.png" alt="Formulario de predicción" width="45%">
  <img src="assets/prediccion2.png" alt="Resultados del modelo" width="45%">
</div>


### 5. 🤖 Objetivo y sobre la app
<div align="center">
  <img src="assets/proyecto.png" alt="Formulario de predicción" width="45%">
  <img src="assets/app.png" alt="Resultados del modelo" width="45%">
</div>

---

## 🛠 Tecnologías Utilizadas

<div align="center">

| Categoría       | Tecnologías                                                                 |
|-----------------|-----------------------------------------------------------------------------|
| Frontend        | ![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?logo=streamlit)  |
| Backend         | ![Python](https://img.shields.io/badge/Python-3.9+-3776AB?logo=python)      |
| Visualización   | ![Plotly](https://img.shields.io/badge/Plotly-3F4F75?logo=plotly) ![Matplotlib](https://img.shields.io/badge/Matplotlib-11557C?logo=matplotlib) |
| Machine Learning| ![XGBoost](https://img.shields.io/badge/XGBoost-017CEE?logo=xgboost) ![Scikit-learn](https://img.shields.io/badge/scikit--learn-F7931E?logo=scikit-learn) |

</div>

---

## ⚙️ Estructura del Proyecto

```python
# Modelo Predictivo (XGBoost)
from xgboost import XGBRegressor
from sklearn.metrics import r2_score

model = XGBRegressor(objective='reg:squarederror')
model.fit(X_train, y_train)

# Precisión del 94.7%
predictions = model.predict(X_test)
score = r2_score(y_test, predictions)

# Clonar repositorio
git clone https://github.com/RosanaNicklas/Madrid_Real_Estate_AI_Valuation.git

# Instalar dependencias
pip install -r requirements.txt

# Ejecutar aplicación
streamlit run main_app.py

📌 Detalles Técnicos
Dataset:
✔ 21,742 propiedades (2022-2023)
✔ 15 características principales
✔ Limpieza automatizada de datos

Rendimiento del Modelo:
✅ R²: 94.7%
✅ MAE: €12,450
✅ Actualizado mensualmente

📬 Contacto

Rosana Longares

📧 rosana8longares@gmail.com

LinkedIn https://www.linkedin.com/in/rosanalongares/
GitHub  https://github.com/RosanaNicklas
