import cirq

# 1. Instanciación del qubit (registro cuántico) 
# y del motor de simulación cuántica
moneda = cirq.NamedQubit("MiMoneda")
simulator = cirq.Simulator()

# 2. Inicialización del objeto Circuit 
# (estructura de datos para el pipeline cuántico)
circuito_moneda = cirq.Circuit()

# 3. Aplicación del operador de Hadamard (H) para transformar 
# el estado base del qubit de |0⟩ a una superposición 
# lineal equiprobable: |+⟩ = (|0⟩ + |1⟩) / √2
circuito_moneda.append(cirq.H(moneda))

# 4. Inserción de la operación de medición en la base 
# computacional (Eje Z).
# Esto provoca el colapso del vector de estado hacia 
# uno de los autoestados (|0⟩ o |1⟩).
circuito_moneda.append(cirq.measure(moneda, key='resultado_final'))

print("--- Representación esquemática del circuito ---")
print(circuito_moneda)

# 5. Ejecución del experimento mediante un 
# muestreo estadístico (Shots / Repeticiones)
# Esto simula el comportamiento aleatorio dictado por la regla de Born.
datos = simulator.run(circuito_moneda, repetitions=10)

print("\n--- Distribución de frecuencias (Histograma) ---")
# Muestra el conteo empírico de las transiciones a los estados |0⟩ y |1⟩
print(datos.histogram(key='resultado_final'))
