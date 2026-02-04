import numpy as np

class HamiltonianSystem:
    """
    Hamiltonian system on a symplectic manifold.
    """

    def __init__(self, manifold, hamiltonian, eps=1e-6):
        self.manifold = manifold
        self.H = hamiltonian
        self.J = manifold.symplectic_form()
        self.eps = eps

    def gradient(self, x):
        grad = np.zeros_like(x, dtype=float)
        for i in range(len(x)):
            dx = np.zeros_like(x, dtype=float)
            dx[i] = self.eps
            grad[i] = (self.H(x + dx) - self.H(x - dx)) / (2 * self.eps)
        return grad

    def vector_field(self, x):
        gradH = self.gradient(x)
        return self.J @ gradH
