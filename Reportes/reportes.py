def listarPacientesGeneral(pacientes):
    print("\nLISTADO GENERAL DE PACIENTES:\n")
    for p in pacientes:
        print(
            f"Código: {p['codigo']} | DNI: {p['dni']} | Nombre: {p['nombres']} {p['apellidos']} | "
            f"Nacimiento: {p['fecha_nacimiento']}"
        )


def listarMedicosGeneral(medicos):
    print("\nLISTADO GENERAL DE MÉDICOS:\n")
    for m in medicos:
        print(
            f"Código: {m['codigo']} | CMP: {m['cmp']} | Nombre: {m['nombres']} {m['apellidos']} | "
            f"Especialidad: {m['especialidad']}"
        )


def pacientesAtendidosPorMedico(consultas, pacientes, codigo_medico):
    print(f"\nPACIENTES ATENDIDOS POR EL MÉDICO: {codigo_medico}\n")

    pacientes_vistos = []
    for consulta in consultas:
        if consulta['Codigo Medico'] == codigo_medico:
            codigo_paciente = consulta['Codigo Paciente']
            if codigo_paciente not in pacientes_vistos:
                pacientes_vistos.append(codigo_paciente)

    for codigo_paciente in pacientes_vistos:
        for paciente in pacientes:
            if paciente['codigo'] == codigo_paciente:
                print(f"- {paciente['nombres']} {paciente['apellidos']} (Código: {paciente['codigo']})")


def historialConsultasPaciente(consultas, codigo_paciente):
    print(f"\nHISTORIAL DE CONSULTAS DEL PACIENTE: {codigo_paciente}\n")

    contador = 0
    for consulta in consultas:
        if consulta['Codigo Paciente'] == codigo_paciente:
            print(
                f"Fecha: {consulta['Fecha']} | Motivo: {consulta['Motivo']} | "
                f"Costo: ${consulta['Costo']} | Peso: {consulta['Peso']}kg"
            )
            contador += 1

    if contador == 0:
        print("El paciente no tiene consultas registradas.")


def cantidadTotalConsultas(consultas):
    contador = len(consultas)
    print(f"\nCantidad total de consultas realizadas: {contador}")


def consultasPorMedico(consultas, medicos):
    print("\nCANTIDAD DE CONSULTAS POR MÉDICO")
    for medico in medicos:
        codigo_medico = medico['codigo']
        contador = 0
        for consulta in consultas:
            if consulta['Codigo Medico'] == codigo_medico:
                contador += 1
        print(f"Médico: {medico['nombres']} {medico['apellidos']} ({codigo_medico}) -> {contador} consultas")


def ingresoTotalConsultas(consultas):
    total = sum(consulta['Costo'] for consulta in consultas)
    print(f"\nIngreso total generado por consultas: ${total}")


def promedioCostoConsultas(consultas):
    total_consultas = len(consultas)
    if total_consultas == 0:
        print("\nPromedio del costo de las consultas: $0")
        return

    suma_costos = sum(consulta['Costo'] for consulta in consultas)
    promedio = suma_costos / total_consultas
    print(f"\nPromedio del costo de las consultas: ${promedio}")


def pacienteMayorConsultas(consultas, pacientes):
    if not consultas:
        print("\nNo hay consultas registradas.")
        return

    max_consultas = 0
    paciente_ganador = "Ninguno"

    for paciente in pacientes:
        codigo_paciente = paciente['codigo']
        contador = sum(
            1 for consulta in consultas if consulta['Codigo Paciente'] == codigo_paciente
        )

        if contador > max_consultas:
            max_consultas = contador
            paciente_ganador = f"{paciente['nombres']} {paciente['apellidos']} ({codigo_paciente})"

    print(f"\nPaciente con mayor cantidad de consultas: {paciente_ganador} con {max_consultas} consultas.")


