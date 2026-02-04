import numpy as np
from quanty.core.manifold import SymplecticManifold
from quanty.core.hamiltonian import HamiltonianSystem
from quanty.core.symplectic import SymplecticIntegrator
from quanty.core.observables import Observable, ExpectationValue

M = SymplecticManifold(2)

def H(x):
    return 0.5 * (x[0]**2 + x[1]**2)

system = HamiltonianSystem(M, H)
integrator = SymplecticIntegrator(system, dt=0.05)

x0 = np.array([1.0, 0.0])
trajectory = integrator.evolve(x0, steps=50)

energy = Observable(H)
expectation = ExpectationValue(energy)

print("Expectation value of energy:")
print(expectation.compute(trajectory))
