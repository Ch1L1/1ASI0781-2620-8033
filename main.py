
responsables = []
pacientes = []
medicos = []
consultas = []
fecha_actual = (6, 10, 2026)

# RESPONSABLES

# ---------- VALIDACIONES ----------
def texto_vacio(texto):
    return texto == ""


def dni_duplicado(lista, dni):
    for r in lista:
        if r["dni"] == dni:
            return True
    return False


def codigo_duplicado(lista, codigo):
    for r in lista:
        if r["codigo"] == codigo:
            return True
    return False


def formatear_fecha(dia, mes, anio):
    dia_txt = str(dia)
    mes_txt = str(mes)

    if len(dia_txt) == 1:
        dia_txt = "0" + dia_txt
    if len(mes_txt) == 1:
        mes_txt = "0" + mes_txt

    return dia_txt + "/" + mes_txt + "/" + str(anio)


# ---------- FUNCIONES PRINCIPALES ----------
def muestra_resp(r):
    print("Código     :", r["codigo"])
    print("DNI        :", r["dni"])
    print("Nombre     :", r["nombres"], r["apellidos"])
    print("Teléfono   :", r["telefono"])
    print("Parentesco :", r["parentesco"])
    print("-----------------------------------")


def reg_resp(lista):
    print("\n===================================")
    print("     REGISTRAR RESPONSABLE")
    print("===================================")

    codigo = input("Código: ")
    if texto_vacio(codigo):
        print("[ERROR] El código no puede estar vacío.")
        return
    if codigo_duplicado(lista, codigo):
        print("[ERROR] Ya existe un responsable con ese código.")
        return

    dni = input("DNI: ")
    if texto_vacio(dni):
        print("[ERROR] El DNI no puede estar vacío.")
        return
    if dni_duplicado(lista, dni):
        print("[ERROR] Ya existe un responsable con ese DNI.")
        return

    nombres = input("Nombres: ")
    if texto_vacio(nombres):
        print("[ERROR] Los nombres no pueden estar vacíos.")
        return

    apellidos = input("Apellidos: ")
    if texto_vacio(apellidos):
        print("[ERROR] Los apellidos no pueden estar vacíos.")
        return

    telefono = input("Teléfono: ")
    parentesco = input("Parentesco con el paciente: ")

    nuevo = {
        "codigo": codigo,
        "dni": dni,
        "nombres": nombres,
        "apellidos": apellidos,
        "telefono": telefono,
        "parentesco": parentesco,
    }
    lista.append(nuevo)
    print("[OK] Responsable registrado correctamente.")


def lista_resp_reg(lista):
    print("\n===================================")
    print("     LISTA DE RESPONSABLES")
    print("===================================")

    if len(lista) == 0:
        print("No hay responsables registrados.")
        return

    for r in lista:
        muestra_resp(r)
    print("Total:", len(lista), "responsable(s)")


def busca_resp_dni(lista, dni):
    for r in lista:
        if r["dni"] == dni:
            return r
    return False


def busca_resp_cod(lista, codigo):
    for r in lista:
        if r["codigo"] == codigo:
            return r
    return False


def cambia_tel(lista):
    print("\n===================================")
    print("       MODIFICAR TELÉFONO")
    print("===================================")

    dni = input("DNI del responsable: ")
    r = busca_resp_dni(lista, dni)

    if r == False:
        print("[ERROR] No existe un responsable con ese DNI.")
        return

    print("Teléfono actual:", r["telefono"])
    r["telefono"] = input("Nuevo teléfono: ")
    print("[OK] Teléfono actualizado.")


def pacientes_resp(lista_resp, lista_pac):
    print("\n===================================")
    print("   PACIENTES DEL RESPONSABLE")
    print("===================================")

    dni = input("DNI del responsable: ")
    r = busca_resp_dni(lista_resp, dni)

    if r == False:
        print("[ERROR] No existe un responsable con ese DNI.")
        return

    print("Responsable:", r["nombres"], r["apellidos"])
    cont = 0
    for p in lista_pac:
        if p["cod_resp"] == r["codigo"]:
            print("  -", p["nombres"], p["apellidos"])
            cont = cont + 1

    if cont == 0:
        print("Este responsable no tiene pacientes asociados.")


