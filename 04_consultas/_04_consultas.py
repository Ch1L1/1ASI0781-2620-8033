class Consultas:
    def __init__(self, codigo="", codigo_paciente="", codigo_medico="", fecha="", motivo="", peso=0.0, talla=0.0, observaciones="", costo=0.0):
        self.codigo = codigo
        self.codigo_paciente = codigo_paciente
        self.codigo_medico = codigo_medico
        self.fecha = fecha
        self.motivo = motivo
        self.peso = peso
        self.talla = talla
        self.observaciones = observaciones
        self.costos = costo

        #Metodos de validación
    def buscarMedicoCodigo(self, medicos_lista): 
        encontrado = False
        for medico in medicos_lista:
            if medico['codigo'] == self.codigo_medico:
                print("\n¡Médico encontrado!")
                encontrado = True
                break

        if not encontrado:
            print("* Médico no encontrado...")
        return encontrado 

    def buscarPacienteCodigo(self, pacientes_lista): 
        encontrado = False
        for paciente in pacientes_lista:
            if paciente['codigo'] == self.codigo_paciente:
                print("\n¡Paciente encontrado!")
                encontrado = True
                break

        if not encontrado:
            print("* Paciente no encontrado...")
        return encontrado 

    def verificarCodigoConsulta(self, lista_consultas):
        encontrado = True
        for consulta in lista_consultas:
            if self.codigo == consulta['Codigo']:
                print('¡Este codigo ya existe!')
                encontrado = False
                break

        if encontrado:
            print('Codigo valido')
        return encontrado

    #Metodo de ingreso
    def ingresarConsulta(self, lista_consultas, pacientes_lista, medicos_lista):
        self.codigo = input("Ingrese codigo de la consulta: ")
        
        if not self.verificarCodigoConsulta(lista_consultas):
            return

        self.codigo_paciente = input("Ingrese codigo del paciente: ")
        if not self.buscarPacienteCodigo(pacientes_lista):
            print("No se puede registrar: El paciente no existe.")
            return

        self.codigo_medico = input("Ingrese codigo del medico: ")
        if not self.buscarMedicoCodigo(medicos_lista):
            print("No se puede registrar: El médico no existe.")
            return

        self.fecha = input("Ingrese fecha de la consulta: ")
        self.motivo = input("Ingrese el motivo de la consulta: ")

        self.peso = float(input("Ingrese el peso del paciente: "))
        if self.peso <= 0:
            print("ERROR, el peso ingresado no es válido")
            return

        self.talla = float(input("Ingrese la talla del paciente: "))
        if self.talla <= 0:
            print("ERROR, la talla ingresada no es válida")
            return

        self.observaciones = input("Ingrese observaciones requeridas: ")

        self.costos = float(input("Ingrese el costo de la consulta: "))
        if self.costos <= 0:
            print ("ERROR, el costo de la consulta debe ser mayor a 0")
            return

        nueva_consulta = {
            "Codigo": self.codigo,
            "Codigo Paciente": self.codigo_paciente,
            "Codigo Medico": self.codigo_medico,
            "Fecha": self.fecha,
            "Motivo": self.motivo,
            "Peso": self.peso,
            "Talla": self.talla,
            "Observaciones": self.observaciones,
            "Costo": self.costos,
        }      
        lista_consultas.append(nueva_consulta)
        print("Consulta guardada con éxito!")


pacientes = [{"codigo": "P001", "nombres": "Juan"}]
medicos = [{"codigo": "M001", "nombres": "Dr. House"}]
mis_consultas = []

c = Consultas()
c.ingresarConsulta(mis_consultas, pacientes, medicos)

print("\n--- LISTA FINAL DE CONSULTAS ---")
print(mis_consultas)