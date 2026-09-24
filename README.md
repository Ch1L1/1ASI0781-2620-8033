# Sistema de Gestión de Clínica Pediátrica 🏥

> **Caso de Estudio / Proyecto Académico**  
> Desarrollo progresivo de una aplicación en Python para la gestión integral de una clínica pediátrica (desde programación estructurada hasta Programación Orientada a Objetos con análisis de datos y persistencia).

---

## 📋 Tabla de Contenidos
1. [Descripción del Proyecto](#-descripción-del-proyecto)
2. [Objetivos del Sistema](#-objetivos-del-sistema)
3. [Fases del Proyecto](#-fases-del-proyecto)
   - [Fase 1: Trabajo Parcial (Versión Básica)](#fase-1-trabajo-parcial-versión-básica)
   - [Fase 2: Trabajo Final (Versión Completa OOP)](#fase-2-trabajo-final-versión-completa-oop)
4. [Estructura de Datos & Atributos](#-estructura-de-datos--atributos)
5. [Funcionalidades Principales](#-funcionalidades-principales)
6. [Métricas, Reportes y Gráficos](#-métricas-reportes-y-gráficos)
7. [Instalación y Ejecución](#-instalación-y-ejecución)

---

## 🩺 1. Descripción del Proyecto
Una clínica pediátrica brinda atención médica a niños y adolescentes mediante consultas programadas. Actualmente, el registro de pacientes, responsables, médicos y atenciones se maneja mediante hojas de cálculo y registros independientes, lo que dificulta:
* Consultar rápidamente el historial médico de un paciente.
* Controlar las atenciones de forma centralizada.
* Obtener estadísticas confiables sobre los servicios brindados.

Este proyecto resuelve dicha problemática implementando un software en Python estructurado en dos entregas evolutivas.

---

## 🎯 2. Objetivos del Sistema
La aplicación permite:
* Registrar responsables/apoderados y asociarlos con pacientes pediátricos.
* Administrar el directorio de médicos pediatras y sus especialidades.
* Registrar consultas médicas incluyendo control biométrico (**peso y talla**).
* Consultar historiales de atención y realizar búsquedas bajo múltiples criterios.
* Obtener estadísticas, reportes gerenciales y gráficos analíticos.
* **Persistencia de datos** (en la fase final) mediante archivos CSV/Excel y recuperación automática al iniciar el sistema.

---

## 🚀 3. Fases del Proyecto

### Fase 1: Trabajo Parcial (Versión Básica)
* **Paradigma:** Programación estructurada (Funciones, Listas, Diccionarios).
* **Restricciones:** *No se permite el uso de clases ni objetos.*
* **Componentes:** Validaciones robustas mediante funciones auxiliares, estructuras condicionales, repetitivas y menús interactivos por consola.

### Fase 2: Trabajo Final (Versión Completa OOP)
* **Paradigma:** Programación Orientada a Objetos (POO).
* **Características Técnicas:**
  * Diseño previo mediante **Diagrama de Clases UML**.
  * Aplicación de **Encapsulamiento** y **Properties** (`@property`, setters) para validación de DNI, CMP, Peso, Talla y Costo.
  * Relaciones de asociación e instancias (`Responsable` ➔ `Paciente`, `Paciente` ➔ `Consulta`, `Médico` ➔ `Consulta`).
  * Persistencia de datos usando **Pandas**.
  * Visualización de datos y métricas mediante **Matplotlib** o **Seaborn**.

---

## 📁 4. Estructura de Datos & Atributos

| Entidad | Atributos Principales |
| :--- | :--- |
| **Responsable** | Código, DNI, Nombres, Apellidos, Teléfono, Parentesco |
| **Paciente** | Código, DNI, Nombres, Apellidos, Fecha de nacimiento, Sexo, Código del responsable |
| **Médico** | Código, CMP, Nombres, Apellidos, Área/Especialidad |
| **Consulta** | Código, Código del paciente, Código del médico, Fecha, Motivo, Peso, Talla, Observaciones, Costo |

> **Especialidades Médicas Soportadas:** Pediatría general, Neonatología, Cardiología pediátrica, Neumología pediátrica y Gastroenterología pediátrica.

---

## ⚙️ 5. Funcionalidades Principales

* **Gestión de Responsables:** Registro, listado, búsqueda por DNI, modificación de teléfono y consulta de pacientes vinculados (DNI único).
* **Gestión de Pacientes:** Registro con validación de existencia del responsable, búsquedas por DNI/nombre/apellido, cálculo automático de edad y visualización de datos del apoderado.
* **Gestión de Médicos:** Registro con control de unicidad de CMP, filtros por especialidad y actualización de datos.
* **Registro de Consultas:** Validación de existencia previa de paciente y médico, almacenamiento de datos biométricos y costos.
* **Validaciones del Sistema:** Control estricto de campos no vacíos, rangos numéricos válidos (peso, talla, costos > 0) y códigos únicos.

---

## 📊 6. Métricas, Reportes y Gráficos

### Reportes Básicos y Avanzados
* Listados generales (pacientes y médicos).
* Historial de consultas por paciente y atenciones por médico.
* Ingresos totales y costo promedio por consulta.
* Paciente con mayor número de consultas.
* Distribución demográfica por **rangos de edad**: 
  * 0 a 2 años | 3 a 5 años | 6 a 11 años | 12 a 17 años.

### Gráficos Estadísticos (Versión Final)
1. **Gráfico de barras:** Cantidad de consultas realizadas por médico.
2. **Gráfico circular (Pie):** Distribución porcentual de pacientes por rango de edad.
3. **Gráfico de líneas:** Evolución temporal de consultas realizadas por mes.
4. **Histograma:** Distribución de las edades de los pacientes pediátricos.

---

## 🛠️ 7. Instalación y Ejecución

1. Clonar el repositorio:
   ```bash
   git clone https://github.com/tu-usuario/clinica-pediatrica.git
   cd clinica-pediatrica
   ```

2. (Para la versión final) Instalar dependencias requeridas:
   ```bash
   pip install pandas matplotlib seaborn
   ```

3. Ejecutar la aplicación:
   ```bash
   python main.py
