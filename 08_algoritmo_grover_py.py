import cirq
import numpy as np

# CONFIGURACIÓN DEL PROBLEMA (10 qubits = 1024 esferas)
qubits = cirq.LineQubit.range(10)
simulador = cirq.Simulator()

# ESFERA NEGRA OCULTA: Elemento 768 (1100000000 en binario)
esfera_negra_bits = [1, 1, 0, 0, 0, 0, 0, 0, 0, 0]
print("Esfera negra oculta:")
print("".join(map(str, esfera_negra_bits)))

# ORÁCULO DE GROVER
def construir_oraculo(qubits, estado_oculto):
    operaciones = []
    for q, bit in zip(qubits, estado_oculto):
        if bit == 0:
            operaciones.append(cirq.X(q))
            
    operaciones.append(
        cirq.Z(qubits[-1]).controlled_by(*qubits[:-1])
    )
    
    for q, bit in zip(qubits, estado_oculto):
        if bit == 0:
            operaciones.append(cirq.X(q))
    return operaciones

# DIFUSOR DE GROVER
def construir_difusor(qubits):
    operaciones = []
    operaciones.append(cirq.H.on_each(*qubits))
    operaciones.append(cirq.X.on_each(*qubits))
    operaciones.append(
        cirq.Z(qubits[-1]).controlled_by(*qubits[:-1])
    )
    operaciones.append(cirq.X.on_each(*qubits))
    operaciones.append(cirq.H.on_each(*qubits))
    return operaciones

# CONSTRUCCIÓN DEL CIRCUITO
circuito_grover = cirq.Circuit()
circuito_grover.append(cirq.H.on_each(*qubits))

num_iteraciones = 25
print(f"\nIteraciones de Grover: {num_iteraciones}")

for _ in range(num_iteraciones):
    circuito_grover.append(construir_oraculo(qubits, esfera_negra_bits))
    circuito_grover.append(construir_difusor(qubits))

circuito_grover.append(cirq.measure(*qubits, key="tombola"))

# EJECUCIÓN
resultado = simulador.run(circuito_grover, repetitions=1)
esfera_encontrada = resultado.measurements["tombola"][0]
cadena_binaria = "".join(str(bit) for bit in esfera_encontrada)
indice_encontrado = int(cadena_binaria, 2)

print("\n" + "=" * 60)
print("RESULTADO DE LA BÚSQUEDA CUÁNTICA")
print("=" * 60)
print(f"Estado encontrado: {cadena_binaria}")
print(f"Índice encontrado: {indice_encontrado}")

if np.array_equal(esfera_encontrada, np.array(esfera_negra_bits)):
    print("\n>>> ¡ÉXITO!")
    print(">>> Se encontró la esfera negra.")
else:
    print("\n>>> La medición no encontró la esfera correcta.")

print("\nCosto clásico aproximado: ≈ 512 búsquedas promedio")
print(f"Costo cuántico: {num_iteraciones} consultas al oráculo")