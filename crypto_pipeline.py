import requests
import pandas as pd
import sqlite3

# API URL
url = "https://api.coingecko.com/api/v3/coins/markets"

# Parameters
params = {
    "vs_currency": "usd",
    "order": "market_cap_desc",
    "per_page": 100,
    "page": 1,
    "sparkline": False
}

# Fetch data
response = requests.get(url, params=params)

data = response.json()

# Create DataFrame
df = pd.DataFrame(data)

print("Dataset Shape:", df.shape)

# Select useful columns
selected_columns = [
    'name',
    'symbol',
    'current_price',
    'market_cap',
    'market_cap_rank',
    'total_volume',
    'price_change_percentage_24h',
    'circulating_supply',
    'last_updated'
]

crypto_df = df[selected_columns]

# Save cleaned CSV
crypto_df.to_csv("crypto_cleaned.csv", index=False)

print(crypto_df.head())

# Create SQLite database
conn = sqlite3.connect("crypto.db")

crypto_df.to_sql(
    "crypto_market",
    conn,
    if_exists="replace",
    index=False
)

conn.close()

print("Data loaded into SQLite database!")

import sqlite3
import pandas as pd

conn = sqlite3.connect("crypto.db")

query = """
SELECT *
FROM crypto_market
LIMIT 10
"""

result = pd.read_sql(query, conn)

print(result)

conn.close()

conn = sqlite3.connect("crypto.db")

SELECT *
FROM crypto_market
LIMIT 10;