import os  # Importa el módulo os para interactuar con el sistema operativo
import json  # Importa el módulo json para trabajar con archivos JSON

BASE_DIR = os.path.dirname(os.path.abspath(__file__))  # Obtiene el directorio base del archivo actual

def cargar_datos(ruta_relativa): # Función para cargar datos desde un archivo JSON dado su ruta relativa
    ruta_absoluta = os.path.join(BASE_DIR, ruta_relativa)  # Convierte la ruta relativa en una ruta absoluta
    try:
        with open(ruta_absoluta, 'r') as archivo:  # Abre el archivo en modo lectura
            return json.load(archivo)  # Carga y retorna los datos JSON del archivo
    except FileNotFoundError:
        return []  # Retorna una lista vacía si no encuentra el archivo
    except json.JSONDecodeError:
        return []  # Retorna una lista vacía si hay un error

def guardar_datos(ruta_relativa, datos):
    # Función para guardar datos en un archivo JSON dado su ruta relativa
    ruta_absoluta = os.path.join(BASE_DIR, ruta_relativa)  # Convierte la ruta relativa en una ruta absoluta
    with open(ruta_absoluta, 'w') as archivo:  # Abre el archivo en modo escritura
        json.dump(datos, archivo, indent=4)  # Guarda los datos en formato JSON con una indentación de 4 espacios

def inicializar_datos():     # Función para inicializar y cargar los datos de libros, socios y préstamos
    libros = cargar_datos('data/libros.json')  # Carga los datos de libros desde el archivo JSON
    socios = cargar_datos('data/socios.json')  # Carga los datos de socios desde el archivo JSON
    prestamos = cargar_datos('data/prestamos.json')  # Carga los datos de préstamos desde el archivo JSON
    return libros, socios, prestamos  # Retorna los datos cargados como una tupla