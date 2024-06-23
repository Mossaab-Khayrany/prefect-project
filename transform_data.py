# transform_data.py

import ast
import pandas as pd

def transform_orders_to_orders_details(orders):
    orders_details_rows = []

    for _, row in orders.iterrows():
        items = ast.literal_eval(row['items'])
        quantities = ast.literal_eval(row['quantity'])
        unit_prices = ast.literal_eval(row['unit_price'])

        for item, quantity, unit_price in zip(items, quantities, unit_prices):
            quantity = int(quantity)
            unit_price = float(unit_price)
            total = quantity * unit_price
            orders_details_rows.append([row['order_id'], item, quantity, unit_price, total])

    orders_details = pd.DataFrame(orders_details_rows, columns=['order_id', 'item', 'quantity', 'unit_price', 'total'])
    return orders_details
