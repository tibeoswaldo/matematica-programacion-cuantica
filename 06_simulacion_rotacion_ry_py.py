import cirq
import numpy as np

# Configuración del hardware simulado y qubit
qubit = cirq.LineQubit(0)
simulador = cirq.Simulator()
circuito = cirq.Circuit()

# Rotación en Y de pi / 3 (60 grados)
angulo = np.pi / 3
circuito.append(cirq.ry(angulo)(qubit))
circuito.append(cirq.measure(qubit, key='medicion_angular'))

print("--- Esquema del Circuito de Rotación ---")
print(circuito)
print("\n" + "=" * 50 + "\n")

# DEMOSTRACIÓN 1: Un solo disparo (Single Shot)
print("--- EXPERIMENTO 1: Un solo disparo (Single Shot) ---")
resultado_unico = simulador.run(circuito, repetitions=1)
print(f"Resultado bruto: {resultado_unico}")
print(f"Histograma tramposo: {resultado_unico.histogram(key='medicion_angular')}")

print("\n" + "=" * 50 + "\n")

# DEMOSTRACIÓN 2: Muestreo masivo (repetitions=1000)
print("--- EXPERIMENTO 2: Muestreo masivo (repetitions=1000) ---")
instancia_estadistica = simulador.run(circuito, repetitions=1000)
histograma_real = instancia_estadistica.histogram(key='medicion_angular')

print("Resultados del Histograma (Frecuencias absolutas):")
print(histograma_real)

print("\nDistribución porcentual empírica:")
total_disparos = 1000
for estado, conteo in histograma_real.items():
    porcentaje = (conteo / total_disparos) * 100
    print(f"Estado |{estado}⟩: {porcentaje}% (Salió {conteo} veces)")