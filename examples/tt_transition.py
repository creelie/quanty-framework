from quanty.core.manifold import SymplecticManifold
from quanty.topology.floer import FloerChainComplex
from quanty.topology.invariants import FloerRankInvariant
from quanty.topology.tracker import InvariantTracker
from quanty.topology.consistency import InvariantConsistencyChecker
from quanty.tt.transitions import TTTransition
from quanty.tt.manager import TTManager

# Setup
M = SymplecticManifold(2)
CF = FloerChainComplex(M)
CF.add_generator("x0", degree=0)
CF.add_generator("x1", degree=1)

tracker = InvariantTracker()
tracker.register(FloerRankInvariant(CF))

checker = InvariantConsistencyChecker()
checker.set_reference(tracker.snapshot())

manager = TTManager(tracker, checker)

# Controlled TT transition (no invariant change)
def apply_ok():
    print("Applying safe TT transition (geometry-only)")

def revert_ok():
    print("Reverting safe TT transition")

safe_tt = TTTransition(
    name="SafeGeometryShift",
    apply_fn=apply_ok,
    revert_fn=revert_ok
)

manager.execute(safe_tt)
print("Safe TT transition succeeded.")

# Violating TT transition
def apply_bad():
    print("Applying bad TT transition (topology change)")
    CF.add_generator("x2", degree=2)

def revert_bad():
    print("Reverting bad TT transition")
    CF.generators.pop()

bad_tt = TTTransition(
    name="BadTopologyChange",
    apply_fn=apply_bad,
    revert_fn=revert_bad
)

try:
    manager.execute(bad_tt)
except RuntimeError as e:
    print(e)
