import pandas as pd
import os
from datetime import datetime

# Użytkownik podaje datę (format: RRRR-MM-DD)
data_str = input("Podaj datę w formacie RRRR-MM-DD (np. 2025-07-01): ").strip()

# Tworzenie dynamicznych ścieżek do plików
airly_path = f"/data/processed/airly/airly_{data_str}.csv"
meteo_path = f"/data/processed/meteo/meteo_{data_str}.csv"
output_path = f"/data/combined/combined_{data_str}.csv"


def clean_airly(df: pd.DataFrame) -> pd.DataFrame:
    """
    Czyści i pivotuje dane z Airly:
    - Konwertuje datetime
    - Pivotuje parametry (PM1, PM25, PM10, TEMPERATURE, HUMIDITY, PRESSURE)
    - Dodaje sufiks _airly do kolumn
    """
    # Konwersja na datetime
    df['datetime'] = pd.to_datetime(df['fromDateTime']).dt.tz_localize(None)

    # Pivot – przekształcamy dane z formatu long na wide
    pivot = df.pivot_table(
        index='datetime',
        columns='name',
        values='value',
        aggfunc='first'
    )
    pivot = pivot.rename(columns=lambda x: x.lower())

    # Dodanie sufiksu źródła
    pivot = pivot.add_suffix('_airly').reset_index()
    return pivot


def clean_meteo(df: pd.DataFrame) -> pd.DataFrame:
    """
    Czyści dane pogodowe z Open-Meteo:
    - Konwertuje time na datetime
    - Zmienia nazwy kolumn na lowercase
    - Dodaje sufiks _meteo
    """
    df['datetime'] = pd.to_datetime(df['time'])
    df = df.rename(columns={
        'temperature_2m': 'temperature',
        'relative_humidity_2m': 'humidity',
        'windspeed_10m': 'windspeed',
    })

    # Wybór kolumn i dodanie sufiksu
    df = df[['datetime', 'temperature', 'humidity', 'windspeed']]
    df = df.rename(columns={
        'temperature': 'temperature_meteo',
        'humidity': 'humidity_meteo',
        'windspeed': 'windspeed_meteo'
    })
    return df


def main():
    try:
        # Wczytanie surowych danych
        df_airly_raw = pd.read_csv(airly_path)
        df_meteo_raw = pd.read_csv(meteo_path)

        # Czyszczenie
        df_airly = clean_airly(df_airly_raw)
        df_meteo = clean_meteo(df_meteo_raw)

        # Połączenie po datetime
        df_combined = pd.merge(
            df_airly, df_meteo,
            on='datetime',
            how='outer'
        ).sort_values('datetime')

        # Tworzenie katalogu jeśli nie istnieje
        os.makedirs(os.path.dirname(output_path), exist_ok=True)

        # Zapis
        df_combined.to_csv(output_path, index=False)
        print(f"✅ Dane połączone i zapisane do: {output_path}")
    except FileNotFoundError as e:
        print(f"❌ Błąd: Plik {e.filename} nie został znaleziony. Sprawdź ścieżki.")
    except pd.errors.EmptyDataError:
        print("❌ Błąd: Plik jest pusty lub nie zawiera danych.")
    except Exception as e:
        print(f"❌ Wystąpił błąd: {e}")

if __name__ == '__main__':
    main()
