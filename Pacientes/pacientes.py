
resp_db = {}
paci_db = {}

def es_bisiesto(a):
    return (a % 4 == 0 and a % 100 != 0) or (a % 400 == 0)


def dias_mes(m, a):
    if m in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    elif m in [4, 6, 9, 11]:
        return 30
    elif m == 2:
        if es_bisiesto(a):
            return 29
        else:
            return 28
    return 0


def validar_fecha(f_str):
    p = f_str.split("/")
    if len(p) != 3:
        return None

    try:
        d = int(p[0])
        m = int(p[1])
        a = int(p[2])
    except ValueError:
        return None

    if a < 1900 or a > 2026 or m < 1 or m > 12:
        return None

    if d < 1 or d > dias_mes(m, a):
        return None

    return (d, m, a)


def es_futura(f_nac, f_act):
    d1, m1, a1 = f_nac
    d2, m2, a2 = f_act

    if a1 > a2:
        return True
    elif a1 == a2:
        if m1 > m2:
            return True
        elif m1 == m2 and d1 > d2:
            return True
    return False


def calcular_edad(f_nac, f_act):
    d1, m1, a1 = f_nac
    d2, m2, a2 = f_act

    anos = a2 - a1
    meses = m2 - m1
    dias = d2 - d1

    if dias < 0:
        meses = meses - 1
        if m2 > 1:
            m_prev = m2 - 1
            a_prev = a2
        else:
            m_prev = 12
            a_prev = a2 - 1
        dias = dias + dias_mes(m_prev, a_prev)

    if meses < 0:
        anos = anos - 1
        meses = meses + 12

    return anos, meses, dias


def formato_resp(r):
    return f"Codigo: {r['cod']} | DNI: {r['dni']} | Nombre: {r['nom']} {r['ape']} | Telefono: {r['tel']} | Parentesco: {r['par']}"


def cargar_demo():
    resp_db["RESP01"] = {
        "cod": "RESP01",
        "dni": "09876543",
        "nom": "Carlos",
        "ape": "Mendoza Rios",
        "tel": "987654321",
        "par": "Padre"
    }
    resp_db["RESP02"] = {
        "cod": "RESP02",
        "dni": "11223344",
        "nom": "Maria",
        "ape": "Gomez Perales",
        "tel": "912345678",
        "par": "Madre"
    }

def reg_responsable():
    print("\n--- REGISTRO DE RESPONSABLE ---")
    c = input("Codigo del responsable: ").strip().upper()
    if c in resp_db:
        print("ERROR: Ya existe un responsable registrado con ese codigo.")
        return

    while True:
        d = input("DNI (8 digitos): ").strip()
        if len(d) == 8 and d.isdigit():
            break
        print("ERROR: El DNI debe ser numerico y tener exactamente 8 digitos.")

    nom = input("Nombres: ").strip().title()
    ape = input("Apellidos: ").strip().title()

    while True:
        t = input("Telefono (9 digitos, inicia con 9): ").strip()
        if len(t) == 9 and t.isdigit() and t[0] == "9":
            break
        print("ERROR: El telefono debe tener 9 digitos, ser numerico y comenzar con 9.")

    par = input("Parentesco (Padre, Madre, Tutor, etc.): ").strip().capitalize()

    resp_db[c] = {
        "cod": c,
        "dni": d,
        "nom": nom,
        "ape": ape,
        "tel": t,
        "par": par
    }
    print(f"Responsable '{nom} {ape}' registrado con exito.")


