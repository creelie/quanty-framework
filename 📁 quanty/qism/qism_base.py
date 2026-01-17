"""
Quantum Inner State Manifold (QISM) base structures.

This module provides abstract data structures corresponding to the
QISM constructions introduced in the QuanTY manuscript.
"""

class QISM:
    def __init__(self, dimension, symplectic_form=None):
        self.dimension = dimension
        self.symplectic_form = symplectic_form

    def product(self, other):
        """
        Formal product of QISMs, corresponding to product manifolds.
        """
        return QISM(
            self.dimension + other.dimension,
            symplectic_form=(self.symplectic_form, other.symplectic_form)
        )
