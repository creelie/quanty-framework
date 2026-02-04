import numpy as np
from quanty.core.manifold import SymplecticManifold
from quanty.core.hamiltonian import HamiltonianSystem

M = SymplecticManifold(2)

def H(x):
    return 0.5 * (x[0]**2 + x[1]**2)

system = HamiltonianSystem(M, H)

x = np.array([1.0, 0.0])
print(system.vector_field(x))
