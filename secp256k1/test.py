from secp256k1 import *

P  = scalar_multiplication(2)
print(point_to_upub(P))
print(point_to_cpub(P))    
G4 = point_multiplication(P, 2)
G6 = point_addition(P, G4)
G2 = point_subtraction(G6, G4)
G2 = point_division(G6, 3)
G12 = point_doubling(G6)
G = point_halving(G2)
print(on_curve(G))
print(point_negation(G))

