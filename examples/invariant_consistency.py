import numpy as np
from quanty.core.manifold import SymplecticManifold
from quanty.core.hamiltonian import HamiltonianSystem
from quanty.core.symplectic import SymplecticIntegrator

from quanty.topology.floer import FloerChainComplex
from quanty.topology.invariants import FloerRankInvariant
from quanty.topology.tracker import InvariantTracker
from quanty.topology.consistency import InvariantConsistencyChecker, InvariantViolation

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

tracker = InvariantTracker()
tracker.register(FloerRankInvariant(CF))

checker = InvariantConsistencyChecker()

# First snapshot (reference)
snapshot1 = tracker.snapshot()
checker.set_reference(snapshot1)

print("Initial snapshot OK:", snapshot1)

# Modify topology (simulate violation)
CF.add_generator("x2", degree=2)

snapshot2 = tracker.snapshot()

try:
    checker.check(snapshot2)
except InvariantViolation as e:
    print("Invariant violation detected:")
    print(e)
