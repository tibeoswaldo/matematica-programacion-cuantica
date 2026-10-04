# matematica-programacion-cuantica
Código fuente en Python de los ejemplos y ejercicios del libro Matemática para Programación Cuántica.
# Capítulo 5: Programación Cuántica ⚛️💻

¡Bienvenido al repositorio de código del **Capítulo 5**! Tras explorar los fundamentos matemáticos de los espacios de Hilbert y las matrices unitarias en los capítulos anteriores, en esta sección tomaremos el control del hardware cuántico y sus simuladores. 

Aquí aprenderás a escribir código Python para manipular amplitudes de probabilidad, orquestar la interferencia y construir algoritmos que explotan la superposición y el entrelazamiento cuántico usando **Cirq** y **Qiskit**.

---
# 1. Instalación de la librería Google Cirq para computación cuántica
!pip install cirq --quiet

# 2. Instalación opcional de Qiskit y Qiskit Aer (para visualizaciones en la Esfera de Bloch)
!pip install qiskit qiskit-aer --quiet
```[cite: 2]

Verifica la instalación de Cirq:

```python
import cirq
print("Versión de Cirq instalada:", cirq.__version__)
```[cite: 2]

---

## 📁 Estructura del Repositorio

Todos los códigos `.py` y notebooks del capítulo están estructurados y subidos al repositorio oficial[cite: 2]:  
🔗 **[https://github.com/tibeoswaldo/matematica-programacion-cuantica](https://github.com/tibeoswaldo/matematica-programacion-cuantica)**[cite: 2]

---

## 📚 Contenido del Módulo

### 5.1 Introducción a la Computación Cuántica
* **Del bit al qubit en código:** Traducción de vectores de estado en el Espacio de Hilbert ($\vert{}0\rangle$ y $\vert{}1\rangle$) a arreglos numéricos en NumPy[cite: 2].
* **Superposición y Normalización:** Condición física de cumplimiento de probabilidades ($\sum \vert{}\alpha_i\vert{}^2 = 1$)[cite: 2].
* **Paradigma de "Computación en el Sitio" (Computation-in-Place):** A diferencia de la arquitectura clásica de Von Neumann donde los datos viajan a la CPU, en una QPU los qubits permanecen estáticos y son las instrucciones (campos magnéticos o microondas) las que viajan hacia ellos[cite: 2].
* **La Esfera de Bloch:** Interfaz geométrica tridimensional para visualizar el estado de un qubit puro mediante los ángulos de colatitud ($\theta$) y fase ($\phi$)[cite: 2].

### 5.2 Programando con Cirq (Google)
* **Filosofía Imperativa de Cirq:** Control fino sobre el tiempo y la topología del hardware[cite: 2].
* **Estructura de Hardware en Código:**
  * `cirq.LineQubit`: Arreglos unidimensionales de qubits[cite: 2].
  * `cirq.GridQubit`: Rejillas bidimensionales 2D (usado en procesadores como Google Sycamore)[cite: 2].
* **Momentos (`cirq.Moment`) y Estrategias de Inserción (`cirq.InsertStrategy.EARLIEST`):** Abstracción temporal para sincronizar puertas paralelas[cite: 2].
* **Simuladores:** `.run()` para muestreo probabilístico realista por disparos (*shots*) y `.simulate()` para depuración directa del vector de estado puro[cite: 2].

### 5.3 Laboratorio de Puertas de un Solo Qubit
* **Puerta Pauli-X (`cirq.X`):** Operador NOT cuántico; invierte los estados base[cite: 2].
* **Puerta de Hadamard (`cirq.H`):** Generador de superposición uniforme ($\vert{}+\rangle$ y $\vert{}-\rangle$)[cite: 2].
* **Puerta Pauli-Z (`cirq.Z`):** Modificación de la fase relativa ($Phase-Flip$) sin alterar la magnitud de probabilidad[cite: 2].
* **Puerta Pauli-Y (`cirq.Y`):** Combinación de cambio de bit y cambio de fase introduciendo la unidad imaginaria $j$[cite: 2].

### 5.4 Operaciones Avanzadas y Entrelazamiento
* **Puerta CNOT (`cirq.CNOT`):** Operador entrelazador de dos qubits (control y objetivo)[cite: 2].
* **Generación del Estado de Bell ($\Phi^+$):** Creación del estado de entrelazamiento máximo $\frac{\vert{}00\rangle + \vert{}11\rangle}{\sqrt{2}}$[cite: 2].
* **Simulación Estadística y Repeticiones:** Justificación de la Ley de los Grandes Números (`repetitions=1000`) frente al fallo informativo de un *"Single Shot"*[cite: 2].
* **Uso de Llaves de Medición (`key='...'`):** Organización e inspección de histogramas de frecuencia[cite: 2].

### 5.5 Introducción a Algoritmos y Oráculos Cuánticos
* **Concepte de Oráculo:** Cajas negras matemáticas reversibles[cite: 2].
* **Algoritmo de Deutsch-Jozsa:** Demostración de ventaja cuántica exponencial; determina si una función es **Constante** o **Equilibrada** en una sola consulta ($1$ query vs. $2^{n-1}+1$ consultas clásicas)[cite: 2].
* **Algoritmo de Grover:** Buscador cuántico en bases de datos desordenadas con aceleración cuadrática ($\mathcal{O}(\sqrt{N})$ iteraciones mediante amplificación de amplitud y difusor)[cite: 2].

---

## 🛠️ Ejemplos Destacados de Código

### 1. Construcción del Estado de Bell (Entrelazamiento) en Cirq
*(Ejecutar en Google Colab)*[cite: 2]

```python
import cirq

