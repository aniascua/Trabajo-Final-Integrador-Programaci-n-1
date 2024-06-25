class Libro:
    def __init__(self, id_libro, titulo, autor, editorial, anio_publicacion, genero, cantidad_disponible):
        self.id_libro = id_libro
        self.titulo = titulo
        self.autor = autor
        self.editorial = editorial
        self.anio_publicacion = anio_publicacion
        self.genero = genero
        self.cantidad_disponible = cantidad_disponible

    def to_dict(self):
        return {
            'id_libro': self.id_libro,
            'titulo': self.titulo,
            'autor': self.autor,
            'editorial': self.editorial,
            'año_publicacion': self.anio_publicacion,
            'genero': self.genero,
            'cantidad_disponible': self.cantidad_disponible
        }