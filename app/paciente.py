from persona import Persona
from cita import Cita

class Paciente(Persona):
    def __init__(self, id_persona, nombre, telefono, email):
        super().__init__(id_persona, nombre, telefono, email)
        self.medico_preferido = None

    def asignar_medico(self, medico):
        self.medico_preferido = medico
        print(f"Se ha asignado al Dr. {medico.nombre} como médico preferido para {self.nombre}.")

    def solicitar_cita(self, medico, fecha):
        if medico.es_disponible(fecha):
            nueva_cita = Cita(self, medico, fecha)
            medico.agregar_cita(nueva_cita)
            print(f"Cita agendada para el {fecha} con el Dr. {medico.nombre}.")
        else:
            print(f"El Dr. {medico.nombre} no tiene disponibilidad en la fecha {fecha}.")
