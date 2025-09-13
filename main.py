from fastapi import FastAPI
import sqlite3
import pandas as pd

app = FastAPI()

# connect to database
def get_connection():
    return sqlite3.connect("Chinook_Sqlite.sqlite")

# Home route
@app.get("/")
def home():
    return {"message": "Welcome to Chinook API "}

# 1) Customers from USA
@app.get("/customers_usa")
def customers_usa():
    con = get_connection()
    query = """
    SELECT FirstName || ' ' || LastName AS FullName, Country
    FROM Customer
    WHERE Country = 'USA';
    """
    df = pd.read_sql(query, con)
    return df.to_dict(orient="records")

# 2) Invoices above $20
@app.get("/invoices_above_20")
def invoices_above_20():
    con = get_connection()
    query = """
    SELECT InvoiceId, CustomerId, Total
    FROM Invoice
    WHERE Total >= 20;
    """
    df = pd.read_sql(query, con)
    return df.to_dict(orient="records")

# 3) Top 3 countries by revenue
@app.get("/top_countries")
def top_countries():
    con = get_connection()
    query = """
    SELECT BillingCountry, SUM(Total) AS Revenue
    FROM Invoice
    GROUP BY BillingCountry
    ORDER BY Revenue DESC
    LIMIT 3;
    """
    df = pd.read_sql(query, con)
    return df.to_dict(orient="records")

# 4) Long tracks by genre (average track length >= 5 minutes)
@app.get("/long_tracks_by_genre")
def long_tracks_by_genre():
    con = get_connection()
    query= """
    SELECT g.Name AS Genre,
    ROUND(AVG(t.Milliseconds)/60000,2) AS AvgMinutes
    FROM Track t
    JOIN Genre g on g.GenreId = t.GenreId
    GROUP BY g.Name
    HAVING AvgMinutes >= 5
    ORDER BY AvgMinutes DESC;
    """
    df = pd.read_sql(query,con)
    return df.to_dict(orient="records")

# 5) Tracks from the rock genre 
@app.get("/rock_genre")
def rock_genre():
    con = get_connection()
    query = """
    SELECT g.Name as Genre ,
    t.Name as SongName
    FROM Track t
    JOIN Genre g on g.GenreId = t.GenreId
    WHERE g.Name = 'Rock';
    """
    df = pd.read_sql(query,con)
    return df.to_dict(orient="records")

# 6) Average invoice per country
@app.get("/avg_invoice_per_country")
def avg_invoice_per_country():
    con = get_connection()
    query = """
    SELECT BillingCountry, ROUND(AVG(Total),2) AS AvgInvoice
    FROM Invoice
    GROUP BY BillingCountry
    ORDER BY AvgInvoice DESC;
    """
    df = pd.read_sql(query, con)
    return df.to_dict(orient="records")

