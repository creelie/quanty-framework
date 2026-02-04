import numpy as np

class HamiltonianSystem:
    """
    Hamiltonian system on a symplectic manifold.
    """

    def __init__(self, manifold, hamiltonian):
        """
        manifold: SymplecticManifold
        hamiltonian: callable H(x)
        """
        self.manifold = manifold
        self.H = hamiltonian
        self.J = manifold.symplectic_form()

    def vector_field(self, x):
        """
        Compute Hamiltonian vector field X_H = J * grad(H)
        """
        grad = np.gradient(self.H(x))
        return self.J @ grad
