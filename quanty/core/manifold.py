import numpy as np

class SymplecticManifold:
    def __init__(self, dimension):
        if dimension % 2 != 0:
            raise ValueError("Dimension must be even")
        self.dimension = dimension

    def symplectic_form(self):
        n = self.dimension // 2
        return np.block([
            [np.zeros((n, n)), np.eye(n)],
            [-np.eye(n), np.zeros((n, n))]
        ])
