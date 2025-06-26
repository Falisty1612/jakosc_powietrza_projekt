import requests #biblo do żadań HTTP
import json #pliki JSON
import os #do pracy z plikami i katalogami
import datetime #do pracy z datami
from dotenv import load_dotenv #do ładowania zmiennych środowiskowych z pliku .env



#Współrzędne geograficzne dla Krakowa
LATITUDE = 50.0614
LONGITUDE = 19.9366


#impport dzisiejszej daty
today = datetime.date.today().isoformat()

#ścieżna do pliku wyjściowego (tam mnie zapiszą się dane)
OUTPUT_FILE = f"data/raw/airly/{today}.json"

#ładowanie klucza z pliku .env
load_dotenv()
AIRLY_API_KEY = os.getenv("AIRLY_API_KEY")

#adres URL do API Airly
URL = "https://airapi.airly.eu/v2/measurements/point"

#parametry (współrzędne geograficzne)
params = {
    "lat": LATITUDE,
    "lng": LONGITUDE
}

#nagłówki HTTP (klucz i format danych)
headers = {
    "Accept": "application/json",
    "apikey": AIRLY_API_KEY
}

# 🧠 Funkcja pobierająca dane z API Airly
def download_airly_data():
    #wysłanie żądania GET do API Airly
    response = requests.get(URL, headers=headers, params=params)

    
    if response.status_code == 200: # kod 200 oznacza, że żądanie się powiodło
        data = response.json()  #przekształcaanie danych z formatu JSON na Python dict

        #tworzymy folderu (jesli takowy nie istnieje)
        os.makedirs(os.path.dirname(OUTPUT_FILE), exist_ok=True)

        #zapis danych do pliku .json (ładnie sformatowane)
        with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4, ensure_ascii=False)

        print("✅ Dane Airly zapisane do:", OUTPUT_FILE)

    #obsługa błędów
    else:
        print(f"❌ Błąd podczas pobierania danych!!! {response.status_code}")
        print(response.text)

#uruchomienie pliku tylko, jeśli plik został uruchomiony jako skrypt (nie importowany)
if __name__ == "__main__":
    download_airly_data()