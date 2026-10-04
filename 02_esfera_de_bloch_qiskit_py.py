import numpy as np
from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector
from qiskit.visualization import plot_bloch_multivector

# Crea un circuito cuántico con 1 qubit
# Inicialmente el qubit se encuentra en el estado |0>
qc = QuantumCircuit(1)

# Aplica la compuerta Hadamard al qubit 0
qc.h(0)

# Aplica una rotación de 45 grados (π/4 radianes) alrededor del eje Y
qc.ry(np.pi / 4, 0)

# Obtiene el vector de estado resultante
estado = Statevector.from_instruction(qc)

# Dibuja la esfera de Bloch mostrando la posición final del estado
plot_bloch_multivector(estado)