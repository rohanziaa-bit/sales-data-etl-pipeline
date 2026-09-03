import pandas as pd
from sqlalchemy import create_engine

engine = create_engine(
    'mssql+pyodbc://localhost/elt_dbs4?driver=ODBC+Driver+18+for+SQL+Server&trusted_connection=yes&TrustServerCertificate=yes'
)

print("Connection established successfully")

df = pd.read_csv('cleaned_users.csv')

print (df.head())
# df.to_sql('users', con=engine, if_exists='append', index=False)