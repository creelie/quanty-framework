class TopologicalInvariant:
    """
    Abstract topological invariant.
    """

    def __init__(self, name):
        self.name = name

    def compute(self, system_state):
        """
        Compute invariant from system state.
        Must be overridden.
        """
        raise NotImplementedError


class FloerRankInvariant(TopologicalInvariant):
    """
    Simple invariant: rank of Floer homology.
    """

    def __init__(self, floer_complex):
        super().__init__("FloerRank")
        self.floer = floer_complex

    def compute(self, system_state=None):
        data = self.floer.compute_homology()
        return data["num_generators"]
