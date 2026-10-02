from datetime import datetime, date

class Responsable:
    """Clase que representa al tutor o responsable del paciente."""
    def __init__(self, codigo: str, dni: str, nombres: str, apellidos: str, telefono: str, parentesco: str):
        self.codigo = codigo.strip().upper()
        self.dni = dni.strip()
        self.nombres = nombres.strip().title()
        self.apellidos = apellidos.strip().title()
        self.telefono = telefono.strip()
        self.parentesco = parentesco.strip().capitalize()

    def mostrar_datos(self) -> str:
        return (f"Codigo: {self.codigo} | DNI: {self.dni} | "
                f"Nombre: {self.nombres} {self.apellidos} | "
                f"Telefono: {self.telefono} | Parentesco: {self.parentesco}")


class Paciente:
    """Clase que representa a un paciente registrado."""
    def __init__(self, codigo: str, dni: str, nombres: str, apellidos: str, fecha_nacimiento: date, sexo: str, cod_responsable: str):
        self.codigo = codigo.strip().upper()
        self.dni = dni.strip()
        self.nombres = nombres.strip().title()
        self.apellidos = apellidos.strip().title()
        self.fecha_nacimiento = fecha_nacimiento
        self.sexo = sexo.strip().upper()
        self.cod_responsable = cod_responsable.strip().upper()

    def calcular_edad_exacta(self) -> tuple:
        """Calcula la edad exacta en años, meses y días respecto a la fecha actual."""
        hoy = date.today()
        anos = hoy.year - self.fecha_nacimiento.year
        meses = hoy.month - self.fecha_nacimiento.month
        dias = hoy.day - self.fecha_nacimiento.day

        if dias < 0:
            meses -= 1
            mes_anterior = hoy.month - 1 if hoy.month > 1 else 12
            ano_ajuste = hoy.year if hoy.month > 1 else hoy.year - 1
            dias += (date(ano_ajuste, mes_anterior % 12 + 1, 1) - date(ano_ajuste, mes_anterior, 1)).days

        if meses < 0:
            anos -= 1
            meses += 12

        return anos, meses, dias

    def obtener_resumen_linea(self) -> str:
        anos, meses, dias = self.calcular_edad_exacta()
        f_nac = self.fecha_nacimiento.strftime("%d/%m/%Y")
        return f"{self.codigo:<8} {self.dni:<10} {self.nombres + ' ' + self.apellidos:<25} {f_nac:<12} {self.sexo:<5} {anos}a {meses}m {dias}d"


