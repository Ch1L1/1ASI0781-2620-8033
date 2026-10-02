class ReportesClinica:
    def __init__(self, lista_consultas, lista_pacientes, lista_medicos):
        self.consultas = lista_consultas
        self.pacientes = lista_pacientes
        self.medicos = lista_medicos

    def listarPacientesGeneral(self):
        print("LISTADO GENERAL DE PACIENTES:\n")
        for p in self.pacientes:
            print(f"Código: {p['codigo']} | DNI: {p['dni']} | Nombre: {p['nombres']} {p['apellidos']} | Nacimiento: {p['fecha_nacimiento']}")

    def listarMedicosGeneral(self):
        print("LISTADO GENERAL DE MÉDICOS:\n")
        for m in self.medicos:
            print(f"Código: {m['codigo']} | CMP: {m['cmp']} | Nombre: {m['nombres']} {m['apellidos']} | Especialidad: {m['especialidad']}")

    def pacientesAtendidosPorMedico(self):
        cod_med = input("Ingrese el código del médico: ")
        print(f"PACIENTES ATENDIDOS POR EL MÉDICO: {cod_med}\n")
        
        pacientes_vistos = []
        for c in self.consultas:
            if c['Codigo Medico'] == cod_med:
                cod_pac = c['Codigo Paciente']
                encontrado = False
                for p_visto in pacientes_vistos:
                    if p_visto == cod_pac:
                        encontrado = True
                        break
                if not encontrado:
                    pacientes_vistos.append(cod_pac)

        for cod_pac in pacientes_vistos:
            for p in self.pacientes:
                if p['codigo'] == cod_pac:
                    print(f"- {p['nombres']} {p['apellidos']} (Código: {p['codigo']})")

    def historialConsultasPaciente(self):
        cod_pac = input("Ingrese el código del paciente: ")
        print(f"HISTORIAL DE CONSULTAS DEL PACIENTE: {cod_pac}\n")
        
        contador = 0
        for c in self.consultas:
            if c['Codigo Paciente'] == cod_pac:
                print(f"Fecha: {c['Fecha']} | Motivo: {c['Motivo']} | Costo: ${c['Costo']} | Peso: {c['Peso']}kg")
                contador = contador + 1
                
        if contador == 0:
            print("El paciente no tiene consultas registradas.")

    def cantidadTotalConsultas(self):
        contador = 0
        for c in self.consultas:
            contador = contador + 1
        print(f"\nCantidad total de consultas realizadas: {contador}")

    def consultasPorMedico(self):
        print("\n--- CANTIDAD DE CONSULTAS POR MÉDICO ---")
        for m in self.medicos:
            cod_med = m['codigo']
            contador = 0
            for c in self.consultas:
                if c['Codigo Medico'] == cod_med:
                    contador = contador + 1
            print(f"Médico: {m['nombres']} {m['apellidos']} ({cod_med}) -> {contador} consultas")

    def ingresoTotalConsultas(self):
        total = 0
        for c in self.consultas:
            total = total + c['Costo']
        print(f"\nIngreso total generado por consultas: ${total}")

    def promedioCostoConsultas(self):
        total_consultas = 0
        suma_costos = 0
        for c in self.consultas:
            total_consultas = total_consultas + 1
            suma_costos = suma_costos + c['Costo']
            
        if total_consultas == 0:
            print("\nPromedio del costo de las consultas: $0")
        else:
            promedio = suma_costos / total_consultas
            print(f"\nPromedio del costo de las consultas: ${promedio}")

    def pacienteMayorConsultas(self):
        if not self.consultas:
            print("\nNo hay consultas registradas.")
            return
            
        max_consultas = 0
        paciente_ganador = "Ninguno"
        
        for p in self.pacientes:
            cod_pac = p['codigo']
            contador = 0
            for c in self.consultas:
                if c['Codigo Paciente'] == cod_pac:
                    contador = contador + 1
                    
            if contador > max_consultas:
                max_consultas = contador
                paciente_ganador = f"{p['nombres']} {p['apellidos']} ({cod_pac})"
                
        print(f"\nPaciente con mayor cantidad de consultas: {paciente_ganador} con {max_consultas} consultas.")

    def pacientesPorRangoEdad(self):
        rango_0_2 = 0
        rango_3_5 = 0
        rango_6_11 = 0
        rango_12_17 = 0
        
        for p in self.pacientes:
            anio_nacimiento = int(p['fecha_nacimiento'][:4])
            edad = 2026 - anio_nacimiento
            
            if 0 <= edad <= 2:
                rango_0_2 = rango_0_2 + 1
            elif 3 <= edad <= 5:
                rango_3_5 = rango_3_5 + 1
            elif 6 <= edad <= 11:
                rango_6_11 = rango_6_11 + 1
            elif 12 <= edad <= 17:
                rango_12_17 = rango_12_17 + 1
                
        print("\nDISTRIBUCIÓN DE PACIENTES SEGÚN EDAD")
        print(f"De 0 a 2 años: {rango_0_2} pacientes")
        print(f"De 3 a 5 años: {rango_3_5} pacientes")
        print(f"De 6 a 11 años: {rango_6_11} pacientes")
        print(f"De 12 a 17 años: {rango_12_17} pacientes")

    # Reporte Adicional 1: Consultas realizadas en una fecha específica
    def reporteConsultasPorFecha(self):
        fecha_buscada = input("\nIngrese la fecha que desea buscar (ej. 2026-06-06): ")
        contador = 0
        
        print(f"--- CONSULTAS EN LA FECHA: {fecha_buscada} ---")
        for c in self.consultas:
            if c['Fecha'] == fecha_buscada:
                print(f"Código: {c['Codigo']} | Paciente: {c['Codigo Paciente']} | Médico: {c['Codigo Medico']} | Costo: ${c['Costo']}")
                contador = contador + 1
        print(f"Total de consultas en esta fecha: {contador}")

    # Reporte Adicional 2: Ingresos generados por un médico específico
    def reporteIngresosPorMedico(self):
        medico_buscado = input("\nIngrese el código del médico a consultar: ")
        ingreso_total_medico = 0
        cantidad_atenciones = 0
        
        for c in self.consultas:
            if c['Codigo Medico'] == medico_buscado:
                ingreso_total_medico = ingreso_total_medico + c['Costo']
                cantidad_atenciones = cantidad_atenciones + 1
                
        print(f"REPORTE FINANCIERO DEL MÉDICO: {medico_buscado}")
        print(f"Total de pacientes atendidos: {cantidad_atenciones}")
        print(f"Ingreso total generado: ${ingreso_total_medico}")

