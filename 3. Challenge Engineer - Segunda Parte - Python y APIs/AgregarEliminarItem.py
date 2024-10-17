import csv
import requests
import json
import os

#funcion para obtener datos del item desde la API de Mercado Libre
def fetch_item_details(item_id):
    url = f"https://api.mercadolibre.com/items/{item_id}"
    response = requests.get(url)
    if response.status_code == 200: #chequeo de recibir un status code 200 sino informo que hay un error en la peticion
        return response.json()
    else:
        print(f"Error al obtener el ítem {item_id}: {response.status_code}")
        return None

#funcion para escribir los datos del item en el CSV
def write_item_to_csv(item_data, archivo_csv):
    with open(archivo_csv, mode='a', newline='') as file:
        writer = csv.writer(file)
        shipping = item_data.get('shipping', {}) #extraigo shipping antes de escribir en el csv porque es un JSON
        seller_address = item_data.get('seller_address', {}) #extraigo seller_address antes de escribir en el csv porque es un JSON
        #obtengo las variables de interes del JSON
        writer.writerow([
            item_data.get('id'),
            item_data.get('title'),
            item_data.get('price'),
            item_data.get('base_price'),
            item_data.get('original_price'),
            item_data.get('initial_quantity'),
            item_data.get('buying_mode'),
            item_data.get('listing_type_id'),
            item_data.get('condition'),
            item_data.get('accepts_mercadopago'),
            shipping.get('mode'),
            shipping.get('local_pick_up'),
            shipping.get('free_shipping'),
            shipping.get('logistic_type'),
            shipping.get('store_pick_up'),
            seller_address.get('city', {}).get('name'),
            seller_address.get('state', {}).get('name'),
            seller_address.get('country', {}).get('name'),
            item_data.get('status'),
            item_data.get('warranty'),
            item_data.get('date_created'),
            item_data.get('last_updated'),
            item_data.get('health')
        ])

#funcion para leer todos los ids ya existentes en el CSV
def read_existing_ids(archivo_csv):
    if not os.path.exists(archivo_csv):
        return set()
    
    with open(archivo_csv, mode='r') as file:
        reader = csv.reader(file)
        return {row[0] for row in reader}  #asumo que el id esta en la primera columna

#funcion para agregar un item al CSV si no existe
def add_item_csv(item_id, archivo_csv):
    ids_existentes = read_existing_ids(archivo_csv)
    if item_id in ids_existentes: #chequeo duplicados
        print(f"El item {item_id} ya existe en el archivo.")
    else:
        item_data = fetch_item_details(item_id)
        if item_data:
            write_item_to_csv(item_data, archivo_csv)
            print(f"Ítem {item_id} agregado al archivo.")
        else:
            print(f"No se pudo agregar el item {item_id}.")

#funcion para eliminar un item del CSV
def delete_item_csv(item_id, archivo_csv):
    if not os.path.exists(archivo_csv):
        print(f"El archivo {archivo_csv} no existe.")
        return

    ids_existentes = read_existing_ids(archivo_csv)
    if item_id not in ids_existentes:
        print(f"El item {item_id} no se encuentra en el archivo.")
        return

    #reescribo el CSV sin el item a eliminar
    with open(archivo_csv, mode='r') as file:
        lines = list(csv.reader(file))

    with open(archivo_csv, mode='w', newline='') as file:
        writer = csv.writer(file)
        for row in lines:
            if row[0] != item_id:
                writer.writerow(row)
    
    print(f"el item {item_id} se elimino del archivo.")
