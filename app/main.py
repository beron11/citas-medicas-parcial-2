from hospital import Hospital
from persona_factory import PersonasFactory
from rich.console import Console
from rich.table import Table

console = Console()

hospital = Hospital()

def desplegar_menu():
    console.print("\n[bold purple]=== Menú Principal ===[/bold purple]")
    console.print("1. Registrar persona")
    console.print("2. Agendar una cita")
    console.print("3. Anular cita")
    console.print("4. Asignar médico preferido")
    console.print("5. Consultar citas pendientes")
    console.print("6. Cambiar la fecha de una cita")
    console.print("7. Actualizar información del paciente")
    console.print("8. Actualizar información del médico")
    console.print("9. Finalizar")

while True:
    desplegar_menu()
    eleccion = console.input("[bold yellow]Elige una opción: [/bold yellow]")

    if eleccion == "1":
        tipo = console.input("¿Es médico o paciente? ([bright_blue]médico[/bright_blue] o [bright_blue]paciente[/bright_blue]): ").lower()
        id_persona = console.input("Introduce el número de identificación: ")
        nombre = console.input("Introduce el nombre: ")
        telefono = console.input("Introduce el teléfono: ")

        if tipo == "medico":
            especialidad = console.input("Especifica la especialidad del médico: ")
            persona = PersonasFactory.crear_persona("medico", id_persona, nombre, telefono, especialidad)
            hospital.registrar_medico(persona)
            console.print(f"[bright_green]El médico {nombre} ha sido añadido.[/bright_green]")
        elif tipo == "paciente":
            correo = console.input("Introduce el correo electrónico: ")
            persona = PersonasFactory.crear_persona("paciente", id_persona, nombre, telefono, correo=correo)
            hospital.registrar_paciente(persona)
            console.print(f"[bright_green]El paciente {nombre} ha sido añadido.[/bright_green]")
        else:
            console.print("[red]Error: tipo de persona no válido.[/red]")

    elif eleccion == "2":
        id_paciente = console.input("Introduce la identificación del paciente: ")
        especialidad = console.input("Especifica la especialidad requerida: ")
        fecha = console.input("Introduce la fecha y hora de la cita (YYYY-MM-DD HH:MM): ")

        paciente = hospital.buscar_paciente(id_paciente)
        if paciente:
            lista_medicos = hospital.obtener_medicos_por_especialidad(especialidad)
            if lista_medicos:
                console.print("[cyan]Médicos disponibles:[/cyan]")
                table = Table(title="[bold cyan]Opciones de médicos[/bold cyan]")
                table.add_column("No.", justify="right")
                table.add_column("Nombre", style="bright_magenta")
                table.add_column("Especialidad", style="green")

                for i, medico in enumerate(lista_medicos):
                    table.add_row(str(i + 1), medico.nombre, medico.especialidad)

                console.print(table)
                seleccion_medico = int(console.input("[bold magenta]Elige el médico (número): [/bold magenta]")) - 1
                if 0 <= seleccion_medico < len(lista_medicos):
                    medico_seleccionado = lista_medicos[seleccion_medico]
                    paciente.agendar_cita(medico_seleccionado, fecha)
                else:
                    console.print("[bright_red]Opción inválida.[/bright_red]")
            else:
                console.print("[bright_red]No se encontraron médicos disponibles.[/bright_red]")
        else:
            console.print("[bright_red]El paciente no existe.[/bright_red]")

    elif eleccion == "3":
        id_paciente = console.input("Introduce la identificación del paciente: ")
        paciente = hospital.buscar_paciente(id_paciente)

        if paciente:
            citas = [cita for cita in hospital.citas if cita.paciente == paciente]

            if citas:
                console.print("[bold bright_blue]Citas actuales:[/bold bright_blue]")
                table = Table(title="[bright_blue]Citas Activas[/bright_blue]")
                table.add_column("No.", justify="right")
                table.add_column("Fecha", style="bright_yellow")
                table.add_column("Médico", style="bright_green")

                for i, cita in enumerate(citas):
                    table.add_row(str(i + 1), cita.fecha, cita.medico.nombre)

                console.print(table)
                seleccion_cita = int(console.input("[bright_magenta]Selecciona la cita a cancelar (número): [/bright_magenta]")) - 1
                if 0 <= seleccion_cita < len(citas):
                    cita_seleccionada = citas[seleccion_cita]
                    hospital.anular_cita(paciente.id_persona, cita_seleccionada.fecha)
                else:
                    console.print("[bright_red]Número de cita inválido.[/bright_red]")
            else:
                console.print("[bright_red]No tienes citas pendientes.[/bright_red]")
        else:
            console.print("[bright_red]Paciente no encontrado.[/bright_red]")

    elif eleccion == "4":
        id_paciente = console.input("Introduce la identificación del paciente: ")
        id_medico = console.input("Introduce la identificación del médico: ")

        paciente = hospital.buscar_paciente(id_paciente)
        medico = hospital.buscar_medico(id_medico)

        if paciente and medico:
            paciente.asignar_medico_preferido(medico)
        else:
            console.print("[bright_red]No se encontró el paciente o el médico.[/bright_red]")

    elif eleccion == "5":
        id_paciente = console.input("Introduce la identificación del paciente: ")
        paciente = hospital.buscar_paciente(id_paciente)

        if paciente:
            citas_pendientes = [cita for cita in hospital.citas if cita.paciente == paciente]

            if citas_pendientes:
                table = Table(title="[bold green]Citas Pendientes[/bold green]")
                table.add_column("No.", justify="right")
                table.add_column("Fecha", style="bright_yellow")
                table.add_column("Médico", style="bright_cyan")

                for i, cita in enumerate(citas_pendientes):
                    table.add_row(str(i + 1), cita.fecha, cita.medico.nombre)

                console.print(table)
            else:
                console.print("[bright_red]No tienes citas pendientes.[/bright_red]")
        else:
            console.print("[bright_red]Paciente no encontrado.[/bright_red]")

    elif eleccion == "6":
        id_paciente = console.input("Introduce la identificación del paciente: ")
        fecha_actual = console.input("Introduce la fecha actual de la cita (YYYY-MM-DD HH:MM): ")
        nueva_fecha = console.input("Introduce la nueva fecha (YYYY-MM-DD HH:MM): ")

        hospital.reprogramar_cita(id_paciente, fecha_actual, nueva_fecha)

    elif eleccion == "7":
        id_paciente = console.input("Introduce la identificación del paciente: ")
        nuevo_nombre = console.input("Introduce el nuevo nombre (dejar en blanco para no cambiar): ")
        nuevo_telefono = console.input("Introduce el nuevo teléfono (dejar en blanco para no cambiar): ")
        nuevo_correo = console.input("Introduce el nuevo correo (dejar en blanco para no cambiar): ")

        hospital.modificar_paciente(id_paciente, nuevo_nombre, nuevo_telefono, nuevo_correo)

    elif eleccion == "8":
        id_medico = console.input("Introduce la identificación del médico: ")
        nuevo_nombre = console.input("Introduce el nuevo nombre (dejar en blanco para no cambiar): ")
        nuevo_telefono = console.input("Introduce el nuevo teléfono (dejar en blanco para no cambiar): ")
        nueva_especialidad = console.input("Introduce la nueva especialidad (dejar en blanco para no cambiar): ")

        hospital.modificar_medico(id_medico, nuevo_nombre, nuevo_telefono, nueva_especialidad)

    elif eleccion == "9":
        console.print("[bold bright_green]Finalizando programa...[/bold bright_green]")
        break

    else:
        console.print("[bright_red]Opción no válida. Intenta nuevamente.[/bright_red]")
