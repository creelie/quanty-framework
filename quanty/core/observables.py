import numpy as np

class Observable:
    """
    Observable defined on phase space.
    """

    def __init__(self, function):
        """
        function: callable f(x)
        """
        self.f = function

    def evaluate(self, x):
        return self.f(x)


class ExpectationValue:
    """
    Expectation value over a trajectory.
    """

    def __init__(self, observable):
        self.observable = observable

    def compute(self, trajectory):
        values = [self.observable.evaluate(x) for x in trajectory]
        return np.mean(values)
