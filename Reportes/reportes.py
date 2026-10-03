def listar_pacientes(pacientes):
    print("\nLISTADO GENERAL DE PACIENTES:\n")
    for p in pacientes:
        fecha_nac = p.get("f_nac")
        if fecha_nac is None:
            fecha_txt = p["fecha_nacimiento"]
        else:
            dia, mes, anio = fecha_nac
            fecha_txt = f"{dia:02d}/{mes:02d}/{anio}"
        print(
            f"Código: {p['codigo']} | DNI: {p['dni']} | Nombre: {p['nombres']} {p['apellidos']} | "
            f"Nacimiento: {fecha_txt}"
        )


def listar_medicos(medicos):
    print("\nLISTADO GENERAL DE MÉDICOS:\n")
    for m in medicos:
        print(
            f"Código: {m['codigo']} | CMP: {m['cmp']} | Nombre: {m['nombres']} {m['apellidos']} | "
            f"Especialidad: {m['especialidad']}"
        )


def pacientes_medico(consultas, pacientes, cod_med):
    print(f"\nPACIENTES ATENDIDOS POR EL MÉDICO: {cod_med}\n")

    pac_vistos = []
    for cons in consultas:
        if cons['Codigo Medico'] == cod_med:
            cod_pac = cons['Codigo Paciente']
            if cod_pac not in pac_vistos:
                pac_vistos.append(cod_pac)

    for cod_pac in pac_vistos:
        for pac in pacientes:
            if pac['codigo'] == cod_pac:
                print(f"- {pac['nombres']} {pac['apellidos']} (Código: {pac['codigo']})")


def hist_paciente(consultas, cod_pac):
    print(f"\nHISTORIAL DE CONSULTAS DEL PACIENTE: {cod_pac}\n")

    cont = 0
    for cons in consultas:
        if cons['Codigo Paciente'] == cod_pac:
            print(
                f"Fecha: {cons['Fecha']} | Motivo: {cons['Motivo']} | "
                f"Costo: ${cons['Costo']} | Peso: {cons['Peso']}kg"
            )
            cont += 1

    if cont == 0:
        print("El paciente no tiene consultas registradas.")


def total_consultas(consultas):
    cont = len(consultas)
    print(f"\nCantidad total de consultas realizadas: {cont}")


def consul_medico(consultas, medicos):
    print("\nCANTIDAD DE CONSULTAS POR MÉDICO")
    for med in medicos:
        cod_med = med['codigo']
        cont = 0
        for cons in consultas:
            if cons['Codigo Medico'] == cod_med:
                cont += 1
        print(f"Médico: {med['nombres']} {med['apellidos']} ({cod_med}) -> {cont} consultas")


def ingreso_total(consultas):
    total = sum(cons['Costo'] for cons in consultas)
    print(f"\nIngreso total generado por consultas: ${total}")


def promedio_costo(consultas):
    total_cons = len(consultas)
    if total_cons == 0:
        print("\nPromedio del costo de las consultas: $0")
        return

    suma = sum(cons['Costo'] for cons in consultas)
    prom = suma / total_cons
    print(f"\nPromedio del costo de las consultas: ${prom}")


def paciente_max(consultas, pacientes):
    if not consultas:
        print("\nNo hay consultas registradas.")
        return

    max_cons = 0
    pac_win = "Ninguno"

    for pac in pacientes:
        cod_pac = pac['codigo']
        cont = sum(1 for cons in consultas if cons['Codigo Paciente'] == cod_pac)

        if cont > max_cons:
            max_cons = cont
            pac_win = f"{pac['nombres']} {pac['apellidos']} ({cod_pac})"

    print(f"\nPaciente con mayor cantidad de consultas: {pac_win} con {max_cons} consultas.")


def edad_rangos(pacientes):
    rango_0_2 = 0
    rango_3_5 = 0
    rango_6_11 = 0
    rango_12_17 = 0

    for pac in pacientes:
        fecha_nac = pac.get("f_nac")
        if fecha_nac is None:
            anio_nac = int(pac["fecha_nacimiento"][:4])
        else:
            anio_nac = fecha_nac[2]
        edad = 2026 - anio_nac

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


def rep_fecha(consultas, fecha_bus):
    cont = 0
    print(f"\n--- CONSULTAS EN LA FECHA: {fecha_bus} ---")

    for cons in consultas:
        if cons['Fecha'] == fecha_bus:
            print(
                f"Código: {cons['Codigo']} | Paciente: {cons['Codigo Paciente']} | "
                f"Médico: {cons['Codigo Medico']} | Costo: ${cons['Costo']}"
            )
            cont += 1

    print(f"Total de consultas en esta fecha: {cont}")


def rep_ing_med(consultas, cod_med):
    ing_med = 0
    num_atenc = 0

    for cons in consultas:
        if cons['Codigo Medico'] == cod_med:
            ing_med += cons['Costo']
            num_atenc += 1

    print(f"\nREPORTE FINANCIERO DEL MÉDICO: {cod_med}")
    print(f"Total de pacientes atendidos: {num_atenc}")
    print(f"Ingreso total generado: ${ing_med}")


def ejecuta_demo():
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

    listar_pacientes(pacientes_prueba)
    listar_medicos(medicos_prueba)
    total_consultas(consultas_prueba)
    ingreso_total(consultas_prueba)
    promedio_costo(consultas_prueba)
    paciente_max(consultas_prueba, pacientes_prueba)
    edad_rangos(pacientes_prueba)
    rep_fecha(consultas_prueba, "2026-06-06")
    rep_ing_med(consultas_prueba, "M001")


if __name__ == "__main__":
    ejecuta_demo()