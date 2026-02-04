class InvariantTracker:
    """
    Tracks topological invariants during computation.
    """

    def __init__(self):
        self.invariants = {}

    def register(self, invariant):
        self.invariants[invariant.name] = invariant

    def snapshot(self, system_state=None):
        """
        Compute all registered invariants.
        """
        return {
            name: inv.compute(system_state)
            for name, inv in self.invariants.items()
        }
