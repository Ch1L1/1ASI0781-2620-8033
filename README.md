# PediaCare

Este proyecto implementa un sistema de gestión para una clínica pediátrica usando solo listas, diccionarios, funciones, validaciones y menús interactivos.

## Objetivo
Administrar responsables, pacientes, médicos y consultas de una clínica pediátrica, manteniendo la información en memoria y mostrando reportes básicos.

## Estructuras principales
Se mantienen 4 listas de diccionarios:

1. `responsables`
   - `codigo`
   - `dni`
   - `nombres`
   - `apellidos`
   - `telefono`
   - `parentesco`

2. `pacientes`
   - `codigo`
   - `dni`
   - `nombres`
   - `apellidos`
   - `f_nac`
   - `sexo`
   - `cod_resp`

3. `medicos`
   - `codigo`
   - `cmp`
   - `nombres`
   - `apellidos`
   - `especialidad`

4. `consultas`
   - `codigo`
   - `cod_pac`
   - `cod_med`
   - `fecha`
   - `motivo`
   - `peso`
   - `talla`
   - `obs`
   - `costo`

Todo el programa está en un solo archivo, `main.py`, incluyendo las cuatro listas,
las funciones de responsables, pacientes, médicos, consultas y reportes, y los menús.
Las listas se crean una sola vez al inicio del script y se usan en todas las secciones.
Las versiones modulares se conservan en sus carpetas (`Responsables/`, `Pacientes/`,
`Medicos/`, `Consultas/`, `Reportes/` y `MenuYValidaciones/`) para desarrollo posterior, la aplicación independiente que se ejecuta y entrega es `main.py`.

Especialidades permitidas:
- Pediatría general
- Neonatología
- Cardiología pediátrica
- Neumología pediátrica
- Gastroenterología pediátrica

## Funcionalidades

### Gestión de responsables
- Registrar responsable
- Listar responsables
- Buscar responsable por DNI
- Modificar teléfono
- Ver pacientes asociados a un responsable

### Gestión de pacientes
- Registrar paciente
- Validar que el responsable exista
- Listar pacientes
- Buscar paciente por DNI
- Buscar paciente por nombre o apellido
- Mostrar responsable asociado
- Calcular edad a partir de la fecha de nacimiento

### Gestión de médicos
- Registrar médico
- Validar CMP único
- Listar médicos
- Buscar médico por código
- Buscar médicos por especialidad
- Modificar datos básicos del médico
- Elegir estas acciones desde el submenú de gestión de médicos y volver al menú principal cuando se desee

### Consultas
- Registrar consulta
- Verificar que exista paciente y médico
- Validar peso, talla y costo positivos
- Consultar historial de un paciente

## Validaciones obligatorias
- DNI no vacío y con 8 dígitos
- Nombres y apellidos no vacíos
- Códigos únicos
- DNI único
- CMP único
- Responsable existente antes de registrar paciente
- Paciente y médico existentes antes de registrar consulta
- Peso > 0
- Talla > 0
- Costo > 0
- Menú con opciones válidas, sin errores por entrada incorrecta

## Reportes requeridos
1. Listado general de pacientes
2. Listado general de médicos
3. Pacientes atendidos por un médico
4. Historial de consultas de un paciente
5. Total de consultas registradas
6. Total de consultas por médico
7. Ingreso total generado
8. Promedio del costo de consultas
9. Paciente con mayor cantidad de consultas
10. Conteo de pacientes por rango de edad
   - 0 a 2 años
   - 3 a 5 años
   - 6 a 11 años
   - 12 a 17 años
11. Consultas registradas por fecha
12. Ingresos y atenciones por médico
13. Volver al menú principal

Reportes extras mínimos:
- Motivo más frecuente de consulta
- Ingreso total por especialidad

## Menú principal
```text
=== CLÍNICA PEDIÁTRICA ===
1. Gestión de responsables
2. Gestión de pacientes
3. Gestión de médicos
4. Registrar consulta
5. Consultar historial del paciente
6. Reportes
7. Salir
```

## Cómo ejecutar
```bash
python3 main.py
```
