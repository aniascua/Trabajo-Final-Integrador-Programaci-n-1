class Prestamo:
    def __init__(self, id_prestamo, id_libro, id_socio, fecha_prestamo, fecha_devolucion=None, estado_prestamo="En Curso"):
        self.id_prestamo = id_prestamo
        self.id_libro = id_libro
        self.id_socio = id_socio
        self.fecha_prestamo = fecha_prestamo
        self.fecha_devolucion = fecha_devolucion
        self.estado_prestamo = estado_prestamo

    def to_dict(self):
        return {
            'id_prestamo': self.id_prestamo,
            'id_libro': self.id_libro,
            'id_socio': self.id_socio,
            'fecha_prestamo': self.fecha_prestamo,
            'fecha_devolucion': self.fecha_devolucion,
            'estado_prestamo': self.estado_prestamo
        }