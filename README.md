# Chinook API 

A simple FastAPI project exposing queries from the Chinook music database.

## Features

- `/customers_usa` → List of all USA customers
- `/invoices_above_20` → Invoices with Total >= $20
- `/top_countries` → Top 3 countries by revenue
- `/long_tracks_by_genre` → Genres with Average lenght >= 5 minutes
- `/rock_genre` → List of all the "Rock" Genre songs
- `/avg_invoice_per_country` → Average Invoice of each country 
- `/min_max_track_length` → Min&Max track length of each genre
## Setup

1. Clone repo and install dependencies:
   ```bash
   pip install -r requirements.txt

2. Run the API:
   uvicorn main:app --reload

3. Open in browser:
   Home: http://127.0.0.1:8000/
   Docs: http://127.0.0.1:8000/docs

## 📓 Notebook

- [Chinook SQL Analysis](./chinook_sql_analysis.ipynb):  
  Contains SQL queries, pandas analysis, and visualizations exploring customer behavior, revenue by country, and track insights using the Chinook sample database.
