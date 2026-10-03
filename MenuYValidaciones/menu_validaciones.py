def validar_opcion(opcion, minimo, maximo):
    if opcion.isdigit():
        numero = int(opcion)

        if numero >= minimo and numero <= maximo:
            return True

    return False


def validar_dni(dni):
    if dni.isdigit() and len(dni) == 8:
        return True

    return False


def validar_nombre(nombre):
    if nombre.strip() != "":
        return True

    return False


def validar_edad(edad):
    if edad.isdigit():
        numero = int(edad)

        if numero >= 0 and numero <= 17:
            return True

    return False


def menu_principal():
    while True:
        print("\n==============================")
        print("   CLÍNICA PEDIÁTRICA")
        print("==============================")
        print("1. Pacientes")
        print("2. Médicos")
        print("3. Responsables")
        print("4. Consultas")
        print("5. Reportes")
        print("6. Salir")

        opcion = input("\nSeleccione una opción: ")

        if not validar_opcion(opcion, 1, 6):
            print("Opción inválida.")
            continue

        if opcion == "1":
            print("\nIngresando al módulo de pacientes...")

        elif opcion == "2":
            print("\nIngresando al módulo de médicos...")

        elif opcion == "3":
            print("\nIngresando al módulo de responsables...")

        elif opcion == "4":
            print("\nIngresando al módulo de consultas...")

        elif opcion == "5":
            print("\nIngresando al módulo de reportes...")

        elif opcion == "6":
            print("\nSaliendo del sistema...")
            break


menu_principal()