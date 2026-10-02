def buscar_medico_codigo(medicos_lista, codigo_medico):
    for medico in medicos_lista:
        if medico['codigo'] == codigo_medico:
            print("\n¡Médico encontrado!")
            return True

    print("* Médico no encontrado...")
    return False


def buscar_paciente_codigo(pacientes_lista, codigo_paciente):
    for paciente in pacientes_lista:
        if paciente['codigo'] == codigo_paciente:
            print("\n¡Paciente encontrado!")
            return True

    print("* Paciente no encontrado...")
    return False


def verificar_codigo_consulta(lista_consultas, codigo_consulta):
    for consulta in lista_consultas:
        if codigo_consulta == consulta['Codigo']:
            print("¡Este codigo ya existe!")
            return False

    print("Codigo valido")
    return True


def ingresar_consulta(lista_consultas, pacientes_lista, medicos_lista):
    codigo = input("Ingrese codigo de la consulta: ")
    if not verificar_codigo_consulta(lista_consultas, codigo):
        return

    codigo_paciente = input("Ingrese codigo del paciente: ")
    if not buscar_paciente_codigo(pacientes_lista, codigo_paciente):
        print("No se puede registrar: El paciente no existe.")
        return

    codigo_medico = input("Ingrese codigo del medico: ")
    if not buscar_medico_codigo(medicos_lista, codigo_medico):
        print("No se puede registrar: El médico no existe.")
        return

    fecha = input("Ingrese fecha de la consulta: ")
    motivo = input("Ingrese el motivo de la consulta: ")

    peso = float(input("Ingrese el peso del paciente: "))
    if peso <= 0:
        print("ERROR, el peso ingresado no es válido")
        return

    talla = float(input("Ingrese la talla del paciente: "))
    if talla <= 0:
        print("ERROR, la talla ingresada no es válida")
        return

    observaciones = input("Ingrese observaciones requeridas: ")

    costo = float(input("Ingrese el costo de la consulta: "))
    if costo <= 0:
        print("ERROR, el costo de la consulta debe ser mayor a 0")
        return

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


def ejecutar_demo():
    pacientes = [{"codigo": "P001", "nombres": "Juan"}]
    medicos = [{"codigo": "M001", "nombres": "Dr. House"}]
    mis_consultas = []

    ingresar_consulta(mis_consultas, pacientes, medicos)

    print("\n--- LISTA FINAL DE CONSULTAS ---")
    print(mis_consultas)


if __name__ == "__main__":
    ejecutar_demo()