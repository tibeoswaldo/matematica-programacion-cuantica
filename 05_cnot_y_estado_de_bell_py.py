import cirq

# ==========================================================
# PASO 1: CREACIÓN DE LOS QUBITS Y SIMULADOR
# ==========================================================
q0 = cirq.LineQubit(0)
q1 = cirq.LineQubit(1)
simulador = cirq.Simulator()

# ==========================================================
# PASO 2: ESTADO INICIAL (|00⟩)
# ==========================================================
circuito_inicial = cirq.Circuit()
resultado_inicial = simulador.simulate(circuito_inicial, qubit_order=[q0, q1])
print("--- Estado Inicial ---")
print(cirq.dirac_notation(resultado_inicial.final_state_vector))

# ==========================================================
# PASO 3: CREAR UNA SUPERPOSICIÓN CON HADAMARD
# ==========================================================
circuito_h = cirq.Circuit(cirq.H(q0))
resultado_h = simulador.simulate(circuito_h)
print("\n--- Después de H(q0) ---")
print(cirq.dirac_notation(resultado_h.final_state_vector))

# ==========================================================
# PASO 4: CONSTRUIR Y EVALUAR EL ESTADO DE BELL (|Φ⁺⟩)
# ==========================================================
circuito_bell = cirq.Circuit()
circuito_bell.append(cirq.H(q0))
circuito_bell.append(cirq.CNOT(q0, q1))

print("\n--- Circuito del Estado de Bell ---")
print(circuito_bell)

resultado_bell = simulador.simulate(circuito_bell)
print("\n--- Estado de Bell ---")
print(cirq.dirac_notation(resultado_bell.final_state_vector))

print("\n--- Vector de Estado ---")
print(resultado_bell.final_state_vector)