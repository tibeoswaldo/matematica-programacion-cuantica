import cirq

# 1. Instanciación del qubit y del motor de simulación cuántica
qubit = cirq.NamedQubit("MiQubit")
simulator = cirq.Simulator()

# 2. Inicialización del pipeline cuántico
circuito_z = cirq.Circuit()

# 3. Aplicación del operador de Hadamard (H) para preparar el estado |+⟩
circuito_z.append(cirq.H(qubit))

# --- Estado de Entrada para la compuerta Z ---
# Simulamos transitoriamente para registrar el vector de estado antes de aplicar Z
estado_antes_de_z = simulator.simulate(circuito_z)
print("Estado antes de Pauli-Z (|+⟩):", estado_antes_de_z.dirac_notation())

# 4. Aplicación del operador Pauli-Z (Phase-Flip)
circuito_z.append(cirq.Z(qubit))

# --- Estado de Salida de la compuerta Z ---
# Simulamos el circuito completo para evaluar la rotación de fase
estado_despues_de_z = simulator.simulate(circuito_z)
print("Estado después de Pauli-Z (|-⟩):", estado_despues_de_z.dirac_notation())

# 5. Inserción de la medición y muestreo estadístico
circuito_z.append(cirq.measure(qubit, key='resultado_fase'))
datos = simulator.run(circuito_z, repetitions=10)

print("\n--- Distribución de frecuencias finales ---")
print(datos.histogram(key='resultado_fase'))