# ---------- MENÚ ----------
def menu_resp(lista_resp, lista_pac):
    opcion = ""
    while opcion != "6":
        print("\n===================================")
        print("     GESTIÓN DE RESPONSABLES")
        print("===================================")
        print("1. Registrar responsable")
        print("2. Listar responsables")
        print("3. Buscar responsable por DNI")
        print("4. Modificar teléfono")
        print("5. Ver pacientes de un responsable")
        print("6. Salir")
        opcion = input("Elige una opción: ")

        if opcion == "1":
            reg_resp(lista_resp)
        elif opcion == "2":
            lista_resp_reg(lista_resp)
        elif opcion == "3":
            dni = input("DNI a buscar: ")
            r = busca_resp_dni(lista_resp, dni)
            if r == False:
                print("[ERROR] No se encontró el responsable.")
            else:
                muestra_resp(r)
        elif opcion == "4":
            cambia_tel(lista_resp)
        elif opcion == "5":
            pacientes_resp(lista_resp, lista_pac)
        elif opcion == "6":
            print("Hasta pronto.")
        else:
            print("[ERROR] Opción no válida.")


# PACIENTES

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
    if len(fecha_str) != 10 or fecha_str[2] != "/" or fecha_str[5] != "/":
        return False

    try:
        dia = int(fecha_str[:2])
        mes = int(fecha_str[3:5])
        anio = int(fecha_str[6:])
    except ValueError:
        return False

    if anio < 1900 or anio > 2026 or mes < 1 or mes > 12:
        return False

    if dia < 1 or dia > dias_mes(mes, anio):
        return False

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


def reg_paciente(fecha_actual):
    print("\n--- REGISTRO DE NUEVO PACIENTE ---")

    cod_resp = input("Ingrese el Codigo del Responsable: ")
    resp_existe = False
    for resp in responsables:
        if resp["codigo"] == cod_resp:
            resp_existe = True
            break

    if not resp_existe:
        print(f"ERROR: El codigo de responsable '{cod_resp}' NO existe en el sistema.")
        print("Debe registrar primero al responsable o verificar el codigo.")
        return

    cod = input("Codigo del Paciente: ")
    cod_existe = False
    for pac in pacientes:
        if pac["codigo"] == cod:
            cod_existe = True
            break

    if cod_existe:
        print("ERROR: Ya existe un paciente registrado con ese codigo.")
        return

    dni_valido = False
    while dni_valido == False:
        dni = input("DNI del Paciente (8 digitos): ")

        if len(dni) == 8 and dni.isdigit():
            dni_existe = False
            for pac in pacientes:
                if pac["dni"] == dni:
                    dni_existe = True
                    break

            if dni_existe:
                print("ERROR: Ya existe un paciente con ese DNI.")
            else:
                dni_valido = True
        else:
            print("ERROR: El DNI debe tener exactamente 8 digitos numericos.")

    nom = input("Nombres: ")
    if nom == "":
        print("Los nombres no pueden estar vacíos.")
        return

    ape = input("Apellidos: ")
    if ape == "":
        print("Los apellidos no pueden estar vacíos.")
        return

    while True:
        sexo = input("Sexo (M/F): ")
        if sexo in ["M", "F"]:
            break
        print("Opcion invalida. Ingrese 'M' o 'F'.")

    fecha_valida = False
    while fecha_valida == False:
        fecha_str = input("Fecha de nacimiento (DD/MM/AAAA): ")
        fecha_nac = validar_fecha(fecha_str)

        if fecha_nac == False:
            print(
                "Formato de fecha incorrecto o dia/mes no valido. "
                "Use DD/MM/AAAA (ej: 15/08/2018)."
            )
        else:
            if es_futura(fecha_nac, fecha_actual):
                print(
                    "ERROR: La fecha de nacimiento no puede ser posterior "
                    "a la fecha actual del sistema."
                )
            else:
                edad, meses, dias = calcular_edad(fecha_nac, fecha_actual)
                if edad > 17:
                    print("ERROR: El paciente debe tener 17 años o menos.")
                else:
                    fecha_valida = True

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


