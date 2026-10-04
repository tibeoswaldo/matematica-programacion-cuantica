import cirq

# 1. Definimos el qubit y el circuito con la compuerta X
qubit = cirq.LineQubit(0)
circuito = cirq.Circuit(cirq.X(qubit))

# 2. Estado de entrada: Por definición en computación cuántica, el estado inicial es |0⟩
estado_inicial = cirq.StateVectorState.from_state_vector_or_qubit_count(1)
print("Entrada:", estado_inicial.dirac_notation())

# 3. Estado de salida: Simulamos el circuito para ver en qué se transforma
simulador = cirq.Simulator()
resultado = simulador.simulate(circuito)
print("Salida: ", resultado.dirac_notation())
