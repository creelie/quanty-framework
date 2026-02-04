import numpy as np

class SymplecticIntegrator:
    """
    Basic symplectic integrator for Hamiltonian systems.
    """

    def __init__(self, hamiltonian_system, dt=0.01):
        self.system = hamiltonian_system
        self.dt = dt

    def step(self, x):
        """
        Perform one symplectic Euler step.
        """
        X_H = self.system.vector_field(x)
        return x + self.dt * X_H

    def evolve(self, x0, steps=100):
        """
        Evolve initial state x0 for given number of steps.
        """
        traj = [x0.copy()]
        x = x0.copy()
        for _ in range(steps):
            x = self.step(x)
            traj.append(x.copy())
        return np.array(traj)
