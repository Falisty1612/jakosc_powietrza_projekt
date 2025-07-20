import json #pliki JSON
import os #do pracy z plikami i katalogami
import datetime #do pracy z datami
import pandas as pd #do pracy z danymi tabelkowymi
import csv #do pracy z plikami CSV

#impport dzisiejszej daty
today = datetime.date.today().isoformat()

#ścieżka do pliku wejściowego JSON (z raw)
INPUT_FILE = f"data/raw/airly/{today}.json"

#ścieżka do pliku wyjściowego CSV (do processed)
OUTPUT_FILE = f"data/processed/airly/airly_{today}.csv"

#wczytywanie danych z pliku JSON
with open(INPUT_FILE, "r", encoding="utf-8") as f:
    data = json.load(f)

#lista do przechowywania wierszy CSV
rows = []

#funckja do przetwarzania pomiarów
#przyjmuje pojedynczy pomiar i dodaje go do listy rows
def process_measurement(measurement):
    from_time = measurement.get('fromDateTime')
    till_time = measurement.get('tillDateTime')
    for val in measurement.get('values', []):
        rows.append({
            'fromDateTime': from_time,
            'tillDateTime': till_time,
            'parameter': val['name'],
            'value': val['value']
        })

#przetwarzanie pomiarów z 'current'
process_measurement(data['current'])

#przetwaraznie każdego pomiaru w 'history'
for hist in data.get('history', []):
    process_measurement(hist)

#zapis do pliku CSV
with open(OUTPUT_FILE, 'w', newline='') as csvfile:
    fieldnames = ['fromDateTime', 'tillDateTime', 'parameter', 'value']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(rows)

print("Zapisano do airly_data.csv")