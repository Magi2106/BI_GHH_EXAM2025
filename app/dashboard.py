import streamlit as st
import pandas as pd
import joblib

# Indlæs model og feature-navne
model = joblib.load('models/linear_model.joblib')
feature_names = joblib.load('models/feature_names.joblib')

st.set_page_config(page_title="SmartBike Forudsigelse", layout="centered")
st.title("SmartBike – Forudsig cykeludlejning")

st.write("Vælg vejr og dag, og se hvor mange cykler der forventes udlejet.")

# Temperatur i grader celsius
temp_c = st.slider("Temperatur (°C)", -5, 40, 20)
atemp_c = st.slider("Følt temperatur (°C)", -5, 45, 21)

# Luftfugtighed i %
hum_percent = st.slider("Luftfugtighed (%)", 0, 100, 60)

# Vindstyrke i m/s
windspeed_ms = st.slider("Vindstyrke (m/s)", 0, 67, 15)



# Sæson og ugedag
season = st.selectbox("Sæson", ['Spring', 'Summer', 'Fall', 'Winter'])
weekday = st.selectbox("Ugedag", ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'])

# Konverter til modelens skala
temp = temp_c / 41
atemp = atemp_c / 50
hum = hum_percent / 100
windspeed = windspeed_ms / 67

# Lav dictionary til input
input_dict = {
    'temp': temp,
    'atemp': atemp,
    'hum': hum,
    'windspeed': windspeed,
    f'season_{season}': 1,
    f'weekday_{weekday}': 1
}

# Konverter til DataFrame og tilføj manglende features som 0
input_df = pd.DataFrame([input_dict])
for col in feature_names:
    if col not in input_df.columns:
        input_df[col] = 0

# Sørg for at kolonnerne står i rigtig rækkefølge
input_df = input_df[feature_names]


if st.button("Forudsig antal udlejninger"):
    prediction = model.predict(input_df)[0]
    st.subheader(f"Forventet antal udlejninger: **{int(prediction)} cykler**")

