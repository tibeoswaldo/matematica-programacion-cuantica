# Capítulo 5: Programación Cuántica

> **Repositorio Oficial:** [matematica-programacion-cuantica](https://github.com/tibeoswaldo/matematica-programacion-cuantica)  
> **Entorno de Ejecución Obligatorio:** Todos los cuadernos y scripts de este módulo **DEBEN ejecutarse en Google Colab** (`GoogleColab`).

---

## 📌 Descripción General

¡Bienvenido al tramo final del entrenamiento práctico en computación cuántica! Tras dominar las bases teóricas y algebraicas en la "sala de mapas" de las matemáticas avanzadas, este módulo aborda el control directo del hardware y de los simuladores cuánticos.

En la computación cuántica, la programación no consiste en escribir lógica tradicional determinista de "si-entonces". Programar el mundo cuántico es el **arte de orquestar la naturaleza**: una labor donde el desarrollador manipula amplitudes de probabilidad, genera correlaciones no clásicas mediante el entrelazamiento y gestiona la interferencia (constructiva y destructiva) para que la solución correcta sea la única físicamente posible tras la medición.

---

## 🚀 Entorno de Ejecución (Google Colab Required)

> ⚠️ **IMPORTANTE:** Para garantizar la compatibilidad con las dependencias de **Cirq**, **Qiskit** y los simuladores cuánticos en la nube, todos los scripts deben ejecutarse dentro de **Google Colab**.

### ¿Por qué Google Colab?
1. **Sin instalaciones locales complejas:** Evita conflictos de entornos virtuales o compilación de dependencias en máquinas locales.
2. **Delegación de recursos:** La simulación cuántica requiere un procesamiento intensivo de matrices complejas. Colab delega este trabajo pesado a la nube, emulando la interacción cliente-servidor con una Unidad de Procesamiento Cuántico (QPU).
3. **Punto de acceso inmediato:** Permite instalar y ejecutar `cirq` y `qiskit` con comandos de celda directo (`!pip install`).

---

## 💻 Instalación y Configuración en Google Colab

Abre un cuaderno en **Google Colab** y ejecuta las siguientes celdas para preparar tu entorno de desarrollo:

```python
# 1. Instalación de la librería Google Cirq para computación cuántica
!pip install cirq --quiet

# 2. Instalación opcional de Qiskit y Qiskit Aer (para visualizaciones en la Esfera de Bloch)
!pip install qiskit qiskit-aer --quiet
```

Verifica la instalación de Cirq:

```python
import cirq
print("Versión de Cirq instalada:", cirq.__version__)
```

---

## 📁 Estructura del Repositorio

Todos los códigos `.py` y notebooks del capítulo están estructurados y subidos al repositorio oficial:  
🔗 **[https://github.com/tibeoswaldo/matematica-programacion-cuantica](https://github.com/tibeoswaldo/matematica-programacion-cuantica)**

```text
├── README.md
├── requirements.txt
└── scripts/
    ├── 01_vectores_estado_superposicion.py
    ├── 02_esfera_de_bloch_qiskit.py
    ├── 03_hola_mundo_cirq.py
    ├── 04_puertas_un_qubit.py
    ├── 05_cnot_y_estado_de_bell.py
    ├── 06_simulacion_rotacion_ry.py
    ├── 07_algoritmo_deutsch_jozsa.py
    └── 08_algoritmo_grover.py
```

---

## 📚 Contenido del Módulo

### 5.1 Introducción a la Computación Cuántica
* **Del bit al qubit en código:** Traducción de vectores de estado en el Espacio de Hilbert a arreglos numéricos en NumPy.
  $$|0\rangle = \begin{pmatrix} 1 \\ 0 \end{pmatrix}, \quad |1\rangle = \begin{pmatrix} 0 \\ 1 \end{pmatrix}$$
* **Superposición y Normalización:** Un estado general se define como $|\psi\rangle = \alpha |0\rangle + \beta |1\rangle$. Condición física de normalización:
  $$|\alpha|^2 + |\beta|^2 = 1$$
* **Paradigma de "Computación en el Sitio" (Computation-in-Place):** A diferencia de la arquitectura clásica de Von Neumann donde los datos viajan a la CPU, en una QPU los qubits permanecen estáticos y son las instrucciones (campos magnéticos o microondas) las que viajan hacia ellos.
* **La Esfera de Bloch:** Interfaz geométrica tridimensional para visualizar el estado de un qubit puro mediante los ángulos de colatitud ($\theta$) y fase ($\phi$):
  $$|\psi\rangle = \cos\left(\frac{\theta}{2}\right)|0\rangle + e^{i\phi}\sin\left(\frac{\theta}{2}\right)|1\rangle$$

### 5.2 Programando con Cirq (Google)
* **Filosofía Imperativa de Cirq:** Control fino sobre el tiempo y la topología del hardware.
* **Estructura de Hardware en Código:**
  * `cirq.LineQubit`: Arreglos unidimensionales de qubits.
  * `cirq.GridQubit`: Rejillas bidimensionales 2D (usado en procesadores como Google Sycamore).
* **Momentos (`cirq.Moment`) y Estrategias de Inserción (`cirq.InsertStrategy.EARLIEST`):** Abstracción temporal para sincronizar puertas paralelas.
* **Simuladores:** `.run()` para muestreo probabilístico realista por disparos (*shots*) y `.simulate()` para depuración directa del vector de estado puro.

### 5.3 Laboratorio de Puertas de un Solo Qubit
* **Puerta Pauli-X (`cirq.X`):** Operador NOT cuántico; invierte los estados base.
  $$X = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}$$
* **Puerta de Hadamard (`cirq.H`):** Generador de superposición uniforme ($|+\rangle$ y $|-\rangle$).
  $$H = \frac{1}{\sqrt{2}}\begin{pmatrix} 1 & 1 \\ 1 & -1 \end{pmatrix}$$
* **Puerta Pauli-Z (`cirq.Z`):** Modificación de la fase relativa (*Phase-Flip*) sin alterar la magnitud de probabilidad.
  $$Z = \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix}$$
