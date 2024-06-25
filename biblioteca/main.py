# TRABAJO FINAL INTEGRADOR PROGRAMACIÓN 1
# ALUMNA: ASCUA, ANA
# TEMA ELEGIDO: SISTEMA DE GESTIÓN DE BIBLIOTECAS EN PYTHON.

# IMPORTAMOS LAS FUNCIONES Y CLASES NECESARIAS
from utils import cargar_datos, guardar_datos, inicializar_datos  # Funciones para manejar archivos JSON e inicializar datos
from libro import Libro  # Clase para representar libros
from socio import Socio  # Clase para representar socios
from prestamo import Prestamo  # Clase para representar préstamos

# DEFINIMOS LAS RUTAS DE LOS ARCHIVOS JSON
DATA_PATH_LIBROS = 'libros.json'
DATA_PATH_SOCIOS = 'socios.json'
DATA_PATH_PRESTAMOS = 'prestamos.json'

def obtener_siguiente_id_libro():
    libros = cargar_datos(DATA_PATH_LIBROS)
    if libros:
        return max(libro['id_libro'] for libro in libros) + 1
    else:
        return 1  # Si no hay libros registrados, empezamos desde el ID 1

# MENÚ PRINCIPAL
def mostrar_menu():
    """FUNCIÓN PARA MOSTRAR EL MENÚ PRINCIPAL"""
    print("\n*** Sistema de Gestión de Biblioteca ***")
    print("1. Registrar Libro")
    print("2. Editar Libro")
    print("3. Eliminar Libro")
    print("4. Registrar Socio")
    print("5. Editar Socio")
    print("6. Eliminar Socio")
    print("7. Registrar Préstamo")
    print("8. Devolver Libro")
    print("9. Listar Libros")
    print("10. Listar Socios")
    print("11. Buscar Libro por Título")
    print("12. Buscar Libro por Género")
    print("13. Buscar Libro por Autor")
    print("14. Buscar Libro por Editorial")
    print("15. **EXTRA** Eliminar todos los libros")  # FUNCIONALIDAD EXTRA PARA BORRAR TODOS LOS LIBROS
    print("16. Salir...")

# 1. Registrar Libro
def registrar_libro():
    titulo = input("Título: ")
    autor = input("Autor: ")
    editorial = input("Editorial: ")
    anio_publicacion = int(input("Año de publicación: "))
    genero = input("Género: ")
    cantidad_disponible = int(input("Cantidad disponible: "))

    id_libro = obtener_siguiente_id_libro()  # Obtener el siguiente ID disponible

    libro = Libro(id_libro, titulo, autor, editorial, anio_publicacion, genero, cantidad_disponible)
    
    libros = cargar_datos(DATA_PATH_LIBROS)
    libros.append(libro.to_dict())
    guardar_datos(DATA_PATH_LIBROS, libros)

    print("Libro registrado exitosamente!")

# 2. Editar Libro
def editar_libro():
    """FUNCIÓN PARA EDITAR UN LIBRO EXISTENTE EN EL SISTEMA"""
    id_libro = int(input("ID del libro a editar: "))
    libros = cargar_datos(DATA_PATH_LIBROS)
    libro_encontrado = False

    for libro in libros:
        if libro['id_libro'] == id_libro:
            libro['titulo'] = input(f"Título ({libro['titulo']}): ") or libro['titulo']
            libro['autor'] = input(f"Autor ({libro['autor']}): ") or libro['autor']
            libro['editorial'] = input(f"Editorial ({libro['editorial']}): ") or libro['editorial']
            libro['anio_publicacion'] = int(input(f"Año de publicación ({libro['anio_publicacion']}): ") or libro['anio_publicacion'])
            libro['genero'] = input(f"Género ({libro['genero']}): ") or libro['genero']
            libro['cantidad_disponible'] = int(input(f"Cantidad disponible ({libro['cantidad_disponible']}): ") or libro['cantidad_disponible'])
            libro_encontrado = True
            break

    if libro_encontrado:
        guardar_datos(DATA_PATH_LIBROS, libros)
        print("Libro editado exitosamente!")
    else:
        print("Libro no encontrado...")

# 3. Eliminar Libro
def eliminar_libro():
    """FUNCIÓN PARA ELIMINAR UN LIBRO DEL SISTEMA"""
    id_libro = int(input("ID del libro a eliminar: "))
    libros = cargar_datos(DATA_PATH_LIBROS)
    
    libros = [libro for libro in libros if libro['id_libro'] != id_libro]
    
    guardar_datos(DATA_PATH_LIBROS, libros)
    print("Libro eliminado exitosamente!")

