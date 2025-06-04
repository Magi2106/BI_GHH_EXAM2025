import pandas as pd
import joblib
import os

# Indlæs det forbehandlede datasæt
df = pd.read_csv("data/processed/bike_cleaned.csv")

# Fjern target-kolonnen
X = df.drop("cnt", axis=1)

# Sørg for, at mappen eksisterer
os.makedirs("models", exist_ok=True)

# Gem feature-navnene
joblib.dump(X.columns.tolist(), "models/rf_feature_names.joblib")

print("✔ Feature-navne gemt i models/rf_feature_names.joblib")
