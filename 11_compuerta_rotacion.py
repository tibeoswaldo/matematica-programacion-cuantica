import cirq
import numpy as np

# 1. Configuración del hardware simulado y qubit
qubit = cirq.LineQubit(0)
simulador = cirq.Simulator()
circuito = cirq.Circuit()

# 2. Aplicamos una rotación en Y de pi / 3 (60 grados)
# Teóricamente esto genera un estado con:
# Probabilidad de |0> = cos^2(60/2) = cos^2(30) = 0.75 (75%)
# Probabilidad de |1> = sin^2(60/2) = sin^2(30) = 0.25 (25%)
angulo = np.pi / 3
circuito.append(cirq.ry(angulo)(qubit))

# 3. Asignamos la Llave de Medición (Measurement Key) como explicaste
circuito.append(cirq.measure(qubit, key='medicion_angular'))

print("--- Esquema del Circuito de Rotación ---")
print(circuito)
print("\n" + "="*50 + "\n")

# =====================================================================
# DEMOSTRACIÓN 1: El problema del "Single Shot" (1 sola repetición)
# =====================================================================
print("--- EXPERIMENTO 1: Un solo disparo (Single Shot) ---")
resultado_unico = simulador.run(circuito, repetitions=1)
print(f"Resultado bruto: {resultado_unico}")
# Intentar armar un histograma con 1 dato no tiene sentido algorítmico:
print(f"Histograma tramposo: {resultado_unico.histogram(key='medicion_angular')}")
print("CONCLUSIÓN: Este único bit no te dice que el algoritmo tenía un 75% de probabilidad.")
print("\n" + "="*50 + "\n")

# =====================================================================
# DEMOSTRACIÓN 2: Mitigación y Precisión con 1000 Repeticiones
# =====================================================================
print("--- EXPERIMENTO 2: Muestreo masivo (repetitions=1000) ---")
instancia_estadistica = simulador.run(circuito, repetitions=1000)

# Extraemos el conteo del diccionario usando nuestra llave especializada
histograma_real = instancia_estadistica.histogram(key='medicion_angular')

print("Resultados del Histograma (Frecuencias absolutas):")
print(histograma_real)

# Convertimos a porcentajes para validar la teoría
total_disparos = 1000
print("\nDistribución porcentual empírica:")
for estado, conteo in histograma_real.items():
    porcentaje = (conteo / total_disparos) * 100
    print(f"Estado |{estado}⟩: {porcentaje}% (Salió {conteo} veces)")

print("\nCONCLUSIÓN: La Ley de los Grandes Números funciona. Los porcentajes se aproximan al 75% y 25% teórico.")