# 4. Registrar Socio
def registrar_socio():
    """FUNCIÓN PARA REGISTRAR UN NUEVO SOCIO EN EL SISTEMA"""
    nombre = input("Nombre: ")
    apellido = input("Apellido: ")
    fecha_nacimiento = input("Fecha de nacimiento (yyyy-mm-dd): ")
    direccion = input("Dirección: ")
    correo_electronico = input("Correo electrónico: ")
    telefono = input("Teléfono: ")

    socios = cargar_datos(DATA_PATH_SOCIOS)
    Socio.actualizar_contador(socios)

    socio = Socio(nombre, apellido, fecha_nacimiento, direccion, correo_electronico, telefono)
    socios.append(socio.to_dict())
    guardar_datos(DATA_PATH_SOCIOS, socios)
    
    print("Socio registrado exitosamente!")

# 5. Editar Socio
def editar_socio():
    """FUNCIÓN PARA EDITAR UN SOCIO EXISTENTE EN EL SISTEMA"""
    id_socio = input("ID del socio a editar: ")
    socios = cargar_datos(DATA_PATH_SOCIOS)
    
    socio_encontrado = False

    for socio in socios:
        if socio['id_socio'] == id_socio:
            socio['nombre'] = input(f"Nombre ({socio['nombre']}): ") or socio['nombre']
            socio['apellido'] = input(f"Apellido ({socio['apellido']}): ") or socio['apellido']
            socio['fecha_nacimiento'] = input(f"Fecha de nacimiento ({socio['fecha_nacimiento']}): ") or socio['fecha_nacimiento']
            socio['direccion'] = input(f"Dirección ({socio['direccion']}): ") or socio['direccion']
            socio['correo_electronico'] = input(f"Correo electrónico ({socio['correo_electronico']}): ") or socio['correo_electronico']
            socio['telefono'] = input(f"Teléfono ({socio['telefono']}): ") or socio['telefono']
            socio_encontrado = True
            break

    if socio_encontrado:
        guardar_datos(DATA_PATH_SOCIOS, socios)
        print("Socio editado exitosamente!")
    else:
        print("Socio no encontrado.")

# 6. Eliminar Socio
def eliminar_socio():
    """FUNCIÓN PARA ELIMINAR UN SOCIO DEL SISTEMA"""
    listar_socios()  # Mostrar la lista de socios para que el usuario seleccione uno
    id_socio_a_eliminar = input("Ingrese el ID del socio a eliminar: ")

    socios = cargar_datos(DATA_PATH_SOCIOS)
    socios_actualizados = [socio for socio in socios if socio['id_socio'] != id_socio_a_eliminar]
    
    guardar_datos(DATA_PATH_SOCIOS, socios_actualizados)
    
    print(f"Socio con ID {id_socio_a_eliminar} eliminado correctamente!")

# 7. Registrar Préstamo
def registrar_prestamo():
    """FUNCIÓN PARA REGISTRAR UN NUEVO PRÉSTAMO EN EL SISTEMA"""
    id_libro = int(input("ID del libro: "))
    id_socio = input("ID del socio: ")
    fecha_prestamo = input("Fecha de préstamo (yyyy-mm-dd): ")
    estado_prestamo = "En Curso" 

    # Creamos una instancia de Prestamo
    prestamo = Prestamo(id_prestamo=None, id_libro=id_libro, id_socio=id_socio,
                        fecha_prestamo=fecha_prestamo, estado_prestamo=estado_prestamo)

    # Guardamos el préstamo en la lista de préstamos
    prestamos = cargar_datos(DATA_PATH_PRESTAMOS)
    prestamos.append(prestamo.to_dict())
    guardar_datos(DATA_PATH_PRESTAMOS, prestamos)

    # Actualizamos la cantidad disponible del libro prestado
    libros = cargar_datos(DATA_PATH_LIBROS)
    libro_encontrado = False

    for libro in libros:
        if libro['id_libro'] == id_libro:
            if libro['cantidad_disponible'] > 0:
                libro['cantidad_disponible'] -= 1
                guardar_datos(DATA_PATH_LIBROS, libros)
                print("Préstamo registrado exitosamente!")
                libro_encontrado = True
            else:
                print("No hay copias disponibles para préstamo...")
            break

    if not libro_encontrado:
        print("Libro no encontrado...")

