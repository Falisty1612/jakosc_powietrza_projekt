
# 📅 Plan 4-tygodniowego projektu analizy jakości powietrza

## Tydzień 1 – Pobieranie i eksploracja danych

**🔸 Dzień 1** 
- Załóż konto w serwisie [Airly](https://developer.airly.org/)
- Wygeneruj swój klucz API
- Przeczytaj dokumentację API Airly i Open-Meteo
- Zapisz dane dostępowe w pliku `docs/API_keys.md`

**🔸 Dzień 2**
- Pobierz dane GIOŚ (np. PM2.5, PM10) jako plik `.csv`
- Zapisz dane do folderu `data/raw/gios.csv`

**🔸 Dzień 3**
- Utwórz skrypt `download_airly.py`, który pobiera dane z Airly (API, JSON)`
- Uruchom go i zapisz dane jako `data/raw/airly.json`

**🔸 Dzień 4**
- Skorzystaj z darmowego API pogodowego [Open-Meteo](https://open-meteo.com/)
- Pobierz dane pogodowe dla Krakowa (np. temperatura, wilgotność, wiatr)
- Zapisz do pliku `data/raw/weather.csv`

**🔸 Dzień 5**
- Otwórz Jupyter Notebook i stwórz `01_exploration.ipynb`
- Wczytaj dane z 3 źródeł (Airly, GIOŚ, Pogoda)
- Wykonaj eksplorację: `head()`, `info()`, `describe()`, sprawdź kolumny, typy danych

---

## Tydzień 2 – Czyszczenie i przygotowanie danych

**🔸 Dzień 1–2**
- Usuń lub oznacz brakujące dane (`NaN`)
- Ujednolić daty (`datetime`) i jednostki (µg/m³, °C itp.)

**🔸 Dzień 3**
- Normalizuj nazwy kolumn (np. lowercase, `snake_case`)
- Upewnij się, że dane mają wspólny format daty/godziny

**🔸 Dzień 4**
- Stwórz `combine_data.py` – skrypt łączący dane GIOŚ, Airly i pogodowe
- Zapisz wynik do `data/combined.csv`

**🔸 Dzień 5**
- W notebooku `02_cleaning.ipynb` udokumentuj cały proces oczyszczania i łączenia danych

---

## Tydzień 3 – Analiza i wizualizacja danych

**🔸 Dzień 1**
- W notebooku `03_analysis.ipynb` oblicz średnie dobowe i tygodniowe stężenia (PM2.5, PM10)

**🔸 Dzień 2**
- Stwórz wykresy trendów: liniowe, słupkowe, rolling average (np. 7 dni)

**🔸 Dzień 3**
- Analizuj korelację z pogodą (np. PM2.5 vs. temperatura, wiatr, wilgotność)
- Użyj wykresów scatter i `corr()`

**🔸 Dzień 4**
- Stwórz heatmapy, wykresy z biblioteki Plotly lub Seaborn
- Jeśli potrafisz – dodaj mapę Krakowa z zaznaczoną jakością powietrza (opcjonalnie)

**🔸 Dzień 5**
- Zapisz wykresy do folderu `figures/`
- Uporządkuj i skomentuj notebook `03_analysis.ipynb`

---

## Tydzień 4 – Wnioski i prezentacja projektu

**🔸 Dzień 1**
- W notebooku `04_conclusions.ipynb` napisz krótkie podsumowanie wyników:
  - Jakie są główne źródła zanieczyszczeń?
  - Kiedy powietrze jest najgorsze?
  - Jaki wpływ ma pogoda?

**🔸 Dzień 2**
- Uzupełnij plik `README.md`:
  - Opis projektu
  - Technologie
  - Struktura katalogów
  - Harmonogram

**🔸 Dzień 3**
- Wgraj cały projekt na GitHub
- Sprawdź czy wszystkie pliki są w repozytorium (notebooki, dane, wykresy)

**🔸 Dzień 4–5**
- Dopisz projekt do swojego CV
- (Opcjonalnie) Wstaw link na swój profil LinkedIn
- Możesz nagrać demo wideo (np. Loom) albo przygotować prezentację w PowerPoint
