import numpy as np

# Estado base |0>
ket0 = np.array([[1], [0]])

# Estado base |1>
ket1 = np.array([[0], [1]])

# Superposición
psi = (1/np.sqrt(2)) * (ket0 + ket1)

print("Estado |0>:")
print(ket0)
print("\nEstado |1>:")
print(ket1)
print("\nEstado de superposición:")
print(psi)
