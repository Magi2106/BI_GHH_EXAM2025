import streamlit as st
import pandas as pd
import joblib
import matplotlib.pyplot as plt
import seaborn as sns

# Indlæs model
model = joblib.load('models/linear_model.joblib')
feature_names = joblib.load('models/feature_names.joblib')

st.set_page_config(page_title="SmartBike Forudsigelse", layout="centered")
st.title("SmartBike – Forudsig cykeludlejning")

st.markdown("Forudsig hvor mange cykler der forventes udlejet en bestemt dag baseret på vejr og tidspunkt.")

# Brugerinputs
temp_c = st.slider("Temperatur (°C)", -5, 40, 20)
atemp_c = st.slider("Følt temperatur (°C)", -5, 45, 21)
hum_percent = st.slider("Luftfugtighed (%)", 0, 100, 60)
windspeed_ms = st.slider("Vindstyrke (m/s)", 0, 67, 15)

season = st.selectbox("Sæson", ['Spring', 'Summer', 'Fall', 'Winter'])
weekday = st.selectbox("Ugedag", ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'])


temp = temp_c / 41
atemp = atemp_c / 50
hum = hum_percent / 100
windspeed = windspeed_ms / 67


input_dict = {
    'temp': temp,
    'atemp': atemp,
    'hum': hum,
    'windspeed': windspeed,
    f'season_{season}': 1,
    f'weekday_{weekday}': 1
}


input_df = pd.DataFrame([input_dict])
for col in feature_names:
    if col not in input_df.columns:
        input_df[col] = 0


input_df = input_df[feature_names]


if st.button(" Forudsig antal udlejninger"):
    try:
        prediction = model.predict(input_df)[0]
        st.success(f" Forventet antal udlejninger: **{int(prediction)} cykler**")

        
        try:
            df = pd.read_csv("data/processed/bike_cleaned.csv")
            for col in ['dteday', 'season', 'weekday']:
                if col in df.columns:
                    df = df.drop(columns=[col])

            st.subheader(" Korrelationer i data")
            fig, ax = plt.subplots(figsize=(10, 6))
            sns.heatmap(df.corr(), annot=True, cmap="coolwarm", fmt=".2f", ax=ax)
            st.pyplot(fig)
        except Exception as viz_error:
            st.warning(f"Kunne ikke vise visualisering: {viz_error}")

    except Exception as e:
        st.error(f"Kunne ikke forudsige: {e}")
