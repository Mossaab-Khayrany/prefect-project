# store_enriched_data.py

import pandas as pd
from sqlalchemy import create_engine

# Common database connection details
DB_DETAILS = {
    "host": "localhost",
    "port": "5499",
    "user": "postgres",
    "password": "your password"  # Server password
}

# Function to create a SQLAlchemy engine
def create_db_engine(database_name):
    return create_engine(
        f"postgresql+psycopg2://{DB_DETAILS['user']}:{DB_DETAILS['password']}@{DB_DETAILS['host']}:{DB_DETAILS['port']}/{database_name}"
    )

def store_enriched_data_to_db(enriched_data):
    engine = create_db_engine("database_one")
    enriched_data.to_sql('enriched_ordersdetails', engine, if_exists='replace', index=False)

def store_orders_data_to_db(orders):
    engine = create_db_engine("database_one")
    orders.to_sql('orders', engine, if_exists='replace', index=False)