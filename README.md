# 📘 README – Clase de Repaso  
## Calculadora en Python

## 🎯 Objetivo
Reforzar los conceptos fundamentales de programación mediante la construcción progresiva de una **calculadora en Python**, integrando distintos **paradigmas de programación** y aplicando buenas prácticas básicas de desarrollo, validación de datos y pruebas unitarias.

---

## 🧠 Conceptos utilizados en la calculadora

### 🔹 Variables
Las variables permiten **almacenar datos en memoria** que pueden cambiar durante la ejecución del programa.

**En la calculadora:**  
Se utilizan para guardar los números ingresados por el usuario, los operadores y los resultados de las operaciones.

---

### 🔹 Comunicación con el usuario
Corresponde a la **entrada y salida de datos**, permitiendo la interacción entre el programa y el usuario.

**En la calculadora:**  
El usuario ingresa números y operadores por consola, y la calculadora muestra el resultado de cada operación.

---

### 🔹 Ciclo repetitivo
Un ciclo permite **repetir instrucciones mientras se cumpla una condición**, controlando el flujo del programa.

**En la calculadora:**  
Se utiliza para mantener el programa en ejecución, volver a solicitar datos y validar entradas incorrectas.

---

## 🧭 Paradigmas de programación aplicados

### 🔸 Paradigma imperativo (`if / elif / else`)
El paradigma **imperativo** se basa en indicar **paso a paso** qué debe hacer el programa y en qué orden.

**En la calculadora:**  
Se utiliza mediante estructuras `if`, `elif` y `else` para:
- Validar datos ingresados por el usuario
- Controlar condiciones específicas
- Dirigir el flujo del programa según distintas situaciones

Aquí el programador describe **cómo** se evalúan las condiciones.

---

### 🔸 Paradigma declarativo (`match`)
El paradigma **declarativo** se centra en expresar **qué acción ejecutar según un valor**, sin detallar el proceso de evaluación.

**En la calculadora:**  
Se utiliza la estructura `match` para declarar qué operación matemática ejecutar según el operador ingresado (`+`, `-`, `*`, `/`, `!`), reemplazando múltiples `if / elif / else`.

Aquí se declaran **reglas**, no procesos paso a paso.

---

### 🔸 Paradigma funcional
El paradigma **funcional** se basa en el uso de **funciones independientes**, cada una con una única responsabilidad.

**En la calculadora:**  
Cada operación matemática está implementada como una función separada:
- `sumar`
- `restar`
- `multiplicar`
- `dividir`
- `factorial`

Las funciones reciben datos y devuelven resultados sin depender del estado del programa.

---

### 🔸 Programación Orientada a Objetos (POO)
La **POO** organiza el programa en **clases y objetos**, encapsulando datos y comportamientos relacionados.

**En la calculadora:**  
Se define una clase `Calculadora` que agrupa las operaciones matemáticas como métodos, encapsulando la lógica del sistema.

---

## 🧩 Conceptos adicionales

### 🔹 Factorial y recursividad
El factorial es una operación matemática que multiplica un número por todos los enteros positivos menores hasta llegar a 1.

**En la calculadora:**  
Se implementa mediante **recursividad**, donde la función se llama a sí misma hasta alcanzar un caso base (`0` o `1`).

---

### 🔹 Estructura de datos: Lista
Las listas permiten **almacenar conjuntos de datos de forma ordenada**.

**En la calculadora:**  
Se utilizan para manejar opciones válidas, operadores permitidos o conjuntos de valores relacionados.

---

### 🔹 Manejo de errores
El manejo de errores permite **controlar situaciones inesperadas** sin detener el programa.

**En la calculadora:**  
Se controla, por ejemplo, la división por cero y el ingreso de valores no numéricos, evitando que el programa falle.

---

## 🛠️ Herramientas utilizadas

### 🔧 Git (Control de versiones)
Git permite **registrar y gestionar los cambios del código** a lo largo del tiempo.

**En el proyecto:**  
Se utiliza para mantener un historial de versiones del código y facilitar correcciones o mejoras.

---

### 🔧 IDE (Entorno de Desarrollo Integrado)
Un IDE integra herramientas para **escribir, ejecutar y depurar código**.

**En el proyecto:**  
Se utiliza para desarrollar la calculadora de forma ordenada y eficiente.

---

### 🔧 Pruebas unitarias
Las pruebas unitarias verifican que **cada función funcione correctamente de manera individual**.

**En el proyecto:**  
Se prueban las funciones matemáticas utilizando `assert`, validando resultados esperados antes de integrar el programa completo.

---

## 🧩 Cierre
La calculadora es un **caso práctico integrador** que demuestra cómo distintos paradigmas pueden convivir en un mismo programa, cada uno cumpliendo un rol específico.

> **El objetivo no es memorizar código, sino aprender a pensar y estructurar soluciones de forma clara.**