def listar_pac_det(fecha_actual):
    print("\n--- LISTADO GENERAL DE PACIENTES ---")
    if not pacientes:
        print("No hay pacientes registrados en el sistema.")
        return

    print(
        f"{'Codigo':<8} {'DNI':<10} {'Nombres y Apellidos':<25} "
        f"{'F. Nac.':<12} {'Sexo':<5} {'Edad Exacta'}"
    )
    print("---------------------------------------------------------------------------")
    for p in pacientes:
        anos, meses, dias = calcular_edad(p["f_nac"], fecha_actual)
        dia_n, mes_n, anio_n = p["f_nac"]
        fecha_txt = formatear_fecha(dia_n, mes_n, anio_n)
        nom_comp = f"{p['nombres']} {p['apellidos']}"
        print(
            f"{p['codigo']:<8} {p['dni']:<10} {nom_comp:<25} "
            f"{fecha_txt:<12} {p['sexo']:<5} {anos}a {meses}m {dias}d"
        )


def buscar_paciente(fecha_actual):
    print("\n--- BUSQUEDA DE PACIENTE ---")
    if not pacientes:
        print("No hay pacientes registrados.")
        return

    busq = input("Ingrese DNI, Nombre o Apellido a buscar: ")
    hallados = []

    for p in pacientes:
        nom_comp = f"{p['nombres']} {p['apellidos']}"
        if busq in p["dni"] or busq in nom_comp:
            hallados.append(p)

    if not hallados:
        print(f"No se encontraron pacientes que coincidan con '{busq}'.")
        return

    print(f"\nSe encontraron {len(hallados)} coincidencia(s):")
    for p in hallados:
        anos, meses, dias = calcular_edad(p["f_nac"], fecha_actual)
        resp = False
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

        op = input("Seleccione una opcion (1-6): ")

        if op == "1":
            reg_paciente(fecha_actual)
        elif op == "2":
            reg_resp(responsables)
        elif op == "3":
            listar_pac_det(fecha_actual)
        elif op == "4":
            buscar_paciente(fecha_actual)
        elif op == "5":
            listar_resp()
        elif op == "6":
            print("\nSaliendo del programa...")
            break
        else:
            print("\nOpcion no valida. Intente nuevamente.")


# MEDICOS

def muestra_medico(medico):
    print(
        f"Codigo: {medico['codigo']}\n"
        f"CMP: {medico['cmp']}\n"
        f"Nombre: {medico['nombres']}\n"
        f"Apellido: {medico['apellidos']}\n"
        f"Área o especialidad pediátrica: {medico['especialidad']}"
    )


def busca_medico_cod():
    cod_ing = input("Coloque el código a buscar: ")

    found = False

    for medico in medicos:
        if medico["codigo"] == cod_ing:
            print("\n¡Médico encontrado!")
            muestra_medico(medico)
            found = True

    if not found:
        print("Médico no encontrado...")


def elige_especial():
    es_valida = False
    opcion = ""

    while not es_valida:
        print("Especialidades:")
        print("     1. Pediatría general")
        print("     2. Neonatología")
        print("     3. Cardiología pediátrica")
        print("     4. Neumología pediátrica")
        print("     5. Gastroenterología pediátrica")

        opcion = input("Seleccione una especialidad: ")

        if opcion in ["1", "2", "3", "4", "5"]:
            es_valida = True
        else:
            print("Opción inválida. Intente nuevamente.\n")

    if opcion == "1":
        return "Pediatría general"
    elif opcion == "2":
        return "Neonatología"
    elif opcion == "3":
        return "Cardiología pediátrica"
    elif opcion == "4":
        return "Neumología pediátrica"
    else:
        return "Gastroenterología pediátrica"


def busca_medico_esp():
    print("\nSelecciona una especialidad para buscar médicos: ")

    esp_buscada = elige_especial()
    found = False

    print(f"\nMédicos de {esp_buscada}:\n")

    for medico in medicos:
        if medico["especialidad"] == esp_buscada:
            muestra_medico(medico)
            print()
            found = True

    if not found:
        print("No hay médicos registrados en esa especialidad.")


def registra_medico():
    codigo = input("Ingrese código (Enter para terminar): ")
    if codigo == "":
        print("Registro de médicos finalizado.\n")
        return False

    if codigo_duplicado(medicos, codigo):
        print("Ya existe un médico con ese código.")
        return False

    cmp_valido = False

    while cmp_valido == False:
        numero_valido = True

        try:
            cmp = int(input("Ingrese CMP: "))
        except ValueError:
            print("El CMP debe ser un número entero.")
            numero_valido = False

        if numero_valido == True:
            rep = False

            if cmp < 0:
                print("El CMP no puede ser negativo.")
            else:
                for medico in medicos:
                    if medico["cmp"] == cmp:
                        rep = True

                if rep:
                    print("Ese CMP ya está registrado. Ingrese otro.")
                else:
                    cmp_valido = True

    nombres = input("Ingrese nombre: ")
    if nombres == "":
        print("El nombre no puede estar vacío.")
        return False

    apellidos = input("Ingrese apellido: ")
    if apellidos == "":
        print("El apellido no puede estar vacío.")
        return False

    area_esp = elige_especial()

    nuevo_medico = {
        "codigo": codigo,
        "cmp": cmp,
        "nombres": nombres,
        "apellidos": apellidos,
        "especialidad": area_esp,
    }

    medicos.append(nuevo_medico)
    print("Médico registrado correctamente.\n")
    return True


