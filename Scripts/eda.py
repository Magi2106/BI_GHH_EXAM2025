import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Læs data ind fra csv-filen
df = pd.read_csv('../data/raw/day.csv')

# Tjek grundlæggende info om data, kolonner og datatyper
print("Data Info:")
print(df.info())

# Kig lige på de første par rækker
print("\nFirst 5 Rows:")
print(df.head())

# Få lidt statistik på de numeriske kolonner
print("\nSummary Statistics:")
print(df.describe())

# Konverter datokolonnen til rigtig datetime-type
df['dteday'] = pd.to_datetime(df['dteday'])

# Lav et søjlediagram over udlejninger fordelt på ugedage
plt.figure(figsize=(8, 5))
sns.barplot(x='weekday', y='cnt', data=df, estimator=sum, palette='viridis')
plt.title('Total Bike Rentals by Weekday')
plt.xlabel('Weekday (0 = Søndag)')
plt.ylabel('Total Rentals')
plt.tight_layout()
plt.savefig('../output/rentals_by_weekday.png')
plt.close()

# Tegn en tidsserie for at se hvordan udlejninger ændrer sig over tid
plt.figure(figsize=(12, 6))
plt.plot(df['dteday'], df['cnt'], label='Total Rentals', color='teal')
plt.title('Bike Rentals Over Time')
plt.xlabel('Dato')
plt.ylabel('Total Rentals')
plt.tight_layout()
plt.savefig('../output/rentals_over_time.png')
plt.close()

# Undersøg om der er en sammenhæng mellem temperatur og udlejninger
plt.figure(figsize=(8, 5))
sns.scatterplot(x='temp', y='cnt', data=df)
plt.title('Temperature vs. Bike Rentals')
plt.xlabel('Normaliseret Temperatur')
plt.ylabel('Total Rentals')
plt.tight_layout()
plt.savefig('../output/temp_vs_rentals.png')
plt.close()

# Lav et heatmap for at se hvilke features der hænger sammen
plt.figure(figsize=(10, 8))
sns.heatmap(df.corr(), annot=True, cmap='coolwarm', fmt='.2f')
plt.title('Feature Correlation Matrix')
plt.tight_layout()
plt.savefig('../output/correlation_heatmap.png')
plt.close()

print("\nEDA færdig – graferne er gemt i ../output/")
