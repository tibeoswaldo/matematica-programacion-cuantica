import cirq
import numpy as np
# ==========================================================
# 1. CONFIGURACIÓN DEL PROBLEMA
# ==========================================================
# Tenemos 1024 esferas dentro de una tómbola.
# Solo una es la esfera negra.
# Como:
#     2^10 = 1024
# necesitamos 10 qubits para representar todas las esferas.
# ==========================================================

qubits = cirq.LineQubit.range(10)
simulador = cirq.Simulator()

# ==========================================================
# ESFERA NEGRA OCULTA
# ==========================================================
# Elegimos arbitrariamente la esfera número 768.
# 768 en binario:
#     1100000000
# ==========================================================

esfera_negra_bits = [1, 1, 0, 0, 0, 0, 0, 0, 0, 0]

print("Esfera negra oculta:")
print("".join(map(str, esfera_negra_bits)))

# ==========================================================
# 2. ORÁCULO DE GROVER
# ==========================================================
# El oráculo marca únicamente la esfera negra.
# Matemáticamente:
#     |x> → -|x>    si x es la esfera negra
#     |x> →  |x>    en cualquier otro caso
# Es decir, solamente invierte la fase del estado buscado.
# ==========================================================

def construir_oraculo(qubits, estado_oculto):
    operaciones = []
    # Convertir el estado buscado temporalmente en |111...111>
    for q, bit in zip(qubits, estado_oculto):
        if bit == 0:
            operaciones.append(cirq.X(q))

    # Aplicar una Z multicontrolada
    operaciones.append(
        cirq.Z(qubits[-1]).controlled_by(*qubits[:-1])
    )

    # Restaurar el estado original
    for q, bit in zip(qubits, estado_oculto):
        if bit == 0:
            operaciones.append(cirq.X(q))

    return operaciones
# ==========================================================
# 3. DIFUSOR DE GROVER
# ==========================================================
# Amplifica la probabilidad del estado marcado.
# Matemáticamente realiza una reflexión respecto
# al promedio de amplitudes.
# ==========================================================

def construir_difusor(qubits):
    operaciones = []
    # H
    operaciones.append(cirq.H.on_each(*qubits))
    # X
    operaciones.append(cirq.X.on_each(*qubits))
    # Reflexión sobre |000...0>
    operaciones.append(
        cirq.Z(qubits[-1]).controlled_by(*qubits[:-1])
    )
    # X
    operaciones.append(cirq.X.on_each(*qubits))
    # H
    operaciones.append(cirq.H.on_each(*qubits))
    return operaciones
# ==========================================================
# 4. CONSTRUCCIÓN DEL CIRCUITO
# ==========================================================
circuito_grover = cirq.Circuit()
# ----------------------------------------------------------
# SUPERPOSICIÓN INICIAL
# ----------------------------------------------------------
# Colocamos simultáneamente las 1024 esferas
# en superposición.
#     |0000000000>
# pasa a:
#     1/sqrt(1024) Σ|x>
# ----------------------------------------------------------

circuito_grover.append(cirq.H.on_each(*qubits))

# ==========================================================
# ITERACIONES DE GROVER
# ==========================================================
# Número óptimo:    k ≈ π/4 * √N
# Para:             N = 1024
# obtenemos:        k ≈ 25
# ==========================================================

num_iteraciones = 25
print(f"\nIteraciones de Grover: {num_iteraciones}")

for _ in range(num_iteraciones):
    # Marcar la esfera negra
    circuito_grover.append(construir_oraculo(qubits,esfera_negra_bits))
    # Amplificar su probabilidad
    circuito_grover.append(construir_difusor(qubits))

# ==========================================================
# MEDICIÓN FINAL
# ==========================================================

circuito_grover.append(cirq.measure(*qubits,key="tombola"))

# ==========================================================
# 5. EJECUCIÓN
# ==========================================================
# Una sola medición final.
# ==========================================================

resultado = simulador.run(circuito_grover,repetitions=1)
esfera_encontrada = resultado.measurements["tombola"][0]

# Convertir a cadena binaria
cadena_binaria = "".join(str(bit) for bit in esfera_encontrada)

# Convertir a decimal
indice_encontrado = int(cadena_binaria, 2)

# ==========================================================
# RESULTADOS
# ==========================================================
print("\n" + "=" * 60)
print("RESULTADO DE LA BÚSQUEDA CUÁNTICA")
print("=" * 60)
print(f"Estado encontrado: {cadena_binaria}")
print(f"Índice encontrado: {indice_encontrado}")

if np.array_equal(esfera_encontrada,np.array(esfera_negra_bits)):
    print("\n>>> ¡ÉXITO!")
    print(">>> Se encontró la esfera negra.")
else:
    print("\n>>> La medición no encontró la esfera correcta.")
    print(">>> Esto puede ocurrir debido a la naturaleza probabilística.")

print("\nCosto clásico aproximado:")
print("≈ 512 búsquedas promedio")
print("\nCosto cuántico:")
print(f"{num_iteraciones} consultas al oráculo")
print("1 medición final")
