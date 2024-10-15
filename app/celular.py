class Celular:
    def verificar_celular(self, numero_celular):
        print(f"Enviando mensaje de verificación a {numero_celular}")

    def enviar_mensaje(self, numero_celular, mensaje):
        print(
            f"Enviando mensaje de texto para {numero_celular}, con contenido: {mensaje}")

    def realizar_llamada(self, numero_celular):
        print(f"Realizando llamada telefónica a {numero_celular}")
