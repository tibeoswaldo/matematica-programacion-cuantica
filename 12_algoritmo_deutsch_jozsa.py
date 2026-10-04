import cirq
import numpy as np
from IPython.display import display

def construir_algoritmo_dj(tipo_oraculo):

    # ======================================================
    # REGISTRO DE ENTRADA
    # 10 qubits de entrada
    # Permiten representar 2^10 = 1024 combinaciones.

    qubits_entrada = cirq.LineQubit.range(10)

    # ======================================================
    # QUBIT AUXILIAR
    # Almacena la respuesta del oráculo.

    qubit_auxiliar = cirq.LineQubit(10)
    circuito = cirq.Circuit()

    # ======================================================
    # PREPARAR EL ESTADO |−⟩
    # ======================================================
    # |0⟩
    #  X
    # |1⟩
    #  H
    # |−⟩=(|0⟩−|1⟩)/√2
    # Esto permite el Phase Kickback.
    # ======================================================

    circuito.append(cirq.X(qubit_auxiliar))
    circuito.append(cirq.H(qubit_auxiliar))

    # ======================================================
    # SUPERPOSICIÓN DE LAS 1024 ENTRADAS
    # ======================================================

    circuito.append(cirq.H.on_each(*qubits_entrada))

    # ======================================================
    # ORÁCULO
    # ======================================================

    if tipo_oraculo == "constante":
        # f(x)=0 para todo x
        # No hacemos nada.
        pass

    elif tipo_oraculo == "equilibrado":
        # f(x)=x0⊕x1⊕...⊕x9
        # La mitad de las entradas produce 0
        # y la otra mitad produce 1.
        for q in qubits_entrada:
            circuito.append(cirq.CNOT(q, qubit_auxiliar))
    # ======================================================
    # INTERFERENCIA
    # ======================================================
    circuito.append(cirq.H.on_each(*qubits_entrada))
    # ======================================================
    # MEDICIÓN
    # ======================================================
    circuito.append(cirq.measure(*qubits_entrada,key="resultado"))

    return circuito

# ==========================================================
# SIMULACIÓN
# ==========================================================
simulador = cirq.Simulator()
for caso in ["constante", "equilibrado"]:

    print("\n" + "=" * 60)
    print(f"ORÁCULO {caso.upper()}")
    print("=" * 60)

    circuito = construir_algoritmo_dj(caso)
    display(circuito)
    resultado = simulador.run(circuito,repetitions=1)

    bits = resultado.measurements["resultado"][0]

    cadena_bits = "".join(str(b) for b in bits)

    print("\nResultado medido:")
    print(cadena_bits)

    if np.all(bits == 0):
        print("\n>>> Deutsch-Jozsa concluye: FUNCIÓN CONSTANTE")
    else:
        print("\n>>> Deutsch-Jozsa concluye: FUNCIÓN EQUILIBRADA")
    print("\nConsultas realizadas al oráculo: 1")
