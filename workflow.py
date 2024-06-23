from import_data import fetch_food_data, fetch_stores_data, fetch_raw_data
from process_data import process_raw_data_to_orders
from transform_data import transform_orders_to_orders_details
from enrichment_pipeline import enrich_orders_details
from store_enriched_data import store_enriched_data_to_db, store_orders_data_to_db
from prefect import task, flow

@task
def fetch_food_data_task():
    return fetch_food_data()

@task
def fetch_stores_data_task():
    return fetch_stores_data()

@task
def fetch_raw_data_task():
    return fetch_raw_data()

@task
def process_raw_data_to_orders_task(raw_data, stores):
    return process_raw_data_to_orders(raw_data, stores)

@task
def transform_orders_to_orders_details_task(orders):
    return transform_orders_to_orders_details(orders)

@task
def enrich_orders_details_task(orders_details, food_data):
    return enrich_orders_details(orders_details, food_data)

@task
def store_enriched_data_to_db_task(enriched_data):
    store_enriched_data_to_db(enriched_data)

@task
def store_orders_data_to_db_task(orders):
    store_orders_data_to_db(orders)

@flow(name="data_processing_pipeline")
def data_processing_pipeline():
    food_data = fetch_food_data_task()
    stores_data = fetch_stores_data_task()
    raw_data = fetch_raw_data_task()

    orders = process_raw_data_to_orders_task(raw_data, stores_data)
    orders_details = transform_orders_to_orders_details_task(orders)
    
    enriched_ordersdetails = enrich_orders_details_task(orders_details, food_data)
    
    # Store the enriched data and orders back into the database
    store_enriched_data_to_db_task(enriched_ordersdetails)
    store_orders_data_to_db_task(orders)

# Run the flow
if __name__ == "__main__":
    data_processing_pipeline()
