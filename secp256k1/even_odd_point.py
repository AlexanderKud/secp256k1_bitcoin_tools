'''
This method cannot help break secp256k1 security but answers the question whether point is even or odd  without calculating its scalar.
Based on the math of first grade of school.
8=7+1
  6+2
  5+3
  4+4
 (4+4) 4 <-> 4 condition: this point is even
9=8+1
  7+2
  6+3
  5+4
 (5+4) 5 <-> 4 condition: this point is odd
'''
from secp256k1 import *

#Q = [89565891926547004231252920425935692360644145829622209833684329913297188986597,
#     12158399299693830322967808612713398636155367887041628176798871954788371653930]
Q = scalar_multiplication(128809)
if Q == curve.g:
    raise ValueError('secp256k1 default Generator point is odd (has scalar 1)')
A = point_subtraction(Q, curve.g)
B = curve.g
while True:
    if A == B:
        print(f'Point is even (has Q=k(even scalar)*G)')
        break
    if point_subtraction(A, B) == curve.g:
        print(f'Point is odd (has Q=k(odd scalar)*G)')
        break
    A = point_subtraction(A, curve.g)
    B = point_addition(B, curve.g)
