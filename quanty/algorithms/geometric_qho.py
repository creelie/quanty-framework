import numpy as np
from quanty.core.manifold import SymplecticManifold
from quanty.core.hamiltonian import HamiltonianSystem
from quanty.core.symplectic import SymplecticIntegrator
from quanty.core.observables import Observable, ExpectationValue

class GeometricQuantumHarmonicOscillator:
    """
    Geometric formulation of the quantum harmonic oscillator.
    """

    def __init__(self, dt=0.05):
        self.manifold = SymplecticManifold(2)

        def H(x):
            return 0.5 * (x[0]**2 + x[1]**2)

        self.system = HamiltonianSystem(self.manifold, H)
        self.integrator = SymplecticIntegrator(self.system, dt=dt)
        self.energy = Observable(H)

    def run(self, x0, steps=100):
        traj = self.integrator.evolve(x0, steps)
        expectation = ExpectationValue(self.energy)
        return expectation.compute(traj)
