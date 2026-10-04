import cirq
import numpy as np

def construir_algoritmo_dj(tipo_oraculo):
    # REGISTRO DE ENTRADA (10 qubits = 1024 combinaciones)
    qubits_entrada = cirq.LineQubit.range(10)
    # QUBIT AUXILIAR
    qubit_auxiliar = cirq.LineQubit(10)
    
    circuito = cirq.Circuit()

    # PREPARAR EL ESTADO |−⟩ PARA PHASE KICKBACK
    circuito.append(cirq.X(qubit_auxiliar))
    circuito.append(cirq.H(qubit_auxiliar))

    # SUPERPOSICIÓN DE LAS ENTRADAS
    circuito.append(cirq.H.on_each(*qubits_entrada))

    # ORÁCULO
    if tipo_oraculo == "constante":
        pass  # f(x) = 0 (Identidad)
    elif tipo_oraculo == "equilibrado":
        for q in qubits_entrada:
            circuito.append(cirq.CNOT(q, qubit_auxiliar))

    # INTERFERENCIA
    circuito.append(cirq.H.on_each(*qubits_entrada))

    # MEDICIÓN
    circuito.append(cirq.measure(*qubits_entrada, key="resultado"))

    return circuito

# SIMULACIÓN
simulador = cirq.Simulator()

for caso in ["constante", "equilibrado"]:
    print("\n" + "=" * 60)
    print(f"ORÁCULO {caso.upper()}")
    print("=" * 60)
    
    circuito = construir_algoritmo_dj(caso)
    print(circuito)
    
    resultado = simulador.run(circuito, repetitions=1)
    bits = resultado.measurements["resultado"][0]
    cadena_bits = "".join(str(b) for b in bits)
    
    print("\nResultado medido:")
    print(cadena_bits)
    
    if np.all(bits == 0):
        print("\n>>> Deutsch-Jozsa concluye: FUNCIÓN CONSTANTE")
    else:
        print("\n>>> Deutsch-Jozsa concluye: FUNCIÓN EQUILIBRADA")
        
    print("\nConsultas realizadas al oráculo: 1")