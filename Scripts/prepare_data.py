import pandas as pd
import os

# Læs datasættet ind
df = pd.read_csv('../data/raw/day.csv')

# Gør dato-kolonnen klar så vi kan bruge den som rigtig dato
df['dteday'] = pd.to_datetime(df['dteday'])

# Omdan 'season' fra tal til noget man kan forstå
season_map = {1: 'Winter', 2: 'Spring', 3: 'Summer', 4: 'Fall'}
df['season'] = df['season'].map(season_map)

# Det samme med ugedage – 0 er søndag, 6 er lørdag
weekday_map = {
    0: 'Sunday', 1: 'Monday', 2: 'Tuesday',
    3: 'Wednesday', 4: 'Thursday', 5: 'Friday', 6: 'Saturday'
}
df['weekday'] = df['weekday'].map(weekday_map)

# Tilføj en ny kolonne der bare siger om det er weekend eller ej
df['is_weekend'] = df['weekday'].isin(['Saturday', 'Sunday'])

# Fjern kolonner vi ikke skal bruge i modellen
# f.eks. instant (bare ID), casual og registered (de er med i totalen cnt)
df = df.drop(columns=['instant', 'casual', 'registered'])

# Lav en mappe til det rensede datasæt hvis den ikke findes
os.makedirs('../data/processed', exist_ok=True)

# Gem det hele som ny fil klar til modellering
df.to_csv('../data/processed/bike_cleaned.csv', index=False)

print(" Data er gjort klar og gemt i /data/processed/bike_cleaned.csv")

