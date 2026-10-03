from datos import pacientes, responsables


def formatear_fecha(dia, mes, anio):
    dia_txt = str(dia)
    mes_txt = str(mes)

    if len(dia_txt) == 1:
        dia_txt = "0" + dia_txt
    if len(mes_txt) == 1:
        mes_txt = "0" + mes_txt

    return dia_txt + "/" + mes_txt + "/" + str(anio)


def es_bisiesto(anio):
    return (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0)


def dias_mes(mes, anio):
    if mes in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    elif mes in [4, 6, 9, 11]:
        return 30
    elif mes == 2:
        if es_bisiesto(anio):
            return 29
        return 28
    return 0


def validar_fecha(fecha_str):
    partes = fecha_str.split("/")
    if len(partes) != 3:
        return None

    try:
        dia = int(partes[0])
        mes = int(partes[1])
        anio = int(partes[2])
    except ValueError:
        return None

    if anio < 1900 or anio > 2026 or mes < 1 or mes > 12:
        return None

    if dia < 1 or dia > dias_mes(mes, anio):
        return None

    return (dia, mes, anio)


def es_futura(fecha_nac, fecha_act):
    dia1, mes1, anio1 = fecha_nac
    dia2, mes2, anio2 = fecha_act

    if anio1 > anio2:
        return True
    if anio1 == anio2:
        if mes1 > mes2:
            return True
        if mes1 == mes2 and dia1 > dia2:
            return True
    return False


def calcular_edad(fecha_nac, fecha_act):
    dia1, mes1, anio1 = fecha_nac
    dia2, mes2, anio2 = fecha_act

    anos = anio2 - anio1
    meses = mes2 - mes1
    dias = dia2 - dia1

    if dias < 0:
        meses -= 1
        if mes2 > 1:
            mes_prev = mes2 - 1
            anio_prev = anio2
        else:
            mes_prev = 12
            anio_prev = anio2 - 1
        dias += dias_mes(mes_prev, anio_prev)

    if meses < 0:
        anos -= 1
        meses += 12

    return anos, meses, dias


def formato_resp(resp):
    return (
        f"Codigo: {resp['codigo']} | DNI: {resp['dni']} | "
        f"Nombre: {resp['nombres']} {resp['apellidos']} | "
        f"Telefono: {resp['telefono']} | Parentesco: {resp['parentesco']}"
    )


def cargar_demo():
    resp01_existe = False
    for resp in responsables:
        if resp["codigo"] == "RESP01":
            resp01_existe = True
            break

    if not resp01_existe:
        responsables.append(
            {
                "codigo": "RESP01",
                "dni": "09876543",
                "nombres": "Carlos",
                "apellidos": "Mendoza Rios",
                "telefono": "987654321",
                "parentesco": "Padre",
            }
        )
    resp02_existe = False
    for resp in responsables:
        if resp["codigo"] == "RESP02":
            resp02_existe = True
            break

    if not resp02_existe:
        responsables.append(
            {
                "codigo": "RESP02",
                "dni": "11223344",
                "nombres": "Maria",
                "apellidos": "Gomez Perales",
                "telefono": "912345678",
                "parentesco": "Madre",
            }
        )


def reg_responsable():
    print("\n--- REGISTRO DE RESPONSABLE ---")
    cod = input("Codigo del responsable: ").strip().upper()
    cod_existe = False
    for resp in responsables:
        if resp["codigo"] == cod:
            cod_existe = True
            break

    if cod_existe:
        print("ERROR: Ya existe un responsable registrado con ese codigo.")
        return

    while True:
        dni = input("DNI (8 digitos): ").strip()
        if len(dni) == 8 and dni.isdigit():
            dni_existe = False
            for resp in responsables:
                if resp["dni"] == dni:
                    dni_existe = True
                    break

            if dni_existe:
                print("ERROR: Ya existe un responsable con ese DNI.")
                continue
            break
        print("ERROR: El DNI debe ser numerico y tener exactamente 8 digitos.")

    nom = input("Nombres: ").strip().title()
    ape = input("Apellidos: ").strip().title()

    while True:
        tel = input("Telefono (9 digitos, inicia con 9): ").strip()
        if len(tel) == 9 and tel.isdigit() and tel[0] == "9":
            break
        print("ERROR: El telefono debe tener 9 digitos, ser numerico y comenzar con 9.")

    par = input("Parentesco (Padre, Madre, Tutor, etc.): ").strip().capitalize()

    responsables.append({
        "codigo": cod,
        "dni": dni,
        "nombres": nom,
        "apellidos": ape,
        "telefono": tel,
        "parentesco": par,
    })
    print(f"Responsable '{nom} {ape}' registrado con exito.")


