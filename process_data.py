# process_data.py

import json
import pandas as pd

def safe_json_loads(s):
    try:
        return json.loads(s)
    except json.JSONDecodeError:
        s = s.replace('\\', '\\\\')
        return json.loads(s)

def process_raw_data_to_orders(raw_data, stores):
    orders_list = []

    for index, row in raw_data.iterrows():
        ticket = safe_json_loads(row['tickets'])
        
        order_id = ticket['ticket_id']
        store_name = ticket['restaurant']['name']
        store_address = ticket['restaurant']['address']
        store_phone = ticket['restaurant']['phone']
        order_date = ticket['billDetails']['date']
        order_time = ticket['billDetails']['time']
        total_price = ticket['summary']['total']
        
        items = [item['item'] for item in ticket['items']]
        quantities = [item['quantity'] for item in ticket['items']]
        unit_prices = [item['unit_price'] for item in ticket['items']]
        
        store_row = stores[(stores['Restaurant Name'] == store_name) & 
                           (stores['Location'] == store_address)]
        
        if not store_row.empty:
            store_id = store_row['id'].values[0]
        else:
            store_id = None
        
        order_row = {
            'order_id': order_id,
            'store_id': store_id,
            'items': str(items),
            'quantity': str(quantities),
            'unit_price': str(unit_prices),
            'currency': 'EUR',
            'total_price': total_price,
            'order_date': order_date,
            'order_time': order_time
        }
        
        orders_list.append(order_row)

    orders = pd.DataFrame(orders_list)
    return orders