class SistemaHospital:
    def __init__(self):
        self.responsables = {}
        self.pacientes = {}

    def cargar_datos_demo(self):
        """Carga datos de prueba iniciales."""
        r1 = Responsable("RESP01", "09876543", "Carlos", "Mendoza Rios", "987654321", "Padre")
        r2 = Responsable("RESP02", "11223344", "Maria", "Gomez Perales", "912345678", "Madre")
        self.responsables[r1.codigo] = r1
        self.responsables[r2.codigo] = r2

    def registrar_responsable(self):
        """Registra un responsable validando DNI y Telefono con len y try-except."""
        print("\n--- REGISTRO DE RESPONSABLE ---")
        cod = input("Codigo del responsable: ").strip().upper()
        if cod in self.responsables:
            print("ERROR: Ya existe un responsable registrado con ese codigo.")
            return


        while True:
            dni = input("DNI (8 digitos): ").strip()
            if len(dni) == 8:
                try:
                    int(dni) 
                    break
                except ValueError:
                    print("ERROR: El DNI debe contener solo numeros.")
            else:
                print("ERROR: El DNI debe tener exactamente 8 digitos.")

        nombres = input("Nombres: ").strip()
        apellidos = input("Apellidos: ").strip()

     
        while True:
            telefono = input("Telefono (9 digitos, inicia con 9): ").strip()
            if len(telefono) == 9 and telefono[0] == "9":
                try:
                    int(telefono)  
                    break
                except ValueError:
                    print("ERROR: El telefono debe contener solo numeros.")
            else:
                print("ERROR: El telefono debe tener 9 digitos y comenzar con 9.")

        parentesco = input("Parentesco (Padre, Madre, Tutor, etc.): ").strip()

        nuevo_resp = Responsable(cod, dni, nombres, apellidos, telefono, parentesco)
        self.responsables[cod] = nuevo_resp
        print(f"Responsable '{nuevo_resp.nombres} {nuevo_resp.apellidos}' registrado con exito.")

    def registrar_paciente(self):
        """Registra un paciente con validacion de DNI con len y try-except."""
        print("\n--- REGISTRO DE NUEVO PACIENTE ---")
        
        cod_resp = input("Ingrese el Codigo del Responsable: ").strip().upper()
        if cod_resp not in self.responsables:
            print(f"ERROR: El codigo de responsable '{cod_resp}' NO existe en el sistema.")
            print("Debe registrar primero al responsable (Opcion 2) o verificar el codigo.")
            return

        cod = input("Codigo del Paciente: ").strip().upper()
        if cod in self.pacientes:
            print("ERROR: Ya existe un paciente con ese codigo.")
            return

        while True:
            dni = input("DNI del Paciente (8 digitos): ").strip()
            if len(dni) == 8:
                try:
                    int(dni)  
                    break
                except ValueError:
                    print("ERROR: El DNI debe contener solo numeros.")
            else:
                print("ERROR: El DNI debe tener exactamente 8 digitos.")

        nombres = input("Nombres: ").strip()
        apellidos = input("Apellidos: ").strip()

        while True:
            sexo = input("Sexo (M/F): ").strip().upper()
            if sexo in ["M", "F"]:
                break
            print("Opcion invalida. Ingrese 'M' o 'F'.")

        while True:
            f_str = input("Fecha de nacimiento (DD/MM/AAAA): ").strip()
            try:
                f_nac = datetime.strptime(f_str, "%d/%m/%Y").date()
                if f_nac > date.today():
                    print("La fecha de nacimiento no puede ser futura.")
                    continue
                break
            except ValueError:
                print("Formato de fecha incorrecto. Use DD/MM/AAAA (ejemplo: 15/08/2010).")

        paciente = Paciente(cod, dni, nombres, apellidos, f_nac, sexo, cod_resp)
        self.pacientes[cod] = paciente
        print(f"Paciente '{paciente.nombres} {paciente.apellidos}' registrado correctamente.")

    def listar_pacientes(self):
        """Muestra la lista general de pacientes."""
        print("\n--- LISTADO GENERAL DE PACIENTES ---")
        if not self.pacientes:
            print("No hay pacientes registrados en el sistema.")
            return

        print(f"{'Codigo':<8} {'DNI':<10} {'Nombres y Apellidos':<25} {'F. Nac.':<12} {'Sexo':<5} {'Edad Exacta'}")
        print("-" * 75)
        for pac in self.pacientes.values():
            print(pac.obtener_resumen_linea())

    def buscar_paciente(self):
        """Busca paciente por DNI o Nombre/Apellido."""
        print("\n--- BUSQUEDA DE PACIENTE ---")
        if not self.pacientes:
            print("No hay pacientes registrados.")
            return

        criterio = input("Ingrese DNI, Nombre o Apellido a buscar: ").strip().lower()
        encontrados = []

        for pac in self.pacientes.values():
            nombre_completo = f"{pac.nombres} {pac.apellidos}".lower()
            if criterio in pac.dni or criterio in nombre_completo:
                encontrados.append(pac)

        if not encontrados:
            print(f"No se encontraron pacientes que coincidan con '{criterio}'.")
            return

        print(f"\nSe encontraron {len(encontrados)} coincidencia(s):")
        for pac in encontrados:
            anos, meses, dias = pac.calcular_edad_exacta()
            responsable = self.responsables.get(pac.cod_responsable)

            print("\n" + "=" * 60)
            print("DATOS DEL PACIENTE")
            print(f" - Codigo: {pac.codigo} | DNI: {pac.dni}")
            print(f" - Nombre Completo: {pac.nombres} {pac.apellidos}")
            print(f" - Fecha de Nacimiento: {pac.fecha_nacimiento.strftime('%d/%m/%Y')}")
            print(f" - Sexo: {pac.sexo}")
            print(f" - Edad Exacta: {anos} anos, {meses} meses y {dias} dias")
            print("-" * 60)
            print("DATOS COMPLETOS DEL RESPONSABLE ASOCIADO")
            if responsable:
                print(f" - {responsable.mostrar_datos()}")
            else:
                print(" - Informacion de responsable no disponible.")
            print("=" * 60)

    def listar_responsables(self):
        """Lista los responsables registrados."""
        print("\n--- LISTA DE RESPONSABLES REGISTRADOS ---")
        if not self.responsables:
            print("No hay responsables registrados.")
            return
        for r in self.responsables.values():
            print(f" - {r.mostrar_datos()}")

    def ejecutar_menu(self):
        """Menú principal utilizando estructuras condicionales tradicionales."""
        self.cargar_datos_demo()

        while True:
            print("\n==========================================")
            print("      SISTEMA DE GESTION HOSPITALARIA     ")
            print("==========================================")
            print("1. Registrar paciente")
            print("2. Registrar responsable")
            print("3. Listar todos los pacientes")
            print("4. Buscar paciente (por DNI o Nombre/Apellido)")
            print("5. Listar responsables registrados")
            print("6. Salir")

            opcion = input("Seleccione una opcion (1-6): ").strip()

            if opcion == "1":
                self.registrar_paciente()
            elif opcion == "2":
                self.registrar_responsable()
            elif opcion == "3":
                self.listar_pacientes()
            elif opcion == "4":
                self.buscar_paciente()
            elif opcion == "5":
                self.listar_responsables()
            elif opcion == "6":
                print("\nSaliendo del sistema...")
                break
            else:
                print("\nOpcion no valida. Intente nuevamente.")

if __name__ == "__main__":
    app = SistemaHospital()
    app.ejecutar_menu()
