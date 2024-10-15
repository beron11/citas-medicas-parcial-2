class Reporte:
    def __init__(self, tipo_reporte, inicio, fin):
        self.tipo_reporte = tipo_reporte
        self.inicio = inicio
        self.fin = fin

    def generar(self):
        pass

    def exportar_a_excel(self):
        print(f"Exportando el reporte {self.tipo_reporte} a un archivo de Excel.")

class ReporteDemanda(Reporte):
    def __init__(self, tipo_reporte, inicio, fin, medico):
        super().__init__(tipo_reporte, inicio, fin)
        self.medico = medico

    def generar(self):
        print(f"Creando el reporte de demanda para el Dr. {self.medico.nombre}.")

class ReporteTendencias(Reporte):
    def __init__(self, tipo_reporte, inicio, fin, citas_agendadas):
        super().__init__(tipo_reporte, inicio, fin)
        self.citas_agendadas = citas_agendadas

    def generar(self):
        print("Creando el reporte de tendencias...")

class ReporteCancelaciones(Reporte):
    def __init__(self, tipo_reporte, inicio, fin, motivo):
        super().__init__(tipo_reporte, inicio, fin)
        self.motivo = motivo

    def generar(self):
        print(f"Creando el reporte de cancelaciones por el motivo: {self.motivo}")

class ReporteAusentismo(Reporte):
    def __init__(self, tipo_reporte, inicio, fin, citas_ausentes):
        super().__init__(tipo_reporte, inicio, fin)
        self.citas_ausentes = citas_ausentes

    def generar(self):
        print("Creando el reporte de ausentismo...")