def muestra_medicos():
    print("\nLista completa de médicos:\n")

    for medico in medicos:
        muestra_medico(medico)
        print()


def modifica_cmp(medico):
    cmp_valido = False

    while cmp_valido == False:
        numero_valido = True

        try:
            nuevo_cmp = int(input("Ingrese nuevo CMP: "))
        except ValueError:
            print("El CMP debe ser un número entero.")
            numero_valido = False

        if numero_valido == True:
            rep = False

            if nuevo_cmp < 0:
                print("El CMP no puede ser negativo.")
            else:
                for otro in medicos:
                    if otro["cmp"] == nuevo_cmp and otro["codigo"] != medico["codigo"]:
                        rep = True

                if rep:
                    print("Ese CMP ya está registrado. Ingrese otro.")
                else:
                    medico["cmp"] = nuevo_cmp
                    cmp_valido = True
                    print("\nMédico modificado correctamente.")


def modifica_medico():
    cod_ing = input("Ingrese el código del médico a modificar: ")
    found = False

    for medico in medicos:
        if medico["codigo"] == cod_ing:
            found = True
            print("\n¿Qué desea modificar?")
            print("     1. Nombre")
            print("     2. Apellido")
            print("     3. Especialidad")
            print("     4. CMP")

            opcion = input("Modificar: ")

            if opcion == "1":
                nuevo_nombre = input("Ingrese nuevo nombre: ")
                if nuevo_nombre == "":
                    print("El nombre no puede estar vacío.")
                else:
                    medico["nombres"] = nuevo_nombre
                    print("\nMédico modificado correctamente.")
            elif opcion == "2":
                nuevo_apellido = input("Ingrese nuevo apellido: ")
                if nuevo_apellido == "":
                    print("El apellido no puede estar vacío.")
                else:
                    medico["apellidos"] = nuevo_apellido
                    print("\nMédico modificado correctamente.")
            elif opcion == "3":
                medico["especialidad"] = elige_especial()
                print("\nMédico modificado correctamente.")
            elif opcion == "4":
                modifica_cmp(medico)
            else:
                print("Opción inválida.")

    if not found:
        print("Médico no encontrado.\n")


def menu_medicos():
    while True:
        print("\n=== GESTIÓN DE MÉDICOS ===")
        print("1. Registrar médico")
        print("2. Listar médicos")
        print("3. Buscar médico por código")
        print("4. Buscar médicos por especialidad")
        print("5. Modificar médico")
        print("6. Volver al menú principal")
        opcion = input("Seleccione opción: ")

        if opcion == "1":
            registra_medico()
        elif opcion == "2":
            muestra_medicos()
        elif opcion == "3":
            busca_medico_cod()
        elif opcion == "4":
            busca_medico_esp()
        elif opcion == "5":
            modifica_medico()
        elif opcion == "6":
            break
        else:
            print("Opción inválida.")


# CONSULTAS
def busca_medico(medicos_lista, codigo_medico):
    for medico in medicos_lista:
        if medico['codigo'] == codigo_medico:
            print("\n¡Médico encontrado!")
            return True

    print("Médico no encontrado...")
    return False


def busca_paciente(pacientes_lista, codigo_paciente):
    for paciente in pacientes_lista:
        if paciente['codigo'] == codigo_paciente:
            print("\n¡Paciente encontrado!")
            return True

    print("Paciente no encontrado...")
    return False


def valida_consulta(lista_consultas, codigo_consulta):
    for consulta in lista_consultas:
        if codigo_consulta == consulta['Codigo']:
            print("¡Este codigo ya existe!")
            return False

    print("Codigo valido")
    return True


