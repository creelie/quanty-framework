class InvariantViolation(Exception):
    """
    Raised when a topological invariant is violated.
    """
    pass


class InvariantConsistencyChecker:
    """
    Checks consistency of invariants across snapshots.
    """

    def __init__(self):
        self.reference = None

    def set_reference(self, snapshot):
        self.reference = snapshot

    def check(self, snapshot):
        if self.reference is None:
            self.set_reference(snapshot)
            return True

        for name, value in snapshot.items():
            if name not in self.reference:
                continue
            if value != self.reference[name]:
                raise InvariantViolation(
                    f"Invariant '{name}' violated: "
                    f"{value} != {self.reference[name]}"
                )
        return True
