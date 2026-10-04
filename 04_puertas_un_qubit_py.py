import cirq

# ==========================================
# 1. PUERTA PAULI-X (NOT)
# ==========================================
print("--- 1. PUERTA PAULI-X ---")
qubit_x = cirq.LineQubit(0)
circuito_x = cirq.Circuit(cirq.X(qubit_x))

estado_inicial = cirq.StateVectorState.from_state_vector_or_qubit_count(1)
print("Entrada:", estado_inicial.dirac_notation())

simulador = cirq.Simulator()
resultado_x = simulador.simulate(circuito_x)
print("Salida: ", resultado_x.dirac_notation())

# ==========================================
# 2. PUERTA HADAMARD (H)
# ==========================================
print("\n--- 2. PUERTA HADAMARD ---")
moneda = cirq.NamedQubit("MiMoneda")
circuito_h = cirq.Circuit()
circuito_h.append(cirq.H(moneda))
circuito_h.append(cirq.measure(moneda, key='resultado_final'))

print(circuito_h)
datos_h = simulador.run(circuito_h, repetitions=10)
print("Distribución de frecuencias:", datos_h.histogram(key='resultado_final'))

# ==========================================
# 3. PUERTA PAULI-Z (FASE)
# ==========================================
print("\n--- 3. PUERTA PAULI-Z ---")
qubit_z = cirq.NamedQubit("MiQubit")
circuito_z = cirq.Circuit()
circuito_z.append(cirq.H(qubit_z))

estado_antes_z = simulador.simulate(circuito_z)
print("Estado antes de Z (|+⟩):", estado_antes_z.dirac_notation())

circuito_z.append(cirq.Z(qubit_z))
estado_despues_z = simulador.simulate(circuito_z)
print("Estado después de Z (|-⟩):", estado_despues_z.dirac_notation())

# ==========================================
# 4. PUERTA PAULI-Y
# ==========================================
print("\n--- 4. PUERTA PAULI-Y ---")
qubit_y = cirq.LineQubit(0)
circuito_y = cirq.Circuit(cirq.Y(qubit_y))

resultado_y = simulador.simulate(circuito_y)
print("Salida Pauli-Y (Dirac):", resultado_y.dirac_notation())
print("Vector de estado complejo numérico [α, β]:", resultado_y.state_vector())