# 8. Devolver Libro
def devolver_libro():
    """FUNCIÓN PARA REGISTRAR LA DEVOLUCIÓN DE UN LIBRO"""
    id_prestamo = input("ID del préstamo: ")
    fecha_devolucion = input("Fecha de devolución (yyyy-mm-dd): ")

    prestamos = cargar_datos(DATA_PATH_PRESTAMOS)
    prestamo_encontrado = False

    for prestamo in prestamos:
        if str(prestamo['id_prestamo']) == id_prestamo:
            prestamo['fecha_devolucion'] = fecha_devolucion
            prestamo['estado_prestamo'] = "Devuelto"
            guardar_datos(DATA_PATH_PRESTAMOS, prestamos)

            id_libro = prestamo['id_libro']
            libros = cargar_datos(DATA_PATH_LIBROS)
            for libro in libros:
                if libro['id_libro'] == id_libro:
                    libro['cantidad_disponible'] += 1
                    guardar_datos(DATA_PATH_LIBROS, libros)
                    break

            print("Libro devuelto exitosamente.")
            prestamo_encontrado = True
            break

    if not prestamo_encontrado:
        print("Préstamo no encontrado...")

# 9. Listar Libros
def listar_libros():
    """FUNCIÓN PARA LISTAR TODOS LOS LIBROS DISPONIBLES EN EL SISTEMA"""
    libros = cargar_datos(DATA_PATH_LIBROS)
    if libros:
        for libro in libros:
            id_libro = libro.get('id_libro', 'Desconocido')
            titulo = libro.get('titulo', 'Desconocido')
            autor = libro.get('autor', 'Desconocido')
            editorial = libro.get('editorial', 'Desconocido')
            anio_publicacion = libro.get('anio_publicacion', 'Desconocido') 
            genero = libro.get('genero', 'Desconocido')
            cantidad_disponible = libro.get('cantidad_disponible', 'Desconocido')

            print(f"ID: {id_libro}, Título: {titulo}, Autor: {autor}, Editorial: {editorial}, Año: {anio_publicacion}, Género: {genero}, Disponible: {cantidad_disponible}")
    else:
        print("No hay libros registrados...")

# 10. Listar Socios
def listar_socios():
    """FUNCIÓN PARA LISTAR TODOS LOS SOCIOS REGISTRADOS EN EL SISTEMA"""
    socios = cargar_datos(DATA_PATH_SOCIOS)
    if socios:
        for socio in socios:
            print(f"ID: {socio['id_socio']}, Nombre: {socio['nombre']}, Apellido: {socio['apellido']}, Fecha de nacimiento: {socio['fecha_nacimiento']}, Dirección: {socio['direccion']}, Correo electrónico: {socio['correo_electronico']}, Teléfono: {socio['telefono']}")
    else:
        print("No hay socios registrados...")

# 11. Buscar Libro por Título
def buscar_libro_titulo():
    """FUNCIÓN PARA BUSCAR UN LIBRO POR TÍTULO"""
    titulo_buscado = input("Ingrese el título del libro a buscar: ").strip().lower()

    libros = cargar_datos(DATA_PATH_LIBROS)
    libros_encontrados = []

    for libro in libros:
        if titulo_buscado in libro['titulo'].strip().lower():
            libros_encontrados.append(libro)

    if libros_encontrados:
        for libro in libros_encontrados:
            # Claves necesarias 
            id_libro = libro.get('id_libro', 'Desconocido')
            titulo = libro.get('titulo', 'Desconocido')
            autor = libro.get('autor', 'Desconocido')
            editorial = libro.get('editorial', 'Desconocido')
            anio_publicacion = libro.get('anio_publicacion', 'Desconocido')
            genero = libro.get('genero', 'Desconocido')
            cantidad_disponible = libro.get('cantidad_disponible', 'Desconocido')

            print(f"ID: {id_libro}, Título: {titulo}, Autor: {autor}, Editorial: {editorial}, Año: {anio_publicacion}, Género: {genero}, Disponible: {cantidad_disponible}")
    else:
        print(f"No se encontró ningún libro con el título '{titulo_buscado}'.")

# 12. Buscar Libro por género
def buscar_libro_genero():
    """FUNCIÓN PARA BUSCAR LIBROS POR GÉNERO"""
    genero_buscado = input("Ingrese el género del libro a buscar: ").strip().lower()

    libros = cargar_datos(DATA_PATH_LIBROS)
    libros_encontrados = []

    for libro in libros:
        if genero_buscado in libro['genero'].strip().lower():
            libros_encontrados.append(libro)

    if libros_encontrados:
        for libro in libros_encontrados:
            # Claves necesarias en el diccionario del libro
            id_libro = libro.get('id_libro', 'Desconocido')
            titulo = libro.get('titulo', 'Desconocido')
            autor = libro.get('autor', 'Desconocido')
            editorial = libro.get('editorial', 'Desconocido')
            anio_publicacion = libro.get('anio_publicacion', 'Desconocido')
            genero = libro.get('genero', 'Desconocido')
            cantidad_disponible = libro.get('cantidad_disponible', 'Desconocido')

            print(f"ID: {id_libro}, Título: {titulo}, Autor: {autor}, Editorial: {editorial}, Año: {anio_publicacion}, Género: {genero}, Disponible: {cantidad_disponible}")
    else:
        print(f"No se encontraron libros con el género '{genero_buscado}'.")

