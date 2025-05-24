import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import joblib
import os

# Læs renset data
df = pd.read_csv('../data/processed/bike_cleaned.csv')

# Konverter kategorier til dummies
df = pd.get_dummies(df, columns=['season', 'weekday'], drop_first=True)

# Print til debug:
print("Kolonner i datasæt efter get_dummies:")
print(df.columns.tolist())

# Split i X og y
X = df.drop(columns=['cnt', 'dteday'])  # behold kun de brugbare features
y = df['cnt']

# Split til træning og test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Træn modellen
model = LinearRegression()
model.fit(X_train, y_train)

# Evaluer modellen
y_pred = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f"MSE: {mse:.2f}")
print(f"R^2 Score: {r2:.2f}")

# Gem model og feature-navne
os.makedirs('../models', exist_ok=True)
joblib.dump(model, '../models/linear_model.joblib')
joblib.dump(X.columns.tolist(), '../models/feature_names.joblib')

print(" Model og feature-liste gemt.")
