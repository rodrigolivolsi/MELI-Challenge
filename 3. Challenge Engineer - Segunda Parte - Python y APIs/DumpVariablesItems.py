import requests
import csv
import json
import os

#funcion para obtener los detalles de un item por su ID
def fetch_item_details(item_id):
    url = f"https://api.mercadolibre.com/items/{item_id}"
    response = requests.get(url)
    
    if response.status_code == 200: #chequeo de recibir un status code 200 sino informo que hay un error en la peticion
        return response.json()
    else:
        print(f"Error al obtener el item {item_id}: {response.status_code}")
        return None

#funcion para extraer las variables de interes del JSON del item
def extract_item_data(item_json):
    shipping = item_json.get('shipping', {}) #extraigo shipping antes del return porque es un JSON
    seller_address = item_json.get('seller_address', {}) #extraigo seller_address antes del return porque es un JSON

    return {
        'id': item_json.get('id', ''),
        'title': item_json.get('title', ''),
        'price': item_json.get('price', ''),
        'base_price': item_json.get('base_price', ''),
        'original_price': item_json.get('original_price', ''),
        'initial_quantity': item_json.get('initial_quantity', ''),
        'buying_mode': item_json.get('buying_mode', ''),
        'listing_type_id': item_json.get('listing_type_id', ''),
        'condition': item_json.get('condition', ''),
        'accepts_mercadopago': item_json.get('accepts_mercadopago', ''),
        'shipping_mode': shipping.get('mode', ''),
        'local_pick_up': shipping.get('local_pick_up', ''),
        'free_shipping': shipping.get('free_shipping', ''),
        'logistic_type': shipping.get('logistic_type', ''),
        'store_pick_up': shipping.get('store_pick_up', ''),
        'city_name': seller_address.get('city', {}).get('name', ''),
        'state_name': seller_address.get('state', {}).get('name', ''),
        'country_name': seller_address.get('country', {}).get('name', ''),
        'status': item_json.get('status', ''),
        'warranty': item_json.get('warranty', ''),
        'date_created': item_json.get('date_created', ''),
        'last_updated': item_json.get('last_updated', ''),
        'health': item_json.get('health', '')
    }

#funcion para leer los ids desde el archivo itemsidbarridos.txt
def read_ids_from_file(file_path):
    with open(file_path, 'r') as file:
        content = file.read().strip()
        return content.split(',')

#funcion para escribir los datos (variables que me interesan) en un archivo CSV
def write_data_to_csv(data, file_path):
    #especifico los nombres de las columnas
    fieldnames = ['id', 'title', 'price', 'base_price', 'original_price', 'initial_quantity', 
                  'buying_mode', 'listing_type_id', 'condition', 'accepts_mercadopago', 
                  'shipping_mode', 'local_pick_up', 'free_shipping', 'logistic_type', 'store_pick_up',
                  'city_name', 'state_name', 'country_name', 'status', 'warranty', 
                  'date_created', 'last_updated', 'health']

    #escribo en el CSV
    with open(file_path, 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for item in data:
            writer.writerow(item)

#funcion principal para procesar los items y generar el archivo CSV
def dump_item_variables(input_file, output_csv):
    ids_file = input_file
    output_file = output_csv
    
    item_ids = read_ids_from_file(ids_file)
    all_items_data = []
    
    for item_id in item_ids:
        print(f"Procesando item: {item_id}...")
        item_json = fetch_item_details(item_id)
        
        if item_json:
            item_data = extract_item_data(item_json)
            all_items_data.append(item_data)
    
    #escribo todos los datos en el archivo CSV
    write_data_to_csv(all_items_data, output_file)
    print(f"Se han guardado los datos de {len(all_items_data)} items en {output_file}")
