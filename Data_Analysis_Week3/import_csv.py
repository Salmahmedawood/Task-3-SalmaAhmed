import pandas as pd
import sqlite3

# Read the CSV file into a DataFrame
df = pd.read_csv('Cleaned_Dataset.csv')

# Create Database 
conn = sqlite3.connect('sales.db')

# Create Table
df.to_sql('sales_data', conn, if_exists='replace', index=False)

conn.close()

print("Data has been successfully imported into the SQLite database.")