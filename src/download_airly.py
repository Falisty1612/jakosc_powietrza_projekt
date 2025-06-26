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

load_dotenv()
AIRLY_API_KEY = os.getenv("AIRLY_API_KEY")