# MOCK DATA - will delete it when everyone implement everything

medicos_prueba = [
    {"codigo": "M001", "cmp": "12345", "nombres": "Carlos", "apellidos": "Pérez", "especialidad": "Pediatría general"},
    {"codigo": "M002", "cmp": "67890", "nombres": "María", "apellidos": "Gómez", "especialidad": "Neonatología"}
]

pacientes_prueba = [
    {"codigo": "P001", "dni": "11111111", "nombres": "Juanito", "apellidos": "Quispe", "fecha_nacimiento": "2024-05-10"},
    {"codigo": "P002", "dni": "22222222", "nombres": "Anita", "apellidos": "Rojas", "fecha_nacimiento": "2020-03-15"},
    {"codigo": "P003", "dni": "33333333", "nombres": "Pepito", "apellidos": "Mamani", "fecha_nacimiento": "2012-08-20"} 
]

consultas_prueba = [
    {"Codigo": "C001", "Codigo Paciente": "P001", "Codigo Medico": "M001", "Fecha": "2026-06-06", "Motivo": "Fiebre", "Peso": 12.5, "Talla": 85.0, "Observaciones": "Leve", "Costo": 50.0},
    {"Codigo": "C002", "Codigo Paciente": "P001", "Codigo Medico": "M001", "Fecha": "2026-06-10", "Motivo": "Control", "Peso": 13.0, "Talla": 87.0, "Observaciones": "Sano", "Costo": 40.0},
    {"Codigo": "C003", "Codigo Paciente": "P002", "Codigo Medico": "M002", "Fecha": "2026-06-06", "Motivo": "Tos", "Peso": 20.0, "Talla": 110.0, "Observaciones": "Bronquios", "Costo": 60.0}
]

mis_reportes = ReportesClinica(consultas_prueba, pacientes_prueba, medicos_prueba)

mis_reportes.listarPacientesGeneral()
mis_reportes.listarMedicosGeneral()
mis_reportes.cantidadTotalConsultas()
mis_reportes.ingresoTotalConsultas()
mis_reportes.promedioCostoConsultas()
mis_reportes.pacienteMayorConsultas()
mis_reportes.pacientesPorRangoEdad()
mis_reportes.reporteConsultasPorFecha()
mis_reportes.reporteIngresosPorMedico()