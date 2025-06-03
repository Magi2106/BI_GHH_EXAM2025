#  SmartBike: Forudsigelse af cykeludlejning med BI og AI

##  Projektbeskrivelse

Bycykler er blevet en vigtig del af transporten i mange byer. Men det kan være svært at forudsige, hvornår og hvor mange cykler der skal være tilgængelige. I dette projekt vil jeg bruge dataanalyse og AI til at forudsige efterspørgslen efter cykeludlejning baseret på bl.a. vejr og tidspunkt. Vi laver både en model, der kan lave forudsigelser, og en interaktiv visualisering, som kan hjælpe planlæggere og udbydere med at træffe bedre beslutninger.

---

##  Problemformulering

**Baggrund:**  
Cykeludlejning er populært, men det er en udfordring at sikre, at der altid er nok cykler til rådighed. Vejret, ugedagen og tiden på året har stor indflydelse på efterspørgslen.

**Formål:**  
Jeg vil analysere historiske data og udvikle en model, som kan forudsige efterspørgslen efter cykler – f.eks. hvor mange cykler der vil blive brugt på en given dag eller time.

**Forskningsspørgsmål:**
1. Hvilke tidspunkter og vejrforhold påvirker brugen af cykler mest?
2. Hvor præcist kan vi forudsige efterspørgslen?
3. Hvilke faktorer er vigtigst for modellen?

**Hypoteser:**
- H1: Vejr har stor betydning for hvor mange cykler der bliver lejet.
- H2: Der er klare mønstre i brugen afhængig af ugedag og årstid.
- H3: En maskinlæringsmodel kan give brugbare forudsigelser.

---

##  Udviklingsmiljø

**Værktøjer:**
- **Programmering:** Python (Pandas, scikit-learn, matplotlib, Prophet)
- **BI-værktøjer:** Streamlit til dashboard
- **Versionstyring:** Git + GitHub
- **Editor:** VS Code

**Data:**  
[Capital Bikeshare data fra Kaggle](https://www.kaggle.com/datasets/lakshmi25npathi/bike-sharing-dataset)

##  Sprint 1: Problem Formulation - Summary

I dette første sprint blev grundlaget for projektet lagt. Fokus er på at løse et konkret problem: at forudsige efterspørgslen efter bycykler, så cykler kan fordeles bedre og mere effektivt i byen. Gennem brug af Business Intelligence og maskinlæring vil løsningen hjælpe udlejere og byplanlæggere med at forstå og reagere på cykelforbruget i forhold til tid og vejrforhold.

Jeg har valgt at bruge datasættet fra **Capital Bikeshare**, som indeholder detaljerede oplysninger om udlejninger over to år, inkl. dato, vejr, temperatur, sæson og antal udlejninger. Projektet bruger Python til dataanalyse og visualisering og bliver dokumenteret og delt via GitHub.

### Resultater og leverancer:
- Problemformulering og researchspørgsmål defineret
- Projektstruktur og værktøjer sat op (VS Code, Python, GitHub)
- Datasæt valgt og downloadet
- Visualiserings- og analyseværktøjer (matplotlib, seaborn) klar til brug

###  Projektstruktur (oprettet i sprint 1):
Projektet er klar til at gå videre til **Sprint 2: Data Preparation**, hvor datasættet skal renses, analyseres og gøres klar til modellering.

##  Sprint 2: Data Preparation – Resume

I denne sprint har jeg gjort datasættet klar til modellering. Jeg startede med at analysere og visualisere data (EDA) for at forstå mønstre og sammenhænge i udlejningerne. Derefter rensede jeg data og forberedte det til maskinlæring.

Jeg har lavet følgende:
- Omdannet ugedage og sæsoner til læsbare navne
- Tilføjet en ny kolonne for om det er weekend
- Fjernet overflødige kolonner som `instant`, `casual`, og `registered`
- Gemt det forberedte datasæt som `bike_cleaned.csv` i `/data/processed/`

Datasættet er nu i en form hvor jeg nemt kan træne modeller på det. Der var ingen store problemer med manglende værdier eller outliers, så jeg kunne holde det simpelt.

##  Sprint 3: Data Modelling – Resume

I denne sprint har jeg bygget og testet vores første forudsigelsesmodel. Jeg brugte en simpel lineær regression til at forudsige antallet af cykeludlejninger baseret på vejr, sæson og tid.

Jeg har lavet følgende:
- One-hot encoded kategorier som `season` og `weekday`
- Delt data op i trænings- og test-sæt (80/20)
- Trænet en lineær model med `scikit-learn`
- Evalueret modellen med MSE og R²-score
- Opnået en **R² på 0.82**, hvilket er et godt resultat
- Gemt den trænede model i `/models/linear_model.joblib` med `joblib`

Modellen er nu klar til at blive brugt i et dashboard eller en webapp i Sprint 4. Den er hurtig og let at integrere, og performance er fin nok til en første version.

##  Sprint 4: Business Application – Resume

I denne sidste sprint har jeg bygget et simpelt og brugervenligt dashboard med Streamlit, som gør vores løsning tilgængelig for almindelige brugere. Brugeren kan vælge vejr, dag og sæson, og systemet forudsiger hvor mange cykler der forventes udlejet den dag.

### Hvad jeg har lavet:
- Bygget en webapp med Streamlit
- Indlæst og brugt den trænede model (gemt med joblib)
- Dynamisk opbygget inputfelter til alle relevante features
- Matchet input med de præcise features modellen blev trænet med
- Vist resultatet som et tal med forudsiget antal udlejninger

Appen kan køres direkte med:
```bash
streamlit run app/dashboard.py


Projektet har vist, hvordan man kan bruge dataanalyse og machine learning til at skabe en brugbar forudsigelsesmodel for cykeludlejning. Gennem fire sprint har jeg bevæget os fra idé og problemformulering til en fuldt funktionel webapp, hvor brugeren nemt kan få indsigt i forventet efterspørgsel.

Resultaterne er både logiske og anvendelige. Modellen præsterer solidt (R² = 0.82), og dashboardet gør det let for ikke-tekniske brugere at eksperimentere med forskellige scenarier. Det kan være nyttigt for både byplanlæggere og udlejningsfirmaer, som ønsker bedre overblik og planlægning.

Hvis projektet skulle videreudvikles, kunne man:
- Tilføje realtidsdata som vejr-API'er
- Træne mere avancerede modeller (f.eks. random forest eller XGBoost)
- Integrere dashboardet med en database eller en mobil løsning
- Udvide modellen til at tage højde for events eller særlige dage

Projektet viser, hvordan selv et enkelt datasæt kan danne grundlag for en konkret og værdiskabende BI-løsning.





