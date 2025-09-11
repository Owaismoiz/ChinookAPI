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
