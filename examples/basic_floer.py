from quanty.core.manifold import SymplecticManifold
from quanty.topology.floer import FloerChainComplex

M = SymplecticManifold(2)
CF = FloerChainComplex(M)

CF.add_generator("x0", degree=0)
CF.add_generator("x1", degree=1)
CF.add_differential("x1", "x0")

print("Floer data:")
print(CF.compute_homology())
