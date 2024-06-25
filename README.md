# Trabajo Final Integrador de Programación 1

## Sistema de Gestión de Bibliotecas #Python

Este proyecto es mi trabajo final integrador del primer semestre de Programación 1 en la Tecnicatura Universitaria en Desarrollo Web (UNER)

Elegí desarrollar una solución de software para gestionar el préstamo y devolución de libros en una biblioteca utilizando Python en Visual Studio Code

### Requerimientos del Trabajo Final Integrador TUDW 2024:

1. **Registro de Libros:**
   - ID de Libro (número único y autoincremental)
   - Título
   - Autor
   - Editorial
   - Año de Publicación
   - Género
   - Cantidad Disponible

2. **Gestión de Socios:**
   - ID de Socio (número único y autoincremental)
   - Nombre
   - Apellido
   - Fecha de Nacimiento
   - Dirección
   - Correo Electrónico
   - Teléfono

3. **Registro de Préstamos y Devoluciones:**
   - ID de Préstamo (número único y autoincremental)
   - ID de Socio
   - ID de Libro
   - Fecha de Préstamo
   - Costo (en caso de que lo hubiera)
   - Fecha de Devolución
   - Estado del Préstamo (En Curso/Devuelto)

### Características del Software

- **Almacenamiento de Información:** Utilización de archivos JSON para almacenar los datos solicitados.
- **Interfaces de Usuario Interactivas que Permiten:** 
  - Registrar, editar y eliminar libros.
  - Registrar, editar y eliminar socios.
  - Registrar préstamos y devoluciones.
  - Generar reportes de préstamos y devoluciones por socio, libro y rango de fechas.

### Funcionalidad Extra

Como parte del trabajo final, se incluye una funcionalidad extra del software a criterio del alumno/grupo. Esto puede incluir el desarrollo de una interfaz gráfica, consumo de una API externa, implementación de búsquedas avanzadas, o cualquier otra funcionalidad que aporte valor agregado al sistema
- Funcionalidad elegida: Nueva opción en el menú -> Eliminar todos los libros.

Esta opción le permite al usuario borrar todos los libros de la lista de una sola vez y volver a empezar más rápido por si no quiere borrar los libros de a uno

## Uso del Sistema
Para ejecutar el sistema en tu PC, seguí estos pasos:

1. Cloná el repositorio desde GitHub o GitHub Desktop
2. Abrí la carpeta del repositorio en tu Visual Studio Code o IDE de preferencia
3. Abrí una Terminal en el IDE
4. Escribí el siguiente comando y darle Enter:
```bash
   python main.py