from secp256k1 import *

N    = 115792089237316195423570985008687907852837564279074904382605163141518161494337
mid2 = 57896044618658097711785492504343953926418782139537452191302581570759080747169

#def multiplicative_inverse(x, m):
    #return pow(x, m - 2, m)
    
def multiplicative_inverse(a, n): #Extended Euclidean Algorithm "division" in elliptic curves
    lm = 1
    hm = 0
    low = a%n
    high = n
    while low > 1:
        ratio = high//low
        nm = hm-lm*ratio
        new = high-low*ratio
        high = low
        low = new
        hm = lm
        lm = nm
    return lm % n
    
def additive_inverse(a):
    return N - a
    
def add(a, b):
    return (a + b) % N

def sub(a, b):
    return (a + additive_inverse(b)) % N

def mul(a, b):
    return (a * b) % N
    
def div(a, b):
    return (a * multiplicative_inverse(b, N)) % N

def parse_pubkey(pubkey):
    if pubkey.startswith('04'):
        x = pubkey[2:66]
        y = pubkey[66:]
        Q = [int(x, 16), int(y, 16)]
        return Q
    p = 0xfffffffffffffffffffffffffffffffffffffffffffffffffffffffefffffc2f
    if pubkey.startswith('02'):
        x = int(pubkey[2:66], 16)
        ysquared = ((x*x*x+7) % p)      
        y1 = pow(ysquared, (p+1)//4, p)
        y2 = p - y1
        if int(str(y1)[-1]) % 2 == 0:
            Q = [x, y1]
            return Q
        else:
            Q = [x, y2]
            return Q
    if pubkey.startswith('03'):
        x = int(pubkey[2:66], 16)
        ysquared = ((x*x*x+7) % p)      
        y1 = pow(ysquared, (p+1)//4, p)
        y2 = p - y1
        if int(str(y1)[-1]) % 2 == 0:
            Q = [x, y2]
            return Q
        else:
            Q = [x, y1]
            return Q

G = scalar_multiplication(1)
p05 = scalar_multiplication(57896044618658097711785492504343953926418782139537452191302581570759080747169)
scalar = 57896044618658097711785492504343953926418782139537452191302581570759080747178
print(f'Scalar: {scalar} {scalar / 2}')
point = scalar_multiplication(scalar)
check_point = point_to_upub(point)
print(f'Point: {point_to_upub(point)}')
div_point = point_division(point, 2)
print(f'Div_Point: {point_to_upub(div_point)}')

if scalar % 2 == 0:
    sub_point = div_point
if scalar % 2 == 1:
    sub_point = point_subtraction(div_point, p05)

final_point = point_addition(div_point, sub_point)
even = False
for i in range(3):
    if point_to_upub(final_point) == check_point:
        even = True
        break
    final_point = point_addition(final_point, G)

if even == True:
    print(f'Point is even')
else:
    print(f'Point is odd')