# 13. Buscar Libro por Autor
def buscar_libro_autor():
    """FUNCIÓN PARA BUSCAR LIBROS POR AUTOR"""
    autor_buscado = input("Ingrese el autor del libro a buscar: ").strip().lower()

    libros = cargar_datos(DATA_PATH_LIBROS)
    libros_encontrados = []

    for libro in libros:
        if autor_buscado in libro['autor'].strip().lower():
            libros_encontrados.append(libro)

    if libros_encontrados:
        for libro in libros_encontrados:
            id_libro = libro.get('id_libro', 'Desconocido')
            titulo = libro.get('titulo', 'Desconocido')
            autor = libro.get('autor', 'Desconocido')
            editorial = libro.get('editorial', 'Desconocido')
            anio_publicacion = libro.get('anio_publicacion', 'Desconocido')
            genero = libro.get('genero', 'Desconocido')
            cantidad_disponible = libro.get('cantidad_disponible', 'Desconocido')

            print(f"ID: {id_libro}, Título: {titulo}, Autor: {autor}, Editorial: {editorial}, Año: {anio_publicacion}, Género: {genero}, Disponible: {cantidad_disponible}")
    else:
        print(f"No se encontraron libros del autor '{autor_buscado}'.")

# 14. Buscar Libro por Editorial
def buscar_libro_editorial():
    """FUNCIÓN PARA BUSCAR LIBROS POR EDITORIAL"""
    editorial_buscada = input("Ingrese la editorial del libro a buscar: ").strip().lower()

    libros = cargar_datos(DATA_PATH_LIBROS)
    libros_encontrados = []

    for libro in libros:
        if editorial_buscada in libro['editorial'].strip().lower():
            libros_encontrados.append(libro)

    if libros_encontrados:
        for libro in libros_encontrados:
            id_libro = libro.get('id_libro', 'Desconocido')
            titulo = libro.get('titulo', 'Desconocido')
            autor = libro.get('autor', 'Desconocido')
            editorial = libro.get('editorial', 'Desconocido')
            anio_publicacion = libro.get('anio_publicacion', 'Desconocido')
            genero = libro.get('genero', 'Desconocido')
            cantidad_disponible = libro.get('cantidad_disponible', 'Desconocido')

            print(f"ID: {id_libro}, Título: {titulo}, Autor: {autor}, Editorial: {editorial}, Año: {anio_publicacion}, Género: {genero}, Disponible: {cantidad_disponible}")
    else:
        print(f"No se encontraron libros de la editorial '{editorial_buscada}'.")

# 15. Eliminar Todos los Libros
def eliminar_todos_libros():
    """FUNCIÓN PARA ELIMINAR TODOS LOS LIBROS DEL SISTEMA"""
    libros = []
    guardar_datos(DATA_PATH_LIBROS, libros)
    print("Todos los libros fueron eliminados del sistema...")

# FUNCION PRINCIPAL
def main():
    """FUNCIÓN PRINCIPAL DEL PROGRAMA"""
    inicializar_datos()  # Inicializamos los datos si es necesario
    
    while True:
        mostrar_menu()  # Mostramos el menú principal
        opcion = input("Selecciona una opción: ")

        if opcion == '1':
            registrar_libro()
        elif opcion == '2':
            editar_libro()
        elif opcion == '3':
            eliminar_libro()
        elif opcion == '4':
            registrar_socio()
        elif opcion == '5':
            editar_socio()
        elif opcion == '6':
            eliminar_socio()
        elif opcion == '7':
            registrar_prestamo()
        elif opcion == '8':
            devolver_libro()
        elif opcion == '9':
            listar_libros()
        elif opcion == '10':
            listar_socios()
        elif opcion == '11':
            buscar_libro_titulo()
        elif opcion == '12':
            buscar_libro_genero()
        elif opcion == '13':
            buscar_libro_autor()
        elif opcion == '14':
            buscar_libro_editorial()
        elif opcion == '15':
            eliminar_todos_libros()
        elif opcion == '16':
            print("Saliendo del sistema... Gracias!")
            break
        else:
            print("Opción no válida. Inténtalo nuevamente.")

if __name__ == "__main__":
    main()