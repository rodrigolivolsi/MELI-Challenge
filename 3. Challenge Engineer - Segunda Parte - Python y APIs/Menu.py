import os

#importo las funciones de los otros archivos .py
from BarrerItems import barrer_items
from DumpVariablesItems import dump_item_variables
from AgregarEliminarItem import add_item_csv, delete_item_csv

#funcion para mostrar las opciones del menu
def show_menu():
    print("\n=== MAIN MENU ===")
    print("1- Barrer items desde 'Querysparabarrer.txt' (NO OLVIDAR DE EDITAR LAS QUERYS DE SER NECESARIO) y generar 'itemsidbarridos.txt'")
    print("2- Dumpear items barridos desde 'itemsidbarridos.txt' al CSV 'items_variables.csv'")
    print("3- Agregar un item al CSV mediante una ID")
    print("4- Eliminar un item del CSV mediante una ID")
    print("5- Salir")
    print("======================")

#funcion para la opcion 1
def option_barrer_items():
    query_file = "Querysparabarrer.txt"
    output_file = "itemsidbarridos.txt"
    if os.path.exists(query_file):
        barrer_items(query_file, output_file)
        print(f"Items barridos exitosamente en '{output_file}'.")
    else:
        print(f"El archivo '{query_file}' no existe.")

#funcion para la opcion 2
def option_dumpear_items():
    input_file = "itemsidbarridos.txt"
    output_csv = "items_variables.csv"
    if os.path.exists(input_file):
        dump_item_variables(input_file, output_csv)
        print(f"Items dumpeados exitosamente en '{output_csv}'.")
    else:
        print(f"El archivo '{input_file}' no existe.")

#funcion para la opcion 3
def option_add_item():
    #se verifica si el CSV existe antes de permitir agregar
    if os.path.exists('items_variables.csv'):
        archivo_csv = 'items_variables.csv'
        item_id = input("Ingrese la ID del item a agregar: ")
        add_item_csv(item_id, archivo_csv)
    else:
        print("Error: Debes ejecutar primero las opciones 1 y 2 para crear el CSV.")    
        
#funcion para la opcion 4
def option_delete_item():
    #se verifica si el CSV existe antes de permitir eliminar
    if os.path.exists('items_variables.csv'):
        archivo_csv = 'items_variables.csv'
        item_id = input("Ingrese la ID del item a eliminar: ")
        delete_item_csv(item_id, archivo_csv)
    else:
        print("Error: Debes ejecutar primero las opciones 1 y 2 para crear el CSV.")    

def main_menu():
    while True: #para que quede constantemente activo, solo se sale del menu eligiendo la opcion 5
        show_menu()
        opcion = input("Seleccione una opcion (1-5): ")
        
        if opcion == "1":
            option_barrer_items()
        elif opcion == "2":
            option_dumpear_items()
        elif opcion == "3":
            option_add_item()
        elif opcion == "4":
            option_delete_item()
        elif opcion == "5":
            print("Saliendo del menu.")
            break
        else:
            print("Opcion invalida, por favor seleccione una opcion valida (1-5).")

#se ejecuta el menu
if __name__ == "__main__":
    main_menu()
