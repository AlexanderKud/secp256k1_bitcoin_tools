'''
This method cannot help break secp256k1 security but answers the question whether point is even or odd  without calculating its scalar.
Based on consecutive subtraction of 2: even will come to 2, odd will come to 3.
(8)8-2=6
   6-2=4
   4-2=2
(9)9-2=7
   7-2=5
   5-2=3
'''
from secp256k1 import *

curve_2G = scalar_multiplication(2)
curve_3G = scalar_multiplication(3)
Q = scalar_multiplication(889004)
if Q == curve.g:
    raise ValueError('secp256k1 default Generator point is odd (has scalar 1)')
while True:
    if Q == curve_2G:
        print(f'Point is even (has Q=k(even scalar)*G)')
        break
    if Q == curve_3G:
        print(f'Point is odd (has Q=k(odd scalar)*G')
        break
    Q = point_subtraction(Q, curve_2G)
