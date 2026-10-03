
medicos = []


def listarMedico(medico):
    print(
        f"Codigo: {medico['codigo']}\n"
        f"CMP: {medico['CMP']}\n"
        f"Nombre: {medico['nombre']}\n"
        f"Apellido: {medico['apellido']}\n"
        f"Área o especialidad pediátrica: {medico['areaEspecialidad']}"
    )


def buscarMedicoCodigo():
    codigoIngresado = input("Coloque el código a buscar: ")

    encontrado = False

    for medico in medicos:
        if medico["codigo"] == codigoIngresado:
            print("\n¡Médico encontrado!")
            listarMedico(medico)
            encontrado = True

    if encontrado == False:
        print("* Médico no encontrado...")


def elegirEspecialidad():
    opcionValida = False
    opcion = ""

    while opcionValida == False:

        print("Especialidades:")
        print("     1. Pediatría general")
        print("     2. Neonatología")
        print("     3. Cardiología pediátrica")
        print("     4. Neumología pediátrica")
        print("     5. Gastroenterología pediátrica")

        opcion = input("Seleccione una especialidad: ")

        if opcion == "1":
            opcionValida = True
        elif opcion == "2":
            opcionValida = True
        elif opcion == "3":
            opcionValida = True
        elif opcion == "4":
            opcionValida = True
        elif opcion == "5":
            opcionValida = True
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


def buscarMedicoEspecialidad():

    print("\nSelecciona una especialidad para buscar médicos: ")

    especialidadBuscada = elegirEspecialidad()

    encontrado = False

    print(f"\nMédicos de {especialidadBuscada}:\n")

    for medico in medicos:
        if medico["areaEspecialidad"] == especialidadBuscada:
            listarMedico(medico)
            print()
            encontrado = True

    if encontrado == False:
        print("* No hay médicos registrados en esa especialidad.")


def registrarMedico():

    codigo = input("Ingrese código: ")

    CMPValido = False

    while CMPValido == False:

        CMP = int(input("Ingrese CMP: "))

        repetido = False

        if CMP < 0:
            print("* El CMP no puede ser negativo.")

        else:
            for medico in medicos:
                if medico["CMP"] == CMP:
                    repetido = True

            if repetido == True:
                print("* Ese CMP ya está registrado. Ingrese otro.")
            else:
                CMPValido = True

    nombre = input("Ingrese nombre: ")
    apellido = input("Ingrese apellido: ")

    areaEspecialidad = elegirEspecialidad()

    nuevoMedico = {
        "codigo": codigo,
        "CMP": CMP,
        "nombre": nombre,
        "apellido": apellido,
        "areaEspecialidad": areaEspecialidad
    }

    medicos.append(nuevoMedico) # linea muy importante de nuevo porque
                                # hace que todo nuevoMedico se añada
                                # a la lista completa de medicos

    print("Médico registrado correctamente.\n")


def mostrarListaMedicos():

    print("\nLista completa de médicos:\n")

    for medico in medicos:
        listarMedico(medico)
        print()


def modificarCMP(medico):

    CMPValido = False

    while CMPValido == False:

        nuevoCMP = int(input("Ingrese nuevo CMP: "))

        repetido = False

        if nuevoCMP < 0:
            print("* El CMP no puede ser negativo.")

        else:
            for otroMedico in medicos:

                if (
                    otroMedico["CMP"] == nuevoCMP
                    and otroMedico["codigo"] != medico["codigo"]
                ):
                    repetido = True

            if repetido == True:
                print("* Ese CMP ya está registrado. Ingrese otro.")

            else:
                medico["CMP"] = nuevoCMP
                CMPValido = True

                print("\nMédico modificado correctamente.")


def modificarMedico():

    codigoIngresado = input(
        "Ingrese el código del médico a modificar: "
    )

    encontrado = False

    for medico in medicos:

        if medico["codigo"] == codigoIngresado:

            encontrado = True

            print("\n¿Qué desea modificar?")
            print("     1. Nombre")
            print("     2. Apellido")
            print("     3. Especialidad")
            print("     4. CMP")

            opcion = input("Modificar: ")

            if opcion == "1":

                medico["nombre"] = input(
                    "Ingrese nuevo nombre: "
                )

                print("\nMédico modificado correctamente.")

            elif opcion == "2":

                medico["apellido"] = input(
                    "Ingrese nuevo apellido: "
                )

                print("\nMédico modificado correctamente.")

            elif opcion == "3":

                medico["areaEspecialidad"] = elegirEspecialidad()

                print("\nMédico modificado correctamente.")

            elif opcion == "4":

                modificarCMP(medico)

            else:
                print("* Opción inválida.")

    if encontrado == False:
        print("* Médico no encontrado.\n")

######################
# programa principal #
######################

numeroValido = False

while numeroValido == False:

    numeroMedicosRegistrar = int(
        input("Ingrese el numero de medicos a registrar: ")
    )

    if numeroMedicosRegistrar > 0:
        numeroValido = True
    else:
        print("* Debes ingresar un número mayor que 0.\n")


for numero in range(numeroMedicosRegistrar):
    registrarMedico()


mostrarListaMedicos()


buscar = input(
    "¿Desea buscar médicos? (1 = Sí, 2 = No): "
)

if buscar == "1":

    print("\n¿Cómo desea buscar?")
    print("     1. Código")
    print("     2. Especialidad")

    opcionBuscar = input("Seleccione una opción: ")

    if opcionBuscar == "1":
        buscarMedicoCodigo()

    elif opcionBuscar == "2":
        buscarMedicoEspecialidad()

    else:
        print("* Opción inválida.")


modificar = input(
    "¿Desea modificar la información "
    "de algún médico? (1 = Sí, 2 = No): "
)

if modificar == "1":
    modificarMedico()