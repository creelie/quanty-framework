class TTTransition:
    """
    Topologically Transient (TT) transition.
    """

    def __init__(self, name, apply_fn, revert_fn):
        """
        apply_fn: function performing controlled change
        revert_fn: function reverting the change
        """
        self.name = name
        self.apply_fn = apply_fn
        self.revert_fn = revert_fn

    def apply(self):
        self.apply_fn()

    def revert(self):
        self.revert_fn()
