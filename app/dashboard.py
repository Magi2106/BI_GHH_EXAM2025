import streamlit as st
import pandas as pd
import joblib

# Indlæs model og de tilhørende feature-navne
model = joblib.load('models/linear_model.joblib')
feature_names = joblib.load('models/feature_names.joblib')

st.set_page_config(page_title="SmartBike Forudsigelse", layout="centered")
st.title("SmartBike – Forudsig cykeludlejning")

st.write("Indtast forhold som vejr, ugedag og sæson, og få en forudsigelse af hvor mange cykler der forventes udlejet.")

# Brugerinput
temp = st.slider("Temperatur (normaliseret)", 0.0, 1.0, 0.5)
atemp = st.slider("Følt temperatur", 0.0, 1.0, 0.5)
hum = st.slider("Luftfugtighed", 0.0, 1.0, 0.5)
windspeed = st.slider("Vindstyrke", 0.0, 1.0, 0.2)
workingday = st.selectbox("Er det en arbejdsdag?", [1, 0])
is_weekend = st.selectbox("Er det weekend?", [1, 0])

season = st.selectbox("Sæson", ['Spring', 'Summer', 'Fall', 'Winter'])
weekday = st.selectbox("Ugedag", ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'])

# Lav tomt input dict
input_dict = {
    'temp': temp,
    'atemp': atemp,
    'hum': hum,
    'windspeed': windspeed,
    'workingday': workingday,
    'is_weekend': is_weekend,
    f'season_{season}': 1,
    f'weekday_{weekday}': 1
}

# Konverter til DataFrame og tilføj alle manglende features som 0
input_df = pd.DataFrame([input_dict])
for col in feature_names:
    if col not in input_df.columns:
        input_df[col] = 0

# Sortér kolonnerne i korrekt rækkefølge
input_df = input_df[feature_names]

# Forudsig
if st.button("Forudsig antal udlejninger"):
    prediction = model.predict(input_df)[0]
    st.subheader(f"Forventet antal udlejninger: {int(prediction)} cykler")
