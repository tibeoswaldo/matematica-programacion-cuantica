import cirq

# PASO 1: Definir el Qubit de forma independiente
# Creamos un único qubit (en la línea 0)
qubit = cirq.LineQubit(0)

# PASO 2: Crear el contenedor del Circuito (vacío)
circuit = cirq.Circuit()

# PASO 3: Añadir la operación de medición al circuito
# Medimos el qubit directamente en su estado inicial
circuit.append(cirq.measure(qubit, key='estado_inicial'))

# --- VISUALIZACIÓN ---
print("=== Estructura del Circuito ===")
print(circuit)

print("\n=== Estructura de Momentos ===")
for i, moment in enumerate(circuit):
    print(f"Momento {i}: {moment}")

# PASO 4: Simulación en la CPU
simulator = cirq.Simulator()
resultado = simulator.run(circuit, repetitions=5)

print("\n=== Resultado (5 disparos) ===")
print(resultado)
