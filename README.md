#  SmartBike – Forudsigelse af cykeludlejning med BI og AI

Dette projekt er en del af eksamensopgaven i Business Intelligence (2025) og fokuserer på at forudsige efterspørgslen efter bycykler baseret på historiske data, vejr og ugedag. Løsningen anvender dataanalyse, maskinlæring og en interaktiv webapp til at præsentere resultatet for ikke-tekniske brugere.

##  Problemformulering

Cykeludlejning i byer kan være uforudsigelig og ineffektiv. Ved at analysere historiske mønstre og vejrdata kan vi bygge en model, der forudsiger efterspørgslen og dermed gør det muligt for udlejere og kommuner at planlægge bedre.

##  Projektstruktur

BI_GHH_EXAM2025/
├── app/ → Streamlit dashboard
├── data/
│ ├── raw/ → Originalt datasæt (day.csv)
│ └── processed/ → Renset datasæt (bike_cleaned.csv)
├── models/ → Trænet model (.joblib) og featureliste
├── scripts/ → EDA, data preparation og modeltræning
├── docs/ → Dokumentation for Sprint 1-4
├── output/ → Grafer fra EDA
├── requirements.txt → Krævede Python-biblioteker
└── README.md


##  Metoder og teknologier

- Python (pandas, matplotlib, seaborn, scikit-learn, joblib)
- Streamlit til dashboard
- Lineær regression til forudsigelse
- One-hot encoding af kategorier
- Github til versionstyring

##  Dashboard

Dashboardet lader brugeren vælge temperatur, luftfugtighed, sæson og ugedag og viser en forudsigelse af det forventede antal cykeludlejninger.

### Sådan starter du appen:

```bash
streamlit run app/dashboard.py
