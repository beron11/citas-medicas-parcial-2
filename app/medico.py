from persona import Persona

class Medico(Persona):
    def __init__(self, id_persona, nombre, telefono, especialidad):
        super().__init__(id_persona, nombre, telefono)
        self.especialidad = especialidad
        self.lista_citas = []

    def es_disponible(self, fecha):
        # Lógica para verificar disponibilidad
        return True

    def agregar_cita(self, cita):
        self.lista_citas.append(cita)
