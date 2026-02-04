from quanty.topology.consistency import InvariantViolation

class TTManager:
    """
    Manages Topologically Transient transitions.
    """

    def __init__(self, tracker, checker):
        self.tracker = tracker
        self.checker = checker

    def execute(self, transition):
        """
        Apply TT transition with invariant protection.
        """
        # Snapshot before
        before = self.tracker.snapshot()

        try:
            transition.apply()
            after = self.tracker.snapshot()
            self.checker.check(after)
        except InvariantViolation as e:
            # Rollback on violation
            transition.revert()
            raise RuntimeError(
                f"TT transition '{transition.name}' failed: invariant violation"
            ) from e

        return True
