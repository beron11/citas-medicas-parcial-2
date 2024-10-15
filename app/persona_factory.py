from medico import Medico
from paciente import Paciente

class PersonasFactory:
    @staticmethod
    def crear_persona(tipo, id_persona, nombre, telefono, especialidad=None, email=None):
        if tipo.lower() == 'medico':
            return Medico(id_persona, nombre, telefono, especialidad)
        elif tipo.lower() == 'paciente':
            return Paciente(id_persona, nombre, telefono, email)
        else:
            raise ValueError(f"Tipo de persona desconocido: {tipo}")
