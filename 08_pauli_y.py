import cirq
import numpy as np
from IPython.display import display

# 1. Instanciación del qubit y circuito cuántico
qubit = cirq.LineQubit(0)
circuito_y = cirq.Circuit()

# 2. Aplicamos la compuerta Pauli-Y utilizando cirq.Y
circuito_y.append(cirq.Y(qubit))

# Renderizado gráfico nativo del circuito
print("--- Diagrama del Circuito ---")
display(circuito_y)

# 3. Inicialización del simulador cuántico
simulador = cirq.Simulator()

# 4. Estado de Entrada implícito (|0⟩)
print("\n--- Análisis de Estados ---")
print("Entrada: |0⟩")

# 5. Simulación para extraer el vector de estado complejo de salida
resultado = simulador.simulate(circuito_y)

print("Salida (Notación Dirac):", resultado.dirac_notation())

# 6. Extracción numérica del State Vector para observar la componente imaginaria
vector_final = resultado.state_vector()
print("Vector de estado complejo numérico [α, β]:")
print(vector_final)
