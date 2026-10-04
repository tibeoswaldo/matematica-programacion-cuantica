import cirq
from IPython.display import display

# ==========================================================
# PASO 1: CREACIÓN DE LOS QUBITS
# ==========================================================
# Se crean dos qubits identificados como q0 y q1.
# Al inicio de la simulación ambos se encuentran en el
# estado fundamental |0⟩.
#
# Estado inicial del sistema:
#
#     |00⟩
#
# donde:
#     q0 = |0⟩
#     q1 = |0⟩
# ==========================================================

q0 = cirq.LineQubit(0)
q1 = cirq.LineQubit(1)

# Crear el simulador cuántico que ejecutará las operaciones
# definidas en los circuitos.
simulador = cirq.Simulator()

# ==========================================================
# PASO 2: OBSERVAR EL ESTADO INICIAL DEL SISTEMA
# ==========================================================
# Se construye un circuito vacío (sin puertas cuánticas).
# Esto permite verificar el estado de entrada antes de
# realizar cualquier transformación.
# ==========================================================

circuito_inicial = cirq.Circuit()

# Simular el circuito vacío.
# Como no se aplican puertas, el sistema permanece en |00⟩.
resultado_inicial = simulador.simulate(
    circuito_inicial,
    qubit_order=[q0, q1]
)

print("--- Estado Inicial ---")

# Mostrar el estado utilizando notación de Dirac (ket).
print(cirq.dirac_notation(resultado_inicial.final_state_vector))

# ==========================================================
# PASO 3: CREAR UNA SUPERPOSICIÓN CON HADAMARD
# ==========================================================
# La puerta Hadamard (H) se aplica sobre q0.
#
# Transformación:
#
#     |0⟩ → (|0⟩ + |1⟩)/√2
#
# Como q1 permanece en |0⟩:
#
#     |00⟩ →
#     (|00⟩ + |10⟩)/√2
#
# El sistema ya no tiene un valor definido para q0,
# sino una superposición de dos posibilidades.
# ==========================================================

circuito_h = cirq.Circuit(
    cirq.H(q0)
)

# Simular únicamente la acción de la puerta Hadamard.
resultado_h = simulador.simulate(circuito_h)

print("\n--- Después de H(q0) ---")

# Mostrar la superposición obtenida.
print(cirq.dirac_notation(resultado_h.final_state_vector))

# ==========================================================
# PASO 4: CONSTRUIR EL ESTADO DE BELL
# ==========================================================
# Un Estado de Bell es un estado entrelazado formado por
# dos qubits.
#
# Para generarlo:
#
# 1) Se crea una superposición en q0 mediante Hadamard.
#
#      |00⟩ → (|00⟩ + |10⟩)/√2
#
# 2) Se aplica una compuerta CNOT utilizando:
#
#      q0 → control
#      q1 → objetivo
#
# La CNOT invierte el qubit objetivo únicamente cuando
# el qubit de control vale |1⟩.
#
# Por tanto:
#
#      |00⟩ → |00⟩
#      |10⟩ → |11⟩
#
# Resultado:
#
#      (|00⟩ + |11⟩)/√2
#
# Este estado se conoce como Estado de Bell Φ⁺.
# ==========================================================

circuito_bell = cirq.Circuit()

# Crear superposición sobre el primer qubit.
circuito_bell.append(cirq.H(q0))

# Entrelazar ambos qubits mediante una compuerta CNOT.
circuito_bell.append(cirq.CNOT(q0, q1))

print("\n--- Circuito del Estado de Bell ---")

# Mostrar gráficamente el circuito cuántico.
display(circuito_bell)

# Ejecutar la simulación completa.
resultado_bell = simulador.simulate(circuito_bell)

print("\n--- Estado de Bell ---")

# Mostrar el estado final en notación ket.
print(cirq.dirac_notation(resultado_bell.final_state_vector))

print("\n--- Vector de Estado ---")

# Mostrar las amplitudes complejas asociadas a:
#
# [ |00⟩ , |01⟩ , |10⟩ , |11⟩ ]
#
# Para el Estado de Bell se espera:
#
# [ 1/√2 , 0 , 0 , 1/√2 ]
#
print(resultado_bell.final_state_vector)
