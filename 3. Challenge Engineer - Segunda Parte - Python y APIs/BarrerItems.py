import requests
import json

#funcion para realizar la petición a la API de Mercadolibre y devuelve los ids de los items de una query especifica
def fetch_items(query):
    url = f"https://api.mercadolibre.com/sites/MLA/search?q={query}&limit=50"
    response = requests.get(url)
    
    if response.status_code == 200: #chequeo de recibir un status code 200 sino informo que hay un error en la peticion
        data = response.json()
        return [item['id'] for item in data.get('results', [])]
    else:
        print(f"Error al hacer la petición para {query}: {response.status_code}")
        return []

#funcion para leer queries desde el archivo Querysparabarrer.txt
def read_queries_from_file(file_path):
    with open(file_path, 'r') as file:
        content = file.read().strip()
        queries = content.split(',')
        return queries

#funcion para escribir los ids en el archivo itemsidbarridos.txt
def write_ids_to_file(ids, file_path):
    with open(file_path, 'w') as file:
        file.write(','.join(ids))

#funcion principal para barrer los items
def barrer_items(query_file, output_file_arg):
    queries_file = query_file
    output_file = output_file_arg
    
    queries = read_queries_from_file(queries_file)
    unique_ids = set()  #uso un set para asegurarme que no haya duplicados
    
    for query in queries:
        print(f"Realizando la query: {query}...")
        ids = fetch_items(query)
        unique_ids.update(ids)  #agrego solo los ids únicos al set

    #convierto el set de ids únicos de vuelta a una lista antes de escribir en el archivo
    write_ids_to_file(list(unique_ids), output_file)
    print(f"Se barrieron {len(unique_ids)} items en total y se guardaron en {output_file}")
