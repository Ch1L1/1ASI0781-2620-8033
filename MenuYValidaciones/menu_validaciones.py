from Medicos.medicos import menu_medicos
from Pacientes.pacientes import menu as menu_pacientes
from Responsables.responsables import menu_resp
from Reportes.reportes import (
    edad_rangos,
    ingreso_total,
    paciente_max,
    promedio_costo,
    rep_fecha,
    rep_ing_med,
    total_consultas,
    consul_medico,
    listar_pacientes,
    listar_medicos,
    pacientes_medico,
    hist_paciente,
)
from Consultas.consultas import ingresa_consulta
from datos import consultas, medicos, pacientes, responsables


def reg_consulta_facade():
    ingresa_consulta(consultas, pacientes, medicos)


def hist_paciente_facade():
    dni = input("Ingrese DNI del paciente: ").strip()
    pac = None
    for item in pacientes:
        if item["dni"] == dni:
            pac = item
            break
    if pac is None:
        print("No existe ese paciente.")
        return
    hist_paciente(consultas, pac["codigo"])


def reportes_facade():
    while True:
        print("\n=== REPORTES ===")
        print("1. Listado general de pacientes")
        print("2. Listado general de médicos")
        print("3. Pacientes atendidos por un médico")
        print("4. Historial de consultas de un paciente")
        print("5. Total de consultas")
        print("6. Consultas por médico")
        print("7. Ingreso total")
        print("8. Promedio del costo")
        print("9. Paciente con más consultas")
        print("10. Conteo por rango de edad")
        print("11. Consultas por fecha")
        print("12. Ingresos por médico")
        print("13. Volver")
        opcion = input("Seleccione opción: ").strip()

        if opcion == "1":
            listar_pacientes(pacientes)
        elif opcion == "2":
            listar_medicos(medicos)
        elif opcion == "3":
            cod = input("Código del médico: ").strip().upper()
            pacientes_medico(consultas, pacientes, cod)
        elif opcion == "4":
            hist_paciente_facade()
        elif opcion == "5":
            total_consultas(consultas)
        elif opcion == "6":
            consul_medico(consultas, medicos)
        elif opcion == "7":
            ingreso_total(consultas)
        elif opcion == "8":
            promedio_costo(consultas)
        elif opcion == "9":
            paciente_max(consultas, pacientes)
        elif opcion == "10":
            edad_rangos(pacientes)
        elif opcion == "11":
            fecha = input("Ingrese la fecha de consulta (DD/MM/AAAA): ").strip()
            rep_fecha(consultas, fecha)
        elif opcion == "12":
            cod = input("Código del médico: ").strip().upper()
            rep_ing_med(consultas, cod)
        elif opcion == "13":
            break
        else:
            print("Opción inválida.")


def main():
    while True:
        print("\n=== CLÍNICA PEDIÁTRICA ===")
        print("1. Gestión de responsables")
        print("2. Gestión de pacientes")
        print("3. Gestión de médicos")
        print("4. Registrar consulta")
        print("5. Consultar historial del paciente")
        print("6. Reportes")
        print("7. Salir")
        opcion = input("Seleccione opción: ").strip()

        if opcion == "1":
            menu_resp(responsables, pacientes)
        elif opcion == "2":
            menu_pacientes()
        elif opcion == "3":
            menu_medicos()
        elif opcion == "4":
            reg_consulta_facade()
        elif opcion == "5":
            hist_paciente_facade()
        elif opcion == "6":
            reportes_facade()
        elif opcion == "7":
            print("Saliendo del sistema...")
            break
        else:
            print("Opción inválida. Intente nuevamente.")


if __name__ == "__main__":
    main()
