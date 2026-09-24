# CASO 8: SISTEMA DE GESTIÓN DE CLÍNICA PEDIÁTRICA 🏥

## 📋 Tabla de Contenidos
1. [Descripción](#1-descripción)
2. [Objetivo del Sistema](#2-objetivo-del-sistema)
3. [Características del Trabajo](#3-características-del-trabajo)
4. [Trabajo Parcial – Versión Básica (sin OOP)](#4-trabajo-parcial--versión-básica-sin-oop)
   - [4.1 Almacenamiento](#41-almacenamiento)
   - [4.2 Funcionalidades Mínimas](#42-funcionalidades-mínimas)
   - [4.3 Reportes Básicos](#43-reportes-básicos)
   - [4.4 Menú Sugerido](#44-menú-sugerido)
5. [Trabajo Final – Versión Completa (OOP + UML + Excel/CSV)](#5-trabajo-final--versión-completa-oop--uml--excelcsv)
   - [5.1 Diagrama de Clases UML](#51-diagrama-de-clases-uml)
   - [5.2 Funcionalidades](#52-funcionalidades)
   - [5.3 Implementación OOP en Python](#53-implementación-oop-en-python)
   - [5.4 Métricas y Gráficos](#54-métricas-y-gráficos)
   - [5.5 Sugerencias de Investigación (Benchmarking)](#55-sugerencias-de-investigación-benchmarking)

---

## 1. Descripción
Una clínica pediátrica brinda atención médica a niños y adolescentes mediante consultas programadas. Actualmente, el registro de pacientes, responsables, médicos y atenciones se realiza utilizando hojas de cálculo y registros independientes, lo que dificulta consultar rápidamente el historial de un paciente, controlar sus atenciones y obtener estadísticas sobre los servicios brindados.

La clínica requiere desarrollar una aplicación en Python que permita organizar la información de los pacientes pediátricos, sus responsables, los médicos y las consultas realizadas.

El sistema será desarrollado progresivamente:
* **Trabajo Parcial:** Se implementará utilizando programación estructurada con funciones, listas y diccionarios.
* **Trabajo Final:** La solución deberá migrarse a Programación Orientada a Objetos, incorporar persistencia de información con Pandas y generar métricas y gráficos.

---

## 2. Objetivo del sistema
La aplicación deberá permitir:
* Registrar responsables o apoderados.
* Registrar pacientes pediátricos.
* Asociar cada paciente con un responsable.
* Registrar médicos pediatras.
* Registrar consultas médicas.
* Registrar peso y talla del paciente durante una consulta.
* Consultar el historial de atenciones de un paciente.
* Realizar búsquedas utilizando diferentes criterios.
* Obtener estadísticas básicas de las atenciones realizadas.
* Generar reportes para apoyar la gestión de la clínica.
* En la versión final, almacenar y recuperar información utilizando archivos CSV o Excel.
* Generar gráficos utilizando los datos registrados.

---

## 3. Características del trabajo

### Versión básica – Trabajo Parcial
La primera versión deberá desarrollarse utilizando programación estructurada en Python. Se deberán utilizar: 
* Funciones
* Listas
* Diccionarios
* Condicionales
* Estructuras repetitivas
* Validaciones
* Variables auxiliares
* *Nota:* No se deberán utilizar clases ni objetos en el Trabajo Parcial.

### Versión completa – Trabajo Final
La solución deberá ser rediseñada aplicando Programación Orientada a Objetos. Se deberá incorporar: 
* Clases y objetos
* Constructores
* Encapsulamiento
* Properties
* Relaciones entre clases
* Diagrama UML
* Pandas
* Archivos CSV o Excel
* Matplotlib o Seaborn

---

## 4. Trabajo Parcial – Versión Básica (sin OOP)

### 4.1 Almacenamiento
Toda la información deberá mantenerse en memoria utilizando listas y diccionarios. Se deberán administrar como mínimo:
1. **Responsable:** Código, DNI, Nombres, Apellidos, Teléfono, Parentesco con el paciente.
2. **Paciente:** Código, DNI, Nombres, Apellidos, Fecha de nacimiento, Sexo, Código del responsable.
3. **Médico:** Código, CMP, Nombres, Apellidos, Área o especialidad pediátrica (*Pediatría general, Neonatología, Cardiología pediátrica, Neumología pediátrica, Gastroenterología pediátrica*).
4. **Consulta:** Código, Código del paciente, Código del médico, Fecha, Motivo de consulta, Peso, Talla, Observaciones, Costo de consulta.

### 4.2 Funcionalidades mínimas

#### A. Gestión de responsables
* Registrar un responsable.
* Listar responsables.
* Buscar un responsable por DNI.
* Modificar teléfono.
* Consultar los pacientes asociados a un responsable.
* **Restricción:** No deberá permitirse registrar dos responsables con el mismo DNI.

#### B. Gestión de pacientes
* Registrar un paciente.
* Asociar el paciente con un responsable existente.
* Listar pacientes.
* Buscar un paciente por DNI.
* Buscar pacientes por nombre o apellido.
* Calcular la edad del paciente.
* Mostrar los datos del responsable asociado.
* **Restricción:** No deberá registrarse un paciente si el responsable indicado no existe.

#### C. Gestión de médicos
* Registrar médicos.
* Listar médicos.
* Buscar un médico por código.
* Buscar médicos por área o especialidad.
* Modificar información básica del médico.
* **Restricción:** El CMP no podrá repetirse.

#### D. Registro de consultas
Para registrar una consulta deberán existir previamente el paciente y el médico. El sistema deberá solicitar:
* Paciente, Médico, Fecha, Motivo de consulta, Peso, Talla, Observaciones, Costo. 
* Una vez registrada, la consulta deberá formar parte del historial del paciente.

#### E. Validaciones
Como mínimo se deberá validar:
* DNI no vacío.
* DNI no duplicado.
* CMP no duplicado.
* Nombres y apellidos no vacíos.
* Existencia del responsable.
* Existencia del paciente.
* Existencia del médico.
* Peso mayor que cero.
* Talla mayor que cero.
* Costo mayor que cero.
* Códigos no duplicados.
* Opciones válidas en los menús.
* *Nota:* Las principales validaciones deberán implementarse mediante funciones.

### 4.3 Reportes básicos
El sistema deberá generar como mínimo:
1. Listado general de pacientes.
2. Listado general de médicos.
3. Pacientes atendidos por un médico.
4. Historial de consultas de un paciente.
5. Cantidad total de consultas realizadas.
6. Cantidad de consultas realizadas por médico.
7. Ingreso total generado por consultas.
8. Promedio del costo de las consultas.
9. Paciente con mayor cantidad de consultas.
10. Cantidad de pacientes según rango de edad:
    * 0 a 2 años
    * 3 a 5 años
    * 6 a 11 años
    * 12 a 17 años
* **Adicional:** Cada grupo deberá implementar como mínimo **2 reportes adicionales** relacionados con el caso.

### 4.4 Menú sugerido
```text
========================================
         CLÍNICA PEDIÁTRICA
========================================
1. Gestión de responsables
2. Gestión de pacientes
3. Gestión de médicos
4. Registrar consulta
5. Consultar historial del paciente
6. Reportes
7. Salir
========================================
```
*Cada opción podrá contener submenús. El grupo podrá modificar la estructura del menú siempre que se mantengan las funcionalidades requeridas.*

---

## 5. Trabajo Final – Versión Completa (OOP + UML + Excel/CSV)

### 5.1 Diagrama de clases UML
El grupo deberá diseñar un diagrama de clases antes de implementar la versión final. Como referencia, se sugieren las siguientes clases:
* **Responsable:** Atributos (`codigo, dni, nombres, apellidos, telefono, parentesco`).
* **Paciente:** Atributos (`codigo, dni, nombres, apellidos, fecha_nacimiento, sexo, responsable`). Métodos (`calcular_edad()`, `mostrar_datos()`).
* **Medico:** Atributos (`codigo, cmp, nombres, apellidos, especialidad`).
* **Consulta:** Atributos (`codigo, fecha, paciente, medico, motivo, peso, talla, observaciones, costo`).
* **ClinicaPediatrica:** Clase encargada de administrar las principales operaciones del sistema. Podrá gestionar colecciones de Responsables, Pacientes, Médicos y Consultas.

> *Nota:* El grupo podrá incorporar otras clases cuando pueda justificar correctamente su necesidad. El UML deberá mostrar: Clases, Atributos, Métodos, Visibilidad, Relaciones, Cardinalidades y Navegabilidad cuando corresponda.

### 5.2 Funcionalidades
La versión final deberá contener todas las funcionalidades implementadas durante el Trabajo Parcial, pero utilizando objetos. Además, deberá permitir:
* Cargar registros existentes desde archivos.
* Guardar nuevos registros.
* Actualizar información.
* Mantener el historial de consultas.
* Obtener indicadores generales.
* Realizar análisis de los datos registrados.
* Generar gráficos estadísticos.

### 5.3 Implementación OOP en Python
La implementación deberá evidenciar correctamente los principales conceptos de Programación Orientada a Objetos:
* **Encapsulamiento:** Los atributos que requieran protección deberán implementarse utilizando encapsulamiento.
* **Properties:** Se deberán utilizar `@property` y setters para controlar atributos que necesiten validaciones (DNI, CMP, Peso, Talla, Costo).
* **Constructores:** Cada clase deberá contar con un constructor que permita inicializar correctamente sus objetos.
* **Relaciones entre clases:** 
  * `Responsable` ➔ `Paciente` (un responsable puede estar asociado con uno o varios pacientes).
  * `Paciente` ➔ `Consulta` (un paciente puede tener múltiples consultas).
  * `Médico` ➔ `Consulta` (un médico puede realizar múltiples consultas).
* **Persistencia con Pandas:** Archivos `responsables.csv`, `pacientes.csv`, `medicos.csv`, `consultas.csv` (también se podrá utilizar un archivo Excel con diferentes hojas). Cuando el programa se ejecute nuevamente deberá recuperar la información almacenada previamente.

### 5.4 Métricas y gráficos
El sistema deberá calcular como mínimo:
1. Número total de pacientes registrados.
2. Número total de médicos.
3. Número total de consultas.
4. Ingreso total generado.
5. Promedio de consultas por paciente.
6. Médico con mayor número de consultas.
7. Paciente con mayor número de consultas.
8. Promedio de edad de los pacientes.
9. Promedio de peso según rango de edad.
10. Cantidad de pacientes por área o especialidad atendida.

Se deberán implementar como mínimo **4 gráficos** (utilizando Matplotlib o Seaborn, u otras alternativas justificadas):
1. **Gráfico de barras:** Cantidad de consultas realizadas por médico.
2. **Gráfico circular:** Distribución de pacientes según rango de edad.
3. **Gráfico de líneas:** Cantidad de consultas realizadas por mes.
4. **Histograma:** Distribución de edades de los pacientes.

### 5.5 Sugerencias de investigación (benchmarking)
Los estudiantes deberán investigar brevemente sistemas utilizados para la gestión de clínicas o consultorios pediátricos. La investigación deberá considerar aspectos como:
* Registro de pacientes
* Registro de responsables
* Gestión de médicos
* Historial de consultas
* Registro de peso y talla
* Reportes administrativos
* Indicadores estadísticos

* **Requisito:** Cada grupo deberá identificar al menos **2 funcionalidades** encontradas en sistemas reales y explicar cómo podrían incorporarse al sistema desarrollado.
* *Advertencia:* No se deberá copiar código de aplicaciones, repositorios o proyectos encontrados en Internet. La investigación deberá utilizarse únicamente como referencia para justificar las decisiones de diseño.
