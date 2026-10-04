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

Verifica la instalación de Cirq:

```python
import cirq
print("Versión de Cirq instalada:", cirq.__version__)

# 2. Instalación opcional de Qiskit y Qiskit Aer (para visualizaciones en la Esfera de Bloch)
!pip install qiskit qiskit-aer --quiet
