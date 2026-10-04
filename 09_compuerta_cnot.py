import cirq
from IPython.display import display

# Crear qubits
control = cirq.NamedQubit("Control")
objetivo = cirq.NamedQubit("Objetivo")

# Simulador
simulador = cirq.Simulator()

# ==========================================
# ESTADO INICIAL
# ==========================================

circuito_inicial = cirq.Circuit()

resultado_inicial = simulador.simulate(circuito_inicial, qubit_order=[control, objetivo])

print("--- Estado de Entrada ---")
print(cirq.dirac_notation(resultado_inicial.final_state_vector))

# ==========================================
# PREPARACIÓN DEL CONTROL
# ==========================================

circuito_x = cirq.Circuit(
    cirq.X(control)
)

resultado_x = simulador.simulate(circuito_x)

print("\n--- Estado después de X(Control) ---")
print(cirq.dirac_notation(resultado_x.final_state_vector))

# ==========================================
# CIRCUITO COMPLETO
# ==========================================

circuito_cnot = cirq.Circuit(
    cirq.X(control),
    cirq.CNOT(control, objetivo)
)

print("\n--- Estructura del Circuito ---")
display(circuito_cnot)

resultado_final = simulador.simulate(circuito_cnot)

print("\n--- Estado Final después de CNOT ---")
print(cirq.dirac_notation(resultado_final.final_state_vector))
