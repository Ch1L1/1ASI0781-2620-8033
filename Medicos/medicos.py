
from datos import medicos


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
        print("* Médico no encontrado...")


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
            print("* Opción inválida. Intente nuevamente.\n")

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
        print("* No hay médicos registrados en esa especialidad.")


def registra_medico():
    codigo = input("Ingrese código (Enter para terminar): ").strip()
    if not codigo:
        print("Registro de médicos finalizado.\n")
        return False

    cmp_valido = False

    while not cmp_valido:
        cmp = int(input("Ingrese CMP: "))
        rep = False

        if cmp < 0:
            print("* El CMP no puede ser negativo.")
        else:
            for medico in medicos:
                if medico["cmp"] == cmp:
                    rep = True

            if rep:
                print("* Ese CMP ya está registrado. Ingrese otro.")
            else:
                cmp_valido = True

    nombres = input("Ingrese nombre: ")
    apellidos = input("Ingrese apellido: ")
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

    while not cmp_valido:
        nuevo_cmp = int(input("Ingrese nuevo CMP: "))
        rep = False

        if nuevo_cmp < 0:
            print("* El CMP no puede ser negativo.")
        else:
            for otro in medicos:
                if otro["cmp"] == nuevo_cmp and otro["codigo"] != medico["codigo"]:
                    rep = True

            if rep:
                print("* Ese CMP ya está registrado. Ingrese otro.")
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
                medico["nombres"] = input("Ingrese nuevo nombre: ")
                print("\nMédico modificado correctamente.")
            elif opcion == "2":
                medico["apellidos"] = input("Ingrese nuevo apellido: ")
                print("\nMédico modificado correctamente.")
            elif opcion == "3":
                medico["especialidad"] = elige_especial()
                print("\nMédico modificado correctamente.")
            elif opcion == "4":
                modifica_cmp(medico)
            else:
                print("* Opción inválida.")

    if not found:
        print("* Médico no encontrado.\n")


def menu_medicos():
    while True:
        print("\n=== GESTIÓN DE MÉDICOS ===")
        print("1. Registrar médico")
        print("2. Listar médicos")
        print("3. Buscar médico por código")
        print("4. Buscar médicos por especialidad")
        print("5. Modificar médico")
        print("6. Volver al menú principal")
        opcion = input("Seleccione opción: ").strip()

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
            print("* Opción inválida.")


if __name__ == "__main__":
    menu_medicos()