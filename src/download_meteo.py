import requests #biblo do żadań HTTP
import json #pliki JSON
import os #do pracy z plikami i katalogami
import datetime #do pracy z datami



#Współrzędne geograficzne dla Krakowa
LATITUDE = 50.0614
LONGITUDE = 19.9366


#impport dzisiejszej daty
today = datetime.date.today().isoformat()

#ścieżna do pliku wyjściowego (tam mnie zapiszą się dane)
OUTPUT_FILE = f"data/raw/meteo/{today}.json"

#adres URL do Meteo
URL = "https://api.open-meteo.com/v1/forecast"

#parametry zaptyania
params = {
    "latitude": LATITUDE,
    "longitude": LONGITUDE,
    "hourly": "temperature_2m,relative_humidity_2m,windspeed_10m",
    "timezone": "Europe/Warsaw"
}



#funkcja pobierająca dane z Open Meteo
def download_meteo_data():
    #wysłanie żądania GET do Meteo
    response = requests.get(URL, params=params)

    
    if response.status_code == 200: # kod 200 oznacza, że żądanie się powiodło
        data = response.json()  #przekształcaanie danych z formatu JSON na Python dict

        #tworzenie folderu (jesli takowy nie istnieje)
        os.makedirs(os.path.dirname(OUTPUT_FILE), exist_ok=True)

        #zapis danych do pliku .json (ładnie sformatowane)
        with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4, ensure_ascii=False)

        print("✅✅ Dane Meteo zapisane do:", OUTPUT_FILE, " ✅✅")

    #obsługa błędów
    else:
        print(f"❌ ❌ Błąd podczas pobierania danych!!! {response.status_code} ❌ ❌")
        print(response.text)

#uruchomienie pliku tylko, jeśli plik został uruchomiony jako skrypt (nie importowany)
if __name__ == "__main__":
    download_meteo_data()