# 1. Definir los qubits en una línea
q0 = cirq.LineQubit(0)
q1 = cirq.LineQubit(1)

# 2. Crear el circuito
circuito_bell = cirq.Circuit()
circuito_bell.append(cirq.H(q0))        # Superposición en el qubit control
circuito_bell.append(cirq.CNOT(q0, q1)) # Entrelazamiento con el qubit objetivo

# 3. Simular el vector de estado resultante
simulador = cirq.Simulator()
resultado = simulador.simulate(circuito_bell)

print("--- Estado de Bell resultante ---")
print(cirq.dirac_notation(resultado.final_state_vector))
```[cite: 2]

### 2. Algoritmo de Deutsch-Jozsa (Consulta Única)
*(Ejecutar en Google Colab)*[cite: 2]

```python
import cirq
import numpy as np

# Registro de 10 qubits de entrada (1024 combinaciones) y 1 auxiliar
qubits_entrada = cirq.LineQubit.range(10)
qubit_auxiliar = cirq.LineQubit(10)

circuito = cirq.Circuit()

# Preparar estado auxiliar en |-⟩ para Phase Kickback
circuito.append([cirq.X(qubit_auxiliar), cirq.H(qubit_auxiliar)])

# Superposición de entradas
circuito.append(cirq.H.on_each(*qubits_entrada))

# Oráculo Equilibrado (CNOTs)
for q in qubits_entrada:
    circuito.append(cirq.CNOT(q, qubit_auxiliar))

# Interferencia final
circuito.append(cirq.H.on_each(*qubits_entrada))

# Medición
circuito.append(cirq.measure(*qubits_entrada, key="resultado"))

# Ejecución en simulador (1 sola consulta / 1 disparo)
simulador = cirq.Simulator()
resultado = simulador.run(circuito, repetitions=1)
bits = resultado.measurements["resultado"][0]

if np.all(bits == 0):
    print("Resultado: FUNCIÓN CONSTANTE")
else:
    print("Resultado: FUNCIÓN EQUILIBRADA")
```[cite: 2]

---

## 🔬 Tabla Comparativa: Paradigmas de Cómputo

| Aspecto | Computación Clásica | Computación Cuántica (In-Place) |
| :--- | :--- | :--- |
| **Unidad de Información** | Bit ($0$ o $1$)[cite: 2] | Qubit (Vector en Espacio de Hilbert)[cite: 2] |
| **Ubicación de Datos** | Se transportan por bus a la CPU[cite: 2] | Permanecen en el qubit (In-place)[cite: 2] |
| **Arquitectura** | Von Neumann (Memoria y CPU separadas)[cite: 2] | Integrada (El qubit es el dato y el procesador)[cite: 2] |
| **Operación Lógica** | Cambio de voltaje / bit-flip[cite: 2] | Evolución unitaria mediante rotación de matrices[cite: 2] |
| **Resultado** | Determinado almacenado en memoria[cite: 2] | Colapse probabilístico tras la medición[cite: 2] |

---

## 📑 Referencias y Créditos

* **Autor:** Oswaldo[cite: 2]
* **Libro:** *Matemática y Programación Cuántica* (Capítulo 05)[cite: 2]
* **Librerías principales:** Google Cirq, Qiskit, NumPy[cite: 2]
* **Repositorio GitHub:** [tibeoswaldo/matematica-programacion-cuantica](https://github.com/tibeoswaldo/matematica-programacion-cuantica)[cite: 2]