def reg_paciente(fecha_act):
    print("\n--- REGISTRO DE NUEVO PACIENTE ---")

    cod_resp = input("Ingrese el Codigo del Responsable: ").strip().upper()
    resp_existe = False
    for resp in responsables:
        if resp["codigo"] == cod_resp:
            resp_existe = True
            break

    if not resp_existe:
        print(f"ERROR: El codigo de responsable '{cod_resp}' NO existe en el sistema.")
        print("Debe registrar primero al responsable o verificar el codigo.")
        return

    cod = input("Codigo del Paciente: ").strip().upper()
    cod_existe = False
    for pac in pacientes:
        if pac["codigo"] == cod:
            cod_existe = True
            break

    if cod_existe:
        print("ERROR: Ya existe un paciente registrado con ese codigo.")
        return

    while True:
        dni = input("DNI del Paciente (8 digitos): ").strip()
        if len(dni) == 8 and dni.isdigit():
            dni_existe = False
            for pac in pacientes:
                if pac["dni"] == dni:
                    dni_existe = True
                    break

            if dni_existe:
                print("ERROR: Ya existe un paciente con ese DNI.")
                continue
            break
        print("ERROR: El DNI debe tener exactamente 8 digitos numericos.")

    nom = input("Nombres: ").strip().title()
    ape = input("Apellidos: ").strip().title()

    while True:
        sexo = input("Sexo (M/F): ").strip().upper()
        if sexo in ["M", "F"]:
            break
        print("Opcion invalida. Ingrese 'M' o 'F'.")

    while True:
        fecha_str = input("Fecha de nacimiento (DD/MM/AAAA): ").strip()
        fecha_nac = validar_fecha(fecha_str)

        if fecha_nac is None:
            print("Formato de fecha incorrecto o dia/mes no valido. Use DD/MM/AAAA (ej: 15/08/2018).")
            continue

        if es_futura(fecha_nac, fecha_act):
            print("ERROR: La fecha de nacimiento no puede ser posterior a la fecha actual del sistema.")
            continue

        break

    pacientes.append({
        "codigo": cod,
        "dni": dni,
        "nombres": nom,
        "apellidos": ape,
        "f_nac": fecha_nac,
        "sexo": sexo,
        "cod_resp": cod_resp,
    })
    print(f"Paciente '{nom} {ape}' registrado correctamente.")


def listar_pacientes(fecha_act):
    print("\n--- LISTADO GENERAL DE PACIENTES ---")
    if not pacientes:
        print("No hay pacientes registrados en el sistema.")
        return

    print(f"{'Codigo':<8} {'DNI':<10} {'Nombres y Apellidos':<25} {'F. Nac.':<12} {'Sexo':<5} {'Edad Exacta'}")
    print("---------------------------------------------------------------------------")
    for p in pacientes:
        anos, meses, dias = calcular_edad(p["f_nac"], fecha_act)
        dia_n, mes_n, anio_n = p["f_nac"]
        fecha_txt = formatear_fecha(dia_n, mes_n, anio_n)
        nom_comp = f"{p['nombres']} {p['apellidos']}"
        print(f"{p['codigo']:<8} {p['dni']:<10} {nom_comp:<25} {fecha_txt:<12} {p['sexo']:<5} {anos}a {meses}m {dias}d")


def buscar_paciente(fecha_act):
    print("\n--- BUSQUEDA DE PACIENTE ---")
    if not pacientes:
        print("No hay pacientes registrados.")
        return

    busq = input("Ingrese DNI, Nombre o Apellido a buscar: ").strip().lower()
    hallados = []

    for p in pacientes:
        nom_comp = f"{p['nombres']} {p['apellidos']}".lower()
        if busq in p["dni"] or busq in nom_comp:
            hallados.append(p)

    if not hallados:
        print(f"No se encontraron pacientes que coincidan con '{busq}'.")
        return

    print(f"\nSe encontraron {len(hallados)} coincidencia(s):")
    for p in hallados:
        anos, meses, dias = calcular_edad(p["f_nac"], fecha_act)
        resp = None
        for item in responsables:
            if item["codigo"] == p["cod_resp"]:
                resp = item
                break
        dia_n, mes_n, anio_n = p["f_nac"]

        print("\n==================")
        print("DATOS DEL PACIENTE")
        print(f" - Codigo: {p['codigo']} | DNI: {p['dni']}")
        print(f" - Nombre Completo: {p['nombres']} {p['apellidos']}")
        print(f" - Fecha de Nacimiento: {formatear_fecha(dia_n, mes_n, anio_n)}")
        print(f" - Sexo: {p['sexo']}")
        print(f" - Edad Exacta: {anos} anos, {meses} meses y {dias} dias")
        print("-------------------")
        print("DATOS COMPLETOS DEL RESPONSABLE ASOCIADO")
        if resp:
            print(f" - {formato_resp(resp)}")
        else:
            print(" - Informacion de responsable no disponible.")
        print("=================")


def listar_resp():
    print("\n--- LISTA DE RESPONSABLES REGISTRADOS ---")
    if not responsables:
        print("No hay responsables registrados.")
        return
    for r in responsables:
        print(f" - {formato_resp(r)}")


def menu():
    cargar_demo()
    fecha_act = (2, 10, 2026)

    while True:
        print("\n==========================================")
        print("    SISTEMA DE GESTION CLINICA PEDIATRICA ")
        print("==========================================")
        print("1. Registrar paciente")
        print("2. Registrar responsable")
        print("3. Listar todos los pacientes")
        print("4. Buscar paciente (por DNI o Nombre/Apellido)")
        print("5. Listar responsables registrados")
        print("6. Salir")

        op = input("Seleccione una opcion (1-6): ").strip()

        if op == "1":
            reg_paciente(fecha_act)
        elif op == "2":
            reg_responsable()
        elif op == "3":
            listar_pacientes(fecha_act)
        elif op == "4":
            buscar_paciente(fecha_act)
        elif op == "5":
            listar_resp()
        elif op == "6":
            print("\nSaliendo del programa...")
            break
        else:
            print("\nOpcion no valida. Intente nuevamente.")
