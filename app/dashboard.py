import streamlit as st
import pandas as pd
import joblib
import numpy as np
import os

st.title("SmartBike TimeAdvisor – Forudsig cykeludlejning")

st.markdown("Forudsig hvor mange cykler der forventes udlejet en bestemt dag baseret på vejr og ugedag.")

# Inputfelter
season = st.selectbox("Sæson", [1, 2, 3, 4], format_func=lambda x: {1: "Forår", 2: "Sommer", 3: "Efterår", 4: "Vinter"}[x])
mnth = st.slider("Måned", 1, 12, 6)
holiday = st.radio("Er det en helligdag?", ["Ja", "Nej"])
weekday = st.slider("Ugedag (0=Mandag ... 6=Søndag)", 0, 6, 2)
workingday = st.radio("Er det en arbejdsdag?", ["Ja", "Nej"])
weathersit = st.selectbox("Vejrtype", [1, 2, 3], format_func=lambda x: {1: "Klart/let skyet", 2: "Skyet", 3: "Regn/sne"}[x])
temp = st.slider("Temperatur (0-1)", 0.0, 1.0, 0.5)
hum = st.slider("Luftfugtighed (0-1)", 0.0, 1.0, 0.5)
windspeed = st.slider("Vindstyrke (0-1)", 0.0, 1.0, 0.3)
yr = st.selectbox("År", [0, 1], format_func=lambda x: "2011" if x == 0 else "2012")

# Base input dictionary – uden 'atemp'
base_input = {
    "yr": yr,
    "mnth": mnth,
    "holiday": 1 if holiday == "Ja" else 0,
    "workingday": 1 if workingday == "Ja" else 0,
    "weathersit": weathersit,
    "temp": temp,
    "hum": hum,
    "windspeed": windspeed
}

# One-hot encoding for 'season'
for s in range(1, 5):
    base_input[f"season_{s}"] = 1 if season == s else 0

# One-hot encoding for 'weekday'
for d in range(0, 7):
    base_input[f"weekday_{d}"] = 1 if weekday == d else 0

# Konverter til DataFrame
input_df = pd.DataFrame([base_input])

<<<<<<< HEAD
# Forudsig
try:
    model_path = os.path.join(os.path.dirname(__file__), '..', 'models', 'random_forest_model.joblib')
    model = joblib.load(model_path)
=======
if st.button("Forudsig antal udlejninger"):
>>>>>>> 1e27d7bd3802a307d397619b7ef134b7ab6e1576
    prediction = model.predict(input_df)[0]
    st.success(f"Forventet antal cykeludlejninger: {int(prediction)}")
except Exception as e:
    st.error(f"Kunne ikke forudsige: {e}")