def pacientesPorRangoEdad(pacientes):
    rango_0_2 = 0
    rango_3_5 = 0
    rango_6_11 = 0
    rango_12_17 = 0

    for paciente in pacientes:
        anio_nacimiento = int(paciente['fecha_nacimiento'][:4])
        edad = 2026 - anio_nacimiento

        if 0 <= edad <= 2:
            rango_0_2 += 1
        elif 3 <= edad <= 5:
            rango_3_5 += 1
        elif 6 <= edad <= 11:
            rango_6_11 += 1
        elif 12 <= edad <= 17:
            rango_12_17 += 1

    print(f"\nDISTRIBUCIÓN DE PACIENTES SEGÚN EDAD")
    print(f"De 0 a 2 años: {rango_0_2} pacientes")
    print(f"De 3 a 5 años: {rango_3_5} pacientes")
    print(f"De 6 a 11 años: {rango_6_11} pacientes")
    print(f"De 12 a 17 años: {rango_12_17} pacientes")


def reporteConsultasPorFecha(consultas, fecha_buscada):
    contador = 0
    print(f"\n--- CONSULTAS EN LA FECHA: {fecha_buscada} ---")

    for consulta in consultas:
        if consulta['Fecha'] == fecha_buscada:
            print(
                f"Código: {consulta['Codigo']} | Paciente: {consulta['Codigo Paciente']} | "
                f"Médico: {consulta['Codigo Medico']} | Costo: ${consulta['Costo']}"
            )
            contador += 1

    print(f"Total de consultas en esta fecha: {contador}")


def reporteIngresosPorMedico(consultas, codigo_medico):
    ingreso_total_medico = 0
    cantidad_atenciones = 0

    for consulta in consultas:
        if consulta['Codigo Medico'] == codigo_medico:
            ingreso_total_medico += consulta['Costo']
            cantidad_atenciones += 1

    print(f"\nREPORTE FINANCIERO DEL MÉDICO: {codigo_medico}")
    print(f"Total de pacientes atendidos: {cantidad_atenciones}")
    print(f"Ingreso total generado: ${ingreso_total_medico}")


def ejecutar_demo():
    medicos_prueba = [
        {"codigo": "M001", "cmp": "12345", "nombres": "Carlos", "apellidos": "Pérez", "especialidad": "Pediatría general"},
        {"codigo": "M002", "cmp": "67890", "nombres": "María", "apellidos": "Gómez", "especialidad": "Neonatología"},
    ]

    pacientes_prueba = [
        {"codigo": "P001", "dni": "11111111", "nombres": "Juanito", "apellidos": "Quispe", "fecha_nacimiento": "2024-05-10"},
        {"codigo": "P002", "dni": "22222222", "nombres": "Anita", "apellidos": "Rojas", "fecha_nacimiento": "2020-03-15"},
        {"codigo": "P003", "dni": "33333333", "nombres": "Pepito", "apellidos": "Mamani", "fecha_nacimiento": "2012-08-20"},
    ]

    consultas_prueba = [
        {"Codigo": "C001", "Codigo Paciente": "P001", "Codigo Medico": "M001", "Fecha": "2026-06-06", "Motivo": "Fiebre", "Peso": 12.5, "Talla": 85.0, "Observaciones": "Leve", "Costo": 50.0},
        {"Codigo": "C002", "Codigo Paciente": "P001", "Codigo Medico": "M001", "Fecha": "2026-06-10", "Motivo": "Control", "Peso": 13.0, "Talla": 87.0, "Observaciones": "Sano", "Costo": 40.0},
        {"Codigo": "C003", "Codigo Paciente": "P002", "Codigo Medico": "M002", "Fecha": "2026-06-06", "Motivo": "Tos", "Peso": 20.0, "Talla": 110.0, "Observaciones": "Bronquios", "Costo": 60.0},
    ]

    listarPacientesGeneral(pacientes_prueba)
    listarMedicosGeneral(medicos_prueba)
    cantidadTotalConsultas(consultas_prueba)
    ingresoTotalConsultas(consultas_prueba)
    promedioCostoConsultas(consultas_prueba)
    pacienteMayorConsultas(consultas_prueba, pacientes_prueba)
    pacientesPorRangoEdad(pacientes_prueba)
    reporteConsultasPorFecha(consultas_prueba, "2026-06-06")
    reporteIngresosPorMedico(consultas_prueba, "M001")


if __name__ == "__main__":
    ejecutar_demo()