from hospital import Hospital
from persona_factory import PersonasFactory
from rich.console import Console
from rich.table import Table

console = Console()

hospital = Hospital()

ddef mostrar_menu():
    console.print("\n[bold green]--- Menú ---[/bold green]")
    console.print("1. Agregar persona")
    console.print("2. Solicitar cita")
    console.print("3. Cancelar cita")
    console.print("4. Establecer médico de preferencia")
    console.print("5. Listar citas pendientes")
    console.print("6. Buscar citas por fecha")
    console.print("7. Generar reporte de médicos por especialidad")
    console.print("8. Ver historial de citas de un paciente")
    console.print("9. Salir")

while True:
    mostrar_menu()
    opcion = console.input("[bold blue]Seleccione una opción: [/bold blue]")

    if opcion == "1":
        tipo_persona = console.input("Ingrese el tipo de persona ([cyan]médico[/cyan] o [cyan]paciente[/cyan]): ").lower()
        id_persona = console.input("Ingrese la identificación: ")
        nombre = console.input("Ingrese el nombre: ")
        telefono = console.input("Ingrese el teléfono: ")

        if tipo_persona == "medico":
            especialidad = console.input("Ingrese la especialidad: ")
            persona = PersonasFactory.crear_persona("medico", id_persona, nombre, telefono, especialidad)
            hospital.agregar_medico(persona)
            console.print(f"[green]Médico {nombre} agregado exitosamente.[/green]")
        elif tipo_persona == "paciente":
            email = console.input("Ingrese el correo: ")
            persona = PersonasFactory.crear_persona("paciente", id_persona, nombre, telefono, email=email)
            hospital.agregar_paciente(persona)
            console.print(f"[green]Paciente {nombre} agregado exitosamente.[/green]")
        else:
            console.print("[red]Tipo de persona no válido.[/red]")

    elif opcion == "2":  # Solicitar cita
        id_paciente = console.input("Ingrese la identificación del paciente: ")
        especialidad = console.input("Ingrese la especialidad requerida: ")
        fecha = console.input("Ingrese la fecha y hora de la cita (YYYY-MM-DD HH:MM): ")

        paciente = hospital.encontrar_paciente(id_paciente)
        if paciente:
            medicos_disponibles = hospital.listar_medicos_por_especialidad(especialidad)
            if medicos_disponibles:
                console.print("Médicos disponibles:")
                table = Table(title="Médicos Disponibles")
                table.add_column("No.", justify="right")
                table.add_column("Nombre", style="cyan")
                table.add_column("Especialidad", style="magenta")

                for i, medico in enumerate(medicos_disponibles):
                    table.add_row(str(i + 1), medico.nombre, medico.especialidad)

                console.print(table)
                opcion_medico = int(console.input("Seleccione el médico (número): ")) - 1
                if 0 <= opcion_medico < len(medicos_disponibles):
                    medico_seleccionado = medicos_disponibles[opcion_medico]
                    paciente.solicitar_cita(medico_seleccionado, fecha)
                else:
                    console.print("[red]Opción de médico no válida.[/red]")
            else:
                console.print("[red]No hay médicos disponibles para esa especialidad.[/red]")
        else:
            console.print("[red]Paciente no encontrado.[/red]")

    elif opcion == "3":  # Cancelar cita
        id_paciente = console.input("Ingrese la identificación del paciente: ")
        paciente = hospital.encontrar_paciente(id_paciente)

        if paciente:
            citas_pendientes = [cita for cita in hospital.citas if cita.paciente == paciente]

            if citas_pendientes:
                console.print("[bold]Citas pendientes:[/bold]")
                table = Table(title="Citas Pendientes")
                table.add_column("No.", justify="right")
                table.add_column("Fecha", style="cyan")
                table.add_column("Médico", style="magenta")

                for i, cita in enumerate(citas_pendientes):
                    table.add_row(str(i + 1), cita.fecha, cita.medico.nombre)

                console.print(table)
                opcion_cita = int(console.input("Seleccione la cita a cancelar (número): ")) - 1
                if 0 <= opcion_cita < len(citas_pendientes):
                    cita_seleccionada = citas_pendientes[opcion_cita]
                    hospital.cancelar_cita(paciente.id_persona, cita_seleccionada.fecha)
                else:
                    console.print("[red]Número de cita no válido.[/red]")
            else:
                console.print("[red]El paciente no tiene citas pendientes.[/red]")
        else:
            console.print("[red]Paciente no encontrado.[/red]")

    elif opcion == "4":  # Establecer médico de preferencia
        id_paciente = console.input("Ingrese la identificación del paciente: ")
        id_medico = console.input("Ingrese la identificación del médico: ")

        paciente = hospital.encontrar_paciente(id_paciente)
        medico = hospital.encontrar_medico(id_medico)

        if paciente and medico:
            paciente.asignar_medico(medico)
        else:
            console.print("[red]Paciente o médico no encontrado.[/red]")

    elif opcion == "5":  # Listar citas pendientes
        id_paciente = console.input("Ingrese la identificación del paciente: ")
        paciente = hospital.encontrar_paciente(id_paciente)

        if paciente:
            console.print("[bold]Citas pendientes:[/bold]")
            citas_pendientes = [cita for cita in hospital.citas if cita.paciente == paciente]

            if citas_pendientes:
                table = Table(title="Citas Pendientes")
                table.add_column("No.", justify="right")
                table.add_column("Fecha", style="cyan")
                table.add_column("Médico", style="magenta")

                for i, cita in enumerate(citas_pendientes):
                    table.add_row(str(i + 1), cita.fecha, cita.medico.nombre)

                console.print(table)
            else:
                console.print("[red]No hay citas pendientes.[/red]")
        else:
            console.print("[red]Paciente no encontrado.[/red]")

    elif opcion == "6":  # Buscar citas por fecha
        fecha_busqueda = console.input("[bold bright_cyan]Ingrese la fecha para buscar citas (YYYY-MM-DD): [/bold bright_cyan]")
        
        citas_encontradas = [cita for cita in hospital.citas if cita.fecha.startswith(fecha_busqueda)]
        
        if citas_encontradas:
            console.print(f"[bold]Citas programadas para el {fecha_busqueda}:[/bold]")
            table = Table(title=f"[bold cyan]Citas del {fecha_busqueda}[/bold cyan]")
            table.add_column("No.", justify="right")
            table.add_column("Hora", style="bright_magenta")
            table.add_column("Paciente", style="green")
            table.add_column("Médico", style="bright_cyan")
            
            for i, cita in enumerate(citas_encontradas):
                hora = cita.fecha.split(" ")[1]  # Extraer la hora de la fecha
                table.add_row(str(i + 1), hora, cita.paciente.nombre, cita.medico.nombre)
            
            console.print(table)
        else:
            console.print(f"[red]No se encontraron citas para el {fecha_busqueda}.[/red]")

    elif opcion == "7":  # Generar reporte de médicos por especialidad
        especialidades = {}
        
        for medico in hospital.medicos:
            especialidad = medico.especialidad
            if especialidad in especialidades:
                especialidades[especialidad] += 1
            else:
                especialidades[especialidad] = 1
        
        console.print("[bold]Reporte de médicos por especialidad:[/bold]")
        table = Table(title="[bold cyan]Médicos por Especialidad[/bold cyan]")
        table.add_column("Especialidad", style="bright_magenta")
        table.add_column("Cantidad", justify="right", style="green")
        
        for especialidad, cantidad in especialidades.items():
            table.add_row(especialidad, str(cantidad))
        
        console.print(table)

    elif opcion == "8":  # Ver historial de citas de un paciente
        id_paciente = console.input("[bold bright_cyan]Ingrese la identificación del paciente: [/bold bright_cyan]")
        paciente = hospital.encontrar_paciente(id_paciente)
        
        if paciente:
            citas_historial = [cita for cita in hospital.citas if cita.paciente == paciente]
            
            if citas_historial:
                console.print(f"[bold]Historial de citas del paciente {paciente.nombre}:[/bold]")
                table = Table(title=f"[bold cyan]Historial de Citas de {paciente.nombre}[/bold cyan]")
                table.add_column("Fecha", style="bright_magenta")
                table.add_column("Médico", style="green")
                table.add_column("Estado", style="bright_yellow")
                
                for cita in citas_historial:
                    estado = "Cancelada" if cita.cancelada else "Realizada"
                    table.add_row(cita.fecha, cita.medico.nombre, estado)
                
                console.print(table)
            else:
                console.print(f"[red]