def ingresa_consulta(lista_consultas, pacientes_lista, medicos_lista):
    codigo = input("Ingrese codigo de la consulta: ")
    if not valida_consulta(lista_consultas, codigo):
        return

    codigo_paciente = input("Ingrese codigo del paciente: ")
    if not busca_paciente(pacientes_lista, codigo_paciente):
        print("No se puede registrar: El paciente no existe.")
        return

    codigo_medico = input("Ingrese codigo del medico: ")
    if not busca_medico(medicos_lista, codigo_medico):
        print("No se puede registrar: El médico no existe.")
        return

    fecha_valida = False
    while fecha_valida == False:
        fecha_txt = input("Ingrese fecha de la consulta (DD/MM/AAAA): ")
        fecha_cons = validar_fecha(fecha_txt)

        if fecha_cons == False:
            print("ERROR: Ingrese una fecha válida en formato DD/MM/AAAA.")
        else:
            if es_futura(fecha_cons, fecha_actual):
                print("ERROR: La fecha de consulta no puede ser futura.")
            else:
                dia, mes, anio = fecha_cons
                fecha = formatear_fecha(dia, mes, anio)
                fecha_valida = True

    motivo = input("Ingrese el motivo de la consulta: ")

    peso_valido = False
    while peso_valido == False:
        numero_valido = True

        try:
            peso = float(input("Ingrese el peso del paciente: "))
        except ValueError:
            print("ERROR: El peso debe ser un número.")
            numero_valido = False

        if numero_valido == True:
            if peso <= 0:
                print("ERROR: El peso debe ser mayor a 0.")
            else:
                peso_valido = True

    talla_valida = False
    while talla_valida == False:
        numero_valido = True

        try:
            talla = float(input("Ingrese la talla del paciente: "))
        except ValueError:
            print("ERROR: La talla debe ser un número.")
            numero_valido = False

        if numero_valido == True:
            if talla <= 0:
                print("ERROR: La talla debe ser mayor a 0.")
            else:
                talla_valida = True

    observaciones = input("Ingrese observaciones requeridas: ")

    costo_valido = False
    while costo_valido == False:
        numero_valido = True

        try:
            costo = float(input("Ingrese el costo de la consulta: "))
        except ValueError:
            print("ERROR: El costo debe ser un número.")
            numero_valido = False

        if numero_valido == True:
            if costo <= 0:
                print("ERROR: El costo debe ser mayor a 0.")
            else:
                costo_valido = True

    nueva_consulta = {
        "Codigo": codigo,
        "Codigo Paciente": codigo_paciente,
        "Codigo Medico": codigo_medico,
        "Fecha": fecha,
        "Motivo": motivo,
        "Peso": peso,
        "Talla": talla,
        "Observaciones": observaciones,
        "Costo": costo,
    }

    lista_consultas.append(nueva_consulta)
    print("Consulta guardada con éxito!")


# REPORTES
def listar_pacientes(pacientes):
    print("\nLISTADO GENERAL DE PACIENTES:\n")
    for p in pacientes:
        if "f_nac" not in p:
            fecha_txt = p["fecha_nacimiento"]
        else:
            dia, mes, anio = p["f_nac"]
            fecha_txt = formatear_fecha(dia, mes, anio)
        print(
            f"Código: {p['codigo']} | DNI: {p['dni']} | "
            f"Nombre: {p['nombres']} {p['apellidos']} | "
            f"Nacimiento: {fecha_txt}"
        )


