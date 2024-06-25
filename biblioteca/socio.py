# socio.py

class Socio:
    contador_id = 0

    @classmethod
    def actualizar_contador(cls, socios):
        if socios:
            ids = [int(socio['id_socio']) for socio in socios]
            cls.contador_id = max(ids)
        else:
            cls.contador_id = 0

    def __init__(self, nombre, apellido, fecha_nacimiento, direccion, correo_electronico, telefono):
        Socio.contador_id += 1
        self.id_socio = str(Socio.contador_id)
        self.nombre = nombre
        self.apellido = apellido
        self.fecha_nacimiento = fecha_nacimiento
        self.direccion = direccion
        self.correo_electronico = correo_electronico
        self.telefono = telefono

    def to_dict(self):
        return {
            'id_socio': self.id_socio,
            'nombre': self.nombre,
            'apellido': self.apellido,
            'fecha_nacimiento': self.fecha_nacimiento,
            'direccion': self.direccion,
            'correo_electronico': self.correo_electronico,
            'telefono': self.telefono
        }
