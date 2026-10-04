import numpy as np

# Definición del estado base |0> y |1>
ket0 = np.array([[1], [0]])
ket1 = np.array([[0], [1]])

# Superposición equiprobable |+>
psi = (1 / np.sqrt(2)) * (ket0 + ket1)

print("Vector para |0>:\n", ket0)
print("\nVector para |1>:\n", ket1)
print("\nEstado de superposición:\n", psi)