def listar_medicos(medicos):
    print("\nLISTADO GENERAL DE MÉDICOS:\n")
    for m in medicos:
        print(
            f"Código: {m['codigo']} | CMP: {m['cmp']} | "
            f"Nombre: {m['nombres']} {m['apellidos']} | "
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
                f"Costo: S/{cons['Costo']} | Peso: {cons['Peso']}kg"
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
        print(
            f"Médico: {med['nombres']} {med['apellidos']} "
            f"({cod_med}) -> {cont} consultas"
        )


def ingreso_total(consultas):
    total = 0
    for cons in consultas:
        total += cons['Costo']
    print(f"\nIngreso total generado por consultas: S/{total}")


def promedio_costo(consultas):
    total_cons = len(consultas)
    if total_cons == 0:
        print("\nPromedio del costo de las consultas: S/0")
        return

    suma = 0
    for cons in consultas:
        suma += cons['Costo']
    prom = suma / total_cons
    print(f"\nPromedio del costo de las consultas: S/{prom}")


def paciente_max(consultas, pacientes):
    if not consultas:
        print("\nNo hay consultas registradas.")
        return

    max_cons = 0
    pac_win = "Ninguno"

    for pac in pacientes:
        cod_pac = pac['codigo']
        cont = 0
        for cons in consultas:
            if cons['Codigo Paciente'] == cod_pac:
                cont += 1

        if cont > max_cons:
            max_cons = cont
            pac_win = f"{pac['nombres']} {pac['apellidos']} ({cod_pac})"

    print(
        f"\nPaciente con mayor cantidad de consultas: {pac_win} "
        f"con {max_cons} consultas."
    )


def edad_rangos(pacientes):
    rango_0_2 = 0
    rango_3_5 = 0
    rango_6_11 = 0
    rango_12_17 = 0
    for pac in pacientes:
        edad, meses, dias = calcular_edad(pac["f_nac"], fecha_actual)

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
                f"Médico: {cons['Codigo Medico']} | Costo: S/{cons['Costo']}"
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
    print(f"Total de consultas realizadas: {num_atenc}")
    print(f"Ingreso total generado: S/{ing_med}")


# MENU PRINCIPAL Y REPORTES
def reg_consulta():
    ingresa_consulta(consultas, pacientes, medicos)


def hist_pac_menu():
    dni = input("Ingrese DNI del paciente: ")
    encontrado = False
    cod_pac = ""

    for item in pacientes:
        if item["dni"] == dni:
            encontrado = True
            cod_pac = item["codigo"]
            break

    if encontrado == False:
        print("No existe ese paciente.")
        return

    hist_paciente(consultas, cod_pac)


def menu_reportes():
    while True:
        print("\n=== REPORTES ===")
        print("1. Listado general de pacientes")
        print("2. Listado general de médicos")
        print("3. Pacientes atendidos por un médico")
        print("4. Historial de consultas de un paciente")
        print("5. Total de consultas")
        print("6. Consultas por médico")
        print("7. Ingreso total")
        print("8. Promedio del costo")
        print("9. Paciente con más consultas")
        print("10. Conteo por rango de edad")
        print("11. Consultas por fecha")
        print("12. Ingresos por médico")
        print("13. Volver")
        opcion = input("Seleccione opción: ")

        if opcion == "1":
            listar_pacientes(pacientes)
        elif opcion == "2":
            listar_medicos(medicos)
        elif opcion == "3":
            cod = input("Código del médico: ")
            pacientes_medico(consultas, pacientes, cod)
        elif opcion == "4":
            hist_pac_menu()
        elif opcion == "5":
            total_consultas(consultas)
        elif opcion == "6":
            consul_medico(consultas, medicos)
        elif opcion == "7":
            ingreso_total(consultas)
        elif opcion == "8":
            promedio_costo(consultas)
        elif opcion == "9":
            paciente_max(consultas, pacientes)
        elif opcion == "10":
            edad_rangos(pacientes)
        elif opcion == "11":
            fecha_txt = input("Ingrese la fecha de consulta (DD/MM/AAAA): ")
            fecha_bus = validar_fecha(fecha_txt)

            if fecha_bus == False:
                print("Fecha inválida. Use DD/MM/AAAA.")
            else:
                dia, mes, anio = fecha_bus
                fecha = formatear_fecha(dia, mes, anio)
                rep_fecha(consultas, fecha)
        elif opcion == "12":
            cod = input("Código del médico: ")
            rep_ing_med(consultas, cod)
        elif opcion == "13":
            break
        else:
            print("Opción inválida.")


def main():
    while True:
        print("\n=== CLÍNICA PEDIÁTRICA ===")
        print("1. Gestión de responsables")
        print("2. Gestión de pacientes")
        print("3. Gestión de médicos")
        print("4. Registrar consulta")
        print("5. Consultar historial del paciente")
        print("6. Reportes")
        print("7. Salir")
        opcion = input("Seleccione opción: ")

        if opcion == "1":
            menu_resp(responsables, pacientes)
        elif opcion == "2":
            menu()
        elif opcion == "3":
            menu_medicos()
        elif opcion == "4":
            reg_consulta()
        elif opcion == "5":
            hist_pac_menu()
        elif opcion == "6":
            menu_reportes()
        elif opcion == "7":
            print("Saliendo del sistema...")
            break
        else:
            print("Opción inválida. Intente nuevamente.")



main()
