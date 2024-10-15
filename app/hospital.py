from medico import Medico
from paciente import Paciente
from cita import Cita

class Hospital:
    def __init__(self):
        self.medicos = []
        self.pacientes = []
        self.citas = []

    def agregar_medico(self, medico):
        self.medicos.append(medico)

    def agregar_paciente(self, paciente):
        self.pacientes.append(paciente)

    def encontrar_medico(self, id_persona):
        for medico in self.medicos:
            if medico.id_persona == id_persona:
                return medico
        return None

    def encontrar_paciente(self, id_persona):
        for paciente in self.pacientes:
            if paciente.id_persona == id_persona:
                return paciente
        return None

    def listar_medicos_por_especialidad(self, especialidad):
        return [medico for medico in self.medicos if medico.especialidad == especialidad]

    def cancelar_cita(self, id_paciente, fecha):
        for cita in self.citas:
            if cita.paciente.id_persona == id_paciente and cita.fecha == fecha:
                self.citas.remove(cita)
                print(f"Cita cancelada para el paciente {id_paciente}.")
                return
        print("No se encontró la cita.")

    def reprogramar_cita(self, id_paciente, fecha_actual, nueva_fecha):
        for cita in self.citas:
            if cita.paciente.id_persona == id_paciente and cita.fecha == fecha_actual:
                cita.fecha = nueva_fecha
                print(f"Cita reprogramada para el paciente {id_paciente} a {nueva_fecha}.")
                return
        print("No se encontró la cita para reprogramar.")

