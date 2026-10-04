# Importa la clase QuantumCircuit para crear circuitos cuánticos
from qiskit import QuantumCircuit

# Importa la clase Statevector para obtener el estado cuántico del sistema
from qiskit.quantum_info import Statevector

# Importa la función para visualizar el estado en la esfera de Bloch
from qiskit.visualization import plot_bloch_multivector

# Importa NumPy para utilizar constantes matemáticas como pi
import numpy as np

# Crea un circuito cuántico con 1 qubit
# Inicialmente el qubit se encuentra en el estado |0>
qc = QuantumCircuit(1)

# Aplica la compuerta Hadamard al qubit 0. Convierte el estado |0>
# en una superposición: (|0> + |1>) / sqrt(2)
qc.h(0)

# Aplica una rotación de 45 grados (π/4 radianes)
# alrededor del eje Y de la esfera de Bloch
qc.ry(np.pi/4, 0)

# Ejecuta matemáticamente el circuito y obtiene
# el vector de estado resultante del qubit
estado = Statevector.from_instruction(qc)

# Dibuja la esfera de Bloch mostrando la posición
# final del estado cuántico después de las operaciones
plot_bloch_multivector(estado)
