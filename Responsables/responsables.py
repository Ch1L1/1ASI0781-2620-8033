class Responsable:
    def __init__(self, codigo, dni, nombres, apellidos, telefono, parentesco):
        self.codigo = codigo
        self.dni = dni
        self.nombres = nombres
        self.apellidos = apellidos
        self.telefono = telefono
        self.parentesco = parentesco

    def mostrar_datos(self):
        print("Código     :", self.codigo)
        print("DNI        :", self.dni)
        print("Nombre     :", self.nombres, self.apellidos)
        print("Teléfono   :", self.telefono)
        print("Parentesco :", self.parentesco)
        print("-" * 35)


# Lista donde guardamos los objetos Responsable (memoria)
responsables = []


# ---------- VALIDACIONES ----------
def texto_vacio(texto):
    return texto == ""


def dni_duplicado(lista, dni):
    for r in lista:
        if r.dni == dni:
            return True
    return False


def codigo_duplicado(lista, codigo):
    for r in lista:
        if r.codigo == codigo:
            return True
    return False


# ---------- FUNCIONES PRINCIPALES ----------
def registrar_responsable(lista):
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

    # Creamos el objeto y lo guardamos en la lista
    nuevo = Responsable(codigo, dni, nombres, apellidos, telefono, parentesco)
    lista.append(nuevo)
    print("[OK] Responsable registrado correctamente.")


def listar_responsables(lista):
    print("\n" + "=" * 35)
    print("     LISTA DE RESPONSABLES")
    print("=" * 35)

    if len(lista) == 0:
        print("No hay responsables registrados.")
        return

    for r in lista:
        r.mostrar_datos()
    print("Total:", len(lista), "responsable(s)")


def buscar_responsable_por_dni(lista, dni):
    for r in lista:
        if r.dni == dni:
            return r
    return None


def buscar_responsable_por_codigo(lista, codigo):
    # La usará el compañero de pacientes para ver si el responsable existe
    for r in lista:
        if r.codigo == codigo:
            return r
    return None


def modificar_telefono(lista):
    print("\n" + "=" * 35)
    print("       MODIFICAR TELÉFONO")
    print("=" * 35)

    dni = input("DNI del responsable: ")
    r = buscar_responsable_por_dni(lista, dni)

    if r is None:
        print("[ERROR] No existe un responsable con ese DNI.")
        return

    print("Teléfono actual:", r.telefono)
    r.telefono = input("Nuevo teléfono: ")
    print("[OK] Teléfono actualizado.")


def pacientes_de_responsable(lista_responsables, lista_pacientes):
    print("\n" + "=" * 35)
    print("   PACIENTES DEL RESPONSABLE")
    print("=" * 35)

    dni = input("DNI del responsable: ")
    r = buscar_responsable_por_dni(lista_responsables, dni)

    if r is None:
        print("[ERROR] No existe un responsable con ese DNI.")
        return

    print("Responsable:", r.nombres, r.apellidos)
    contador = 0
    for p in lista_pacientes:
        if p["codigo_responsable"] == r.codigo:
            print("  -", p["nombres"], p["apellidos"])
            contador = contador + 1

    if contador == 0:
        print("Este responsable no tiene pacientes asociados.")


# ---------- MENÚ ----------
def menu_responsables(lista_responsables, lista_pacientes):
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
            registrar_responsable(lista_responsables)
        elif opcion == "2":
            listar_responsables(lista_responsables)
        elif opcion == "3":
            dni = input("DNI a buscar: ")
            r = buscar_responsable_por_dni(lista_responsables, dni)
            if r is None:
                print("[ERROR] No se encontró el responsable.")
            else:
                r.mostrar_datos()
        elif opcion == "4":
            modificar_telefono(lista_responsables)
        elif opcion == "5":
            pacientes_de_responsable(lista_responsables, lista_pacientes)
        elif opcion == "6":
            print("Hasta pronto.")
        else:
            print("[ERROR] Opción no válida.")
