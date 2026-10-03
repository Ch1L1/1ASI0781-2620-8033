from datos import responsables


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


# ---------- FUNCIONES PRINCIPALES ----------
def muestra_resp(r):
    print("Código     :", r["codigo"])
    print("DNI        :", r["dni"])
    print("Nombre     :", r["nombres"], r["apellidos"])
    print("Teléfono   :", r["telefono"])
    print("Parentesco :", r["parentesco"])
    print("-" * 35)


def reg_resp(lista):
    print("\n" + "=" * 35)
    print("     REGISTRAR RESPONSABLE")
    print("=" * 35)

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
    print("\n" + "=" * 35)
    print("     LISTA DE RESPONSABLES")
    print("=" * 35)

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
    return None


def busca_resp_cod(lista, codigo):
    for r in lista:
        if r["codigo"] == codigo:
            return r
    return None


def cambia_tel(lista):
    print("\n" + "=" * 35)
    print("       MODIFICAR TELÉFONO")
    print("=" * 35)

    dni = input("DNI del responsable: ")
    r = busca_resp_dni(lista, dni)

    if r is None:
        print("[ERROR] No existe un responsable con ese DNI.")
        return

    print("Teléfono actual:", r["telefono"])
    r["telefono"] = input("Nuevo teléfono: ")
    print("[OK] Teléfono actualizado.")


def pacientes_resp(lista_resp, lista_pac):
    print("\n" + "=" * 35)
    print("   PACIENTES DEL RESPONSABLE")
    print("=" * 35)

    dni = input("DNI del responsable: ")
    r = busca_resp_dni(lista_resp, dni)

    if r is None:
        print("[ERROR] No existe un responsable con ese DNI.")
        return

    print("Responsable:", r["nombres"], r["apellidos"])
    cont = 0
    for p in lista_pac:
        if p["codigo_responsable"] == r["codigo"]:
            print("  -", p["nombres"], p["apellidos"])
            cont = cont + 1

    if cont == 0:
        print("Este responsable no tiene pacientes asociados.")


# ---------- MENÚ ----------
def menu_resp(lista_resp, lista_pac):
    opcion = ""
    while opcion != "6":
        print("\n" + "=" * 35)
        print("     GESTIÓN DE RESPONSABLES")
        print("=" * 35)
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
            if r is None:
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
