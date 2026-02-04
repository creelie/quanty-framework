import numpy as np
from quanty.core.manifold import SymplecticManifold
from quanty.core.hamiltonian import HamiltonianSystem
from quanty.core.symplectic import SymplecticIntegrator

from quanty.topology.floer import FloerChainComplex
from quanty.topology.invariants import FloerRankInvariant
from quanty.topology.tracker import InvariantTracker

# Geometry
M = SymplecticManifold(2)

def H(x):
    return 0.5 * (x[0]**2 + x[1]**2)

system = HamiltonianSystem(M, H)
integrator = SymplecticIntegrator(system, dt=0.1)

# Topology
CF = FloerChainComplex(M)
CF.add_generator("x0", degree=0)
CF.add_generator("x1", degree=1)

floer_rank = FloerRankInvariant(CF)

tracker = InvariantTracker()
tracker.register(floer_rank)

# Evolution
x = np.array([1.0, 0.0])
trajectory = integrator.evolve(x, steps=5)

# Invariant snapshot
print("Invariant snapshot:")
print(tracker.snapshot())
