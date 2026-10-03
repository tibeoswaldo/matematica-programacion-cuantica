# matematica-programacion-cuantica
Código fuente en Python de los ejemplos y ejercicios del libro Matemática para Programación Cuántica.
# Capítulo 5: Programación Cuántica ⚛️💻

¡Bienvenido al repositorio de código del **Capítulo 5**! Tras explorar los fundamentos matemáticos de los espacios de Hilbert y las matrices unitarias en los capítulos anteriores, en esta sección tomaremos el control del hardware cuántico y sus simuladores. 

Aquí aprenderás a escribir código Python para manipular amplitudes de probabilidad, orquestar la interferencia y construir algoritmos que explotan la superposición y el entrelazamiento cuántico usando **Cirq** y **Qiskit**.

---

## 📋 Tabla de Contenidos

- [Descripción General](#descripción-general)
- [Contenido del Capítulo](#contenido-del-capítulo)
- [Requisitos e Instalación](#requisitos-e-instalación)
- [Estructura del Código Fuente](#estructura-del-código-fuente)
- [Ejemplos Destacados](#ejemplos-destacados)
  - [1. Representación Vectorial y Superposición](#1-representación-vectorial-y-superposición)
  - [2. "Hola Mundo" en Cirq](#2-hola-mundo-en-cirq)
  - [3. Entrelazamiento y Estado de Bell](#3-entrelazamiento-y-estado-de-bell)
  - [4. Algoritmo de Deutsch-Jozsa](#4-algoritmo-de-deutsch-jozsa)
  - [5. Algoritmo de Grover](#5-algoritmo-de-grover)
- [Ejecución en Google Colab](#ejecución-en-google-colab)

---

## 📸 Descripción General

Programar en el mundo cuántico no se trata de escribir lógica tradicional `if-else`, sino de manipular estados físicos y gestionar la interferencia para que la respuesta correcta sea la única físicamente probable tras la medición.

A lo largo de este capítulo se cubren:
* **El paradigma *Computation-in-place*:** Donde los datos no se mueven hacia una CPU, sino que evolucionan físicamente en el qubit mediante pulsos electromagnéticos o microondas.
* **La Esfera de Bloch:** Interfaz geométrica fundamental para depurar y visualizar rotaciones de un solo qubit.
* **El framework Cirq (Google):** Manejo imperativo de qubits, momentos y estrategias de inserción.
* **Oráculos y Ventaja Cuántica:** Implementación de cajas negras para los algoritmos de Deutsch-Jozsa y la búsqueda cuadrática de Grover.

---

## 📚 Contenido del Capítulo

1. **5.1 Introducción a la Computación Cuántica**
   - Del bit al qubit en código.
   - Normalización y regla de Born.
   - Paradigma de computación en el sitio (*computation-in-place*).
   - Visualización con la Esfera de Bloch.
2. **5.2 Programando con Cirq**[cite: 1]
   - Configuración en Google Colab[cite: 1].
   - Anatomía de Cirq: `LineQubit`, `GridQubit`, `Circuit` y `Moment`[cite: 1].
   - Primer "Hola Mundo" cuántico[cite: 1].
3. **5.3 Puertas de un Solo Qubit**[cite: 1]
   - Puertas de Pauli ($X$, $Y$, $Z$) y Hadamard ($H$)[cite: 1].
4. **5.4 Operaciones Avanzadas y Entrelazamiento**[cite: 1]
   - Puerta CNOT[cite: 1].
   - Construcción del Estado de Bell ($\Phi^+$)[cite: 1].
   - Simulación estadística: la necesidad de múltiples repeticiones (*shots*)[cite: 1].
   - Rotaciones continuas con $R_y(\theta)$[cite: 1].
5. **5.5 Introducción a Algoritmos y Oráculos**[cite: 1]
   - Algoritmo de Deutsch-Jozsa (Ventaja exponencial con 1 consulta)[cite: 1].
   - Algoritmo de Grover (Búsqueda cuántica y amplificación de amplitud)[cite: 1].

---

## ⚙️ Requisitos e Instalación

Para ejecutar los scripts localmente, asegúrate de tener instalado **Python 3.8+** e instala las dependencias mediante:

```bash
pip install -r requirements.txt