* **Puerta Pauli-Y (`cirq.Y`):** Combinación de cambio de bit y cambio de fase introduciendo la unidad imaginaria $i$.
  $$Y = \begin{pmatrix} 0 & -i \\ i & 0 \end{pmatrix}$$

### 5.4 Operaciones Avanzadas y Entrelazamiento
* **Puerta CNOT (`cirq.CNOT`):** Operador entrelazador de dos qubits (control y objetivo).
  $$\text{CNOT} = \begin{pmatrix} 1 & 0 & 0 & 0 \\ 0 & 1 & 0 & 0 \\ 0 & 0 & 0 & 1 \\ 0 & 0 & 1 & 0 \end{pmatrix}$$
* **Generación del Estado de Bell ($\Phi^+$):** Creación del estado de entrelazamiento máximo:
  $$|\Phi^+\rangle = \frac{|00\rangle + |11\rangle}{\sqrt{2}}$$
* **Simulación Estadística y Repeticiones:** Justificación de la Ley de los Grandes Números (`repetitions=1000`) frente al fallo informativo de un *"Single Shot"*.
* **Uso de Llaves de Medición (`key='...'`):** Organización e inspección de histogramas de frecuencia.

### 5.5 Introducción a Algoritmos y Oráculos Cuánticos
* **Concepto de Oráculo:** Cajas negras matemáticas reversibles.
* **Algoritmo de Deutsch-Jozsa:** Demostración de ventaja cuántica exponencial; determina si una función es **Constante** o **Equilibrada** en una sola consulta ($1$ query vs. $2^{n-1}+1$ consultas clásicas).
* **Algoritmo de Grover:** Buscador cuántico en bases de datos desordenadas con aceleración cuadrática ($\mathcal{O}(\sqrt{N})$ iteraciones mediante amplificación de amplitud y difusor).
  $$k \approx \frac{\pi}{4}\sqrt{N}$$

---

## 🛠️ Ejemplos Destacados de Código

### 1. Construcción del Estado de Bell (Entrelazamiento) en Cirq
*(Ejecutar en Google Colab)*

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
```

### 2. Algoritmo de Deutsch-Jozsa (Consulta Única)
*(Ejecutar en Google Colab)*

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
```

---

## 🔬 Tabla Comparativa: Paradigmas de Cómputo

| Aspecto | Computación Clásica | Computación Cuántica (In-Place) |
| :--- | :--- | :--- |
| **Unidad de Información** | Bit ($0$ o $1$) | Qubit (Vector en Espacio de Hilbert) |
| **Ubicación de Datos** | Se transportan por bus a la CPU | Permanecen en el qubit (In-place) |
| **Arquitectura** | Von Neumann (Memoria y CPU separadas) | Integrada (El qubit es el dato y el procesador) |
| **Operación Lógica** | Cambio de voltaje / bit-flip | Evolución unitaria mediante rotación de matrices |
| **Resultado** | Determinado almacenado en memoria | Colapso probabilístico tras la medición |

---

## 📑 Referencias y Créditos

* **Autor:** Oswaldo
* **Libro:** *Matemática y Programación Cuántica* (Capítulo 05)
* **Librerías principales:** Google Cirq, Qiskit, NumPy
* **Repositorio GitHub:** [tibeoswaldo/matematica-programacion-cuantica](https://github.com/tibeoswaldo/matematica-programacion-cuantica)