def reg_paciente(f_act):
    print("\n--- REGISTRO DE NUEVO PACIENTE ---")

    c_resp = input("Ingrese el Codigo del Responsable: ").strip().upper()
    if c_resp not in resp_db:
        print(f"ERROR: El codigo de responsable '{c_resp}' NO existe en el sistema.")
        print("Debe registrar primero al responsable o verificar el codigo.")
        return

    c = input("Codigo del Paciente: ").strip().upper()
    if c in paci_db:
        print("ERROR: Ya existe un paciente registrado con ese codigo.")
        return

    while True:
        d = input("DNI del Paciente (8 digitos): ").strip()
        if len(d) == 8 and d.isdigit():
            break
        print("ERROR: El DNI debe tener exactamente 8 digitos numericos.")

    nom = input("Nombres: ").strip().title()
    ape = input("Apellidos: ").strip().title()

    while True:
        s = input("Sexo (M/F): ").strip().upper()
        if s in ["M", "F"]:
            break
        print("Opcion invalida. Ingrese 'M' o 'F'.")

    while True:
        f_str = input("Fecha de nacimiento (DD/MM/AAAA): ").strip()
        f_nac = validar_fecha(f_str)

        if f_nac == None:
            print("Formato de fecha incorrecto o dia/mes no valido. Use DD/MM/AAAA (ej: 15/08/2018).")
            continue

        if es_futura(f_nac, f_act):
            print("ERROR: La fecha de nacimiento no puede ser posterior a la fecha actual del sistema.")
            continue

        break

    paci_db[c] = {
        "cod": c,
        "dni": d,
        "nom": nom,
        "ape": ape,
        "fnac": f_nac,
        "sexo": s,
        "c_resp": c_resp
    }
    print(f"Paciente '{nom} {ape}' registrado correctamente.")


def listar_pacientes(f_act):
    print("\n--- LISTADO GENERAL DE PACIENTES ---")
    if not paci_db:
        print("No hay pacientes registrados en el sistema.")
        return

    print(f"{'Codigo':<8} {'DNI':<10} {'Nombres y Apellidos':<25} {'F. Nac.':<12} {'Sexo':<5} {'Edad Exacta'}")
    print("-" * 75)
    for p in paci_db.values():
        a, m, d = calcular_edad(p["fnac"], f_act)
        d_n, m_n, a_n = p["fnac"]
        f_str = f"{d_n:02d}/{m_n:02d}/{a_n}"
        nom_comp = f"{p['nom']} {p['ape']}"
        print(f"{p['cod']:<8} {p['dni']:<10} {nom_comp:<25} {f_str:<12} {p['sexo']:<5} {a}a {m}m {d}d")


def buscar_paciente(f_act):
    print("\n--- BUSQUEDA DE PACIENTE ---")
    if not paci_db:
        print("No hay pacientes registrados.")
        return

    busqueda = input("Ingrese DNI, Nombre o Apellido a buscar: ").strip().lower()
    hallados = []

    for p in paci_db.values():
        nom_comp = f"{p['nom']} {p['ape']}".lower()
        if busqueda in p["dni"] or busqueda in nom_comp:
            hallados.append(p)

    if not hallados:
        print(f"No se encontraron pacientes que coincidan con '{busqueda}'.")
        return

    print(f"\nSe encontraron {len(hallados)} coincidencia(s):")
    for p in hallados:
        a, m, d = calcular_edad(p["fnac"], f_act)
        r = resp_db.get(p["c_resp"])
        d_n, m_n, a_n = p["fnac"]

        print("\n" + "=" * 65)
        print("DATOS DEL PACIENTE")
        print(f" - Codigo: {p['cod']} | DNI: {p['dni']}")
        print(f" - Nombre Completo: {p['nom']} {p['ape']}")
        print(f" - Fecha de Nacimiento: {d_n:02d}/{m_n:02d}/{a_n}")
        print(f" - Sexo: {p['sexo']}")
        print(f" - Edad Exacta: {a} anos, {m} meses y {d} dias")
        print("-" * 65)
        print("DATOS COMPLETOS DEL RESPONSABLE ASOCIADO")
        if r:
            print(f" - {formato_resp(r)}")
        else:
            print(" - Informacion de responsable no disponible.")
        print("=" * 65)


def listar_responsables():
    print("\n--- LISTA DE RESPONSABLES REGISTRADOS ---")
    if not resp_db:
        print("No hay responsables registrados.")
        return
    for r in resp_db.values():
        print(f" - {formato_resp(r)}")

def menu():
    cargar_demo()
    f_act = (2, 10, 2026)

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
            reg_paciente(f_act)
        elif op == "2":
            reg_responsable()
        elif op == "3":
            listar_pacientes(f_act)
        elif op == "4":
            buscar_paciente(f_act)
        elif op == "5":
            listar_responsables()
        elif op == "6":
            print("\nSaliendo del programa...")
            break
        else:
            print("\nOpcion no valida. Intente nuevamente.")


if __name__ == "__main__":
    menu()
