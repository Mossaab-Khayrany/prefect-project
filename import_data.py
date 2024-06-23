# import_data.py

import pandas as pd
from sqlalchemy import create_engine

# Common database connection details
DB_DETAILS = {
    "host": "localhost",
    "port": "5490",
    "user": "postgres",
    "password": "admin"  # Server password
}

# Function to create a SQLAlchemy engine
def create_db_engine(database_name):
    return create_engine(
        f"postgresql+psycopg2://{DB_DETAILS['user']}:{DB_DETAILS['password']}@{DB_DETAILS['host']}:{DB_DETAILS['port']}/{database_name}"
    )

def fetch_food_data():
    engine = create_db_engine("database_one")
    query = "SELECT * FROM food"
    food = pd.read_sql(query, engine)
    return food

def fetch_stores_data():
    engine = create_db_engine("database_one")
    query = "SELECT * FROM stores"
    stores = pd.read_sql(query, engine)
    return stores

def fetch_raw_data():
    engine = create_db_engine("database_one")
    query = "SELECT * FROM raw_data"
    raw_data = pd.read_sql(query, engine)
    return raw_data
