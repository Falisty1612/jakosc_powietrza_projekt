import json #pliki JSON
import os #do pracy z plikami i katalogami
import datetime #do pracy z datami
import pandas as pd #do pracy z danymi tabelkowymi

#impport dzisiejszej daty
today = datetime.date.today().isoformat()

#ścieżka do pliku wejściowego JSON (z raw)
INPUT_FILE = f"data/raw/meteo/{today}.json"

#ścieżka do pliku wyjściowego CSV (do processed)
OUTPUT_FILE = "data/processed/meteo.csv"


#wczytywanie danych z pliku JSON
with open(INPUT_FILE, "r", encoding="utf-8") as f:
    data = json.load(f)
    
#wyciąganie sekcji  'hourly'
hourly = data["hourly"]

#tworzenie DataFrame z wybranych danych
df = pd.DataFrame({
    "time": hourly["time"],
    "temperature_2m": hourly["temperature_2m"],
    "relative_humidity_2m": hourly["relative_humidity_2m"],
    "windspeed_10m": hourly["windspeed_10m"]
})

try:
    #tworzenie folderu (jeśli nie istnieje)
    os.makedirs(os.path.dirname(OUTPUT_FILE), exist_ok=True)
    #zapis do pliku CSV
    df.to_csv(OUTPUT_FILE, index=False)
    print("✅ Dane pogodowe zapisane do:", OUTPUT_FILE)

#wyjątek w przypadku błędu poprawnego zapisu
except Exception as e:
    print(f"❌ Błąd podczas zapisu do pliku: {e}")
    exit(1)

