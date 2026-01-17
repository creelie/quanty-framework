"""
Examples of low-dimensional Quantum Inner State Manifolds.
"""

from .qism_base import QISM

def sphere_qism():
    """Formal QISM corresponding to S^2."""
    return QISM(dimension=2)

def product_spheres(Y):
    """Formal product QISM (S^2)^Y."""
    return QISM(dimension=2 * Y)
