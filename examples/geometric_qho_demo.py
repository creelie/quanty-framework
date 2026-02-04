import numpy as np
from quanty.algorithms.geometric_qho import GeometricQuantumHarmonicOscillator

algo = GeometricQuantumHarmonicOscillator(dt=0.05)
x0 = np.array([1.0, 0.0])

energy_expectation = algo.run(x0, steps=100)

print("Geometric QHO energy expectation:")
print(energy_expectation)
