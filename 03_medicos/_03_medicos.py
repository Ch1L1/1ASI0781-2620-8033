
medicos = []

class Medico:
    def __init__( 
        self, codigo, CMP, nombre, 
        apellido, areaEspecialidad
    ):
        self.codigo = codigo
        self.CMP = CMP
        self.nombre = nombre
        self.apellido = apellido
        self.areaEspecialidad = areaEspecialidad


    def listarMedico(self): # listar médico INDIVIDUAL
                            # (todos sus datos, por eso está dentro de la clase)
        print(
            f"Codigo: {self.codigo}\nCMP:{self.CMP}"
            f"\nNombre: {self.nombre}\nApellido: {self.apellido}"
            f"\nÁrea o especialidad pediátrica: {self.areaEspecialidad}"
        
        )



def buscarMedicoCodigo(): # FUERA DE LA CLASE: buscamos un
                          # médico del TOTAL de la lista de medicos.
    codigoIngresado = input("Coloque el código a buscar: ")

    encontrado = False

    for medico in medicos:
        if medico.codigo == codigoIngresado:
            print("\n¡Médico encontrado!")
            medico.listarMedico()
            encontrado = True

    if encontrado == False:
        print("* Médico no encontrado...")



def elegirEspecialidad():
    while True:

        print("Especialidades:")
        print("     1. Pediatría general")
        print("     2. Neonatología")
        print("     3. Cardiología")
        print("     4. Neumología")
        print("     5. Gastroenterología")

        opcion = input("Seleccione una especialidad: ")

        match opcion:
            case "1":
                return "Pediatría general"
            case "2":
                return "Neonatología"
            case "3":
                return "Cardiología"
            case "4":
                return "Neumología"
            case "5":
                return "Gastroenterología"
            case _:
                print("* Opción inválida. Intente nuevamente.\n")



def buscarMedicoEspecialidad():
    print("\nSelecciona una especialidad para buscar médicos: ")
    especialidadBuscada = elegirEspecialidad()

    encontrado = False

    print(f"\nMédicos de {especialidadBuscada}:\n")

    for medico in medicos:
        if medico.areaEspecialidad == especialidadBuscada:
            medico.listarMedico()
            print()
            encontrado = True

    if encontrado == False:
        print("* No hay médicos registrados en esa especialidad.")



def registrarMedico(): # FUERA DE LA CLASE: registramos un medico y
                       # lo metemos en la lista medicos (con los otros)

    codigo = input("Ingrese código: ")

    while True:
        CMP = int(input("Ingrese CMP: "))

        repetido = False

        if CMP < 0:
            print("* El CMP no puede ser negativo.")

        else:
            for medico in medicos:
                if medico.CMP == CMP:
                    repetido = True # cuando encuentra un CMP repetido
            
            if repetido == True:
                print("* Ese CMP ya está registrado. Ingrese otro.")

            if repetido == False:
                break
    
    nombre = input("Ingrese nombre: ")
    apellido = input("Ingrese apellido: ")
    areaEspecialidad = elegirEspecialidad()

    nuevoMedico = Medico(
        codigo,
        CMP,
        nombre,
        apellido,
        areaEspecialidad
    )

    medicos.append(nuevoMedico)

    print("Médico registrado correctamente.\n")



def mostrarListaMedicos():
    print("\nLista completa de médicos:\n")
    for medico in medicos:
        medico.listarMedico()
        print()



def modificarMedico():

    codigoIngresado = input("Ingrese el código del médico a modificar: ")

    encontrado = False

    for medico in medicos:
        if medico.codigo == codigoIngresado:

            encontrado = True

            print("\n¿Qué desea modificar?")
            print("     1. Nombre")
            print("     2. Apellido")
            print("     3. Especialidad")
            print("     4. CMP")

            opcion = input("Modificar: ")

            match opcion:
                case "1":
                    medico.nombre = input("Ingrese nuevo nombre: ")
                    print("\nMédico modificado correctamente.")
                case "2":
                    medico.apellido = input("Ingrese nuevo apellido: ")
                    print("\nMédico modificado correctamente.")
                case "3":
                    medico.areaEspecialidad = elegirEspecialidad()
                    print("\nMédico modificado correctamente.")
                case "4":
                    while True:
                        nuevoCMP = int(input("Ingrese nuevo CMP: "))

                        repetido = False

                        if nuevoCMP < 0:
                            print("* El CMP no puede ser negativo.")

                        else:
                            for otroMedico in medicos:
                                # si otro médico tiene ese mismo CMP
                                # *AND* no es el médico que estamos modificando
                                if (
                                    otroMedico.CMP == nuevoCMP
                                    and otroMedico.codigo != medico.codigo
                                ):
                                    repetido = True

                            if repetido == True:
                                print("* Ese CMP ya está registrado. Ingrese otro.")

                            if repetido == False:
                                medico.CMP = nuevoCMP
                                print("\nMédico modificado correctamente.")
                                break

                case _:
                    print("* Opción inválida.")


    if encontrado == False:
        print("* Médico no encontrado.\n")



# pedir el numero de medicos a registrar.. si desea
# buscar médicos y si desea modificar informacion de
# algun médico mediante su código

while True:

    numeroMedicosRegistrar = int(
        input("Ingrese el numero de medicos a registrar: ")
    )

    if numeroMedicosRegistrar > 0:
        break

    print("* Debes ingresar un número mayor que 0.\n")

for numero in range(numeroMedicosRegistrar):
    registrarMedico()

mostrarListaMedicos()

buscar = input("¿Desea buscar médicos? (1 = Sí, 2 = No): ")

if buscar == "1":

    print("\n¿Cómo desea buscar?")
    print("     1. Código")
    print("     2. Especialidad")

    buscar = input("Seleccione una opción: ")

    match buscar:
        case "1":
            buscarMedicoCodigo()
        case "2":
            buscarMedicoEspecialidad()

        case _: # esto por si la respuesta no está en los CASE
            print("* Opción inválida.")

modificar = input(
    "¿Desea modificar la información"
    " de algún médico? (1 = Sí, 2 = No): "
)
if modificar == "1":
    modificarMedico()
