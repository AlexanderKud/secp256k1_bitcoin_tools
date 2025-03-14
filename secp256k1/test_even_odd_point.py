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
p025 = scalar_multiplication(86844066927987146567678238756515930889628173209306178286953872356138621120753)
p05  = scalar_multiplication(57896044618658097711785492504343953926418782139537452191302581570759080747169)
p075 = scalar_multiplication(28948022309329048855892746252171976963209391069768726095651290785379540373585)
bits_down = 2
scalar = 890999999999999999999999977777
print(f'Scalar: {scalar} {scalar / 4}')
point = scalar_multiplication(scalar)
check_point = point_to_upub(point)
print(f'Point: {point_to_upub(point)}')
print(f'Quarter_Scalar: {div(scalar, 4)}')
quarter_point = point_division(point, 4)
print(f'Quarter_Point: {point_to_upub(quarter_point)}')

if scalar % 4 == 0:
    quarter_point_whole = quarter_point
if scalar % 4 == 1:
    quarter_point_whole = point_subtraction(quarter_point, p025)
if scalar % 4 == 2:
    quarter_point_whole = point_subtraction(quarter_point, p05)
if scalar % 4 == 3:
    quarter_point_whole = point_subtraction(quarter_point, p075)
    
group = list()
group.append(point_to_upub(point))
for i in range(bits_down):
    final_group = list()
    for p in group:
        point = parse_pubkey(str(p))
        final_group.append(point_to_upub(point_multiplication(point, 57896044618658097711785492504343953926418782139537452191302581570759080747169)))
        point = point_subtraction(point, G)        
        final_group.append(point_to_upub(point_multiplication(point, 57896044618658097711785492504343953926418782139537452191302581570759080747169)))
    group = final_group

index = 1
for p in final_group:
    print(f'{index}: {p}')
    index += 1
   
print()

t = 2

a1 = parse_pubkey(final_group[0])
b1 = parse_pubkey(final_group[3])
for i in range(t):
    a1 = point_addition(a1, b1)
print(f'1: {point_to_upub(a1)}')

a2 = parse_pubkey(final_group[1])
b2 = parse_pubkey(final_group[2])
for i in range(t):
    a2 = point_addition(a2, b2)
print(f'2: {point_to_upub(a2)}')
print()
bruteforce_point1 = point_addition(a1, quarter_point_whole)
bruteforce_point2 = point_addition(a2, quarter_point_whole)
print(f'B1: {point_to_upub(bruteforce_point1)}')
print(f'B2: {point_to_upub(bruteforce_point2)}')
print()
even = False
for i in range(3):
    if point_to_upub(bruteforce_point1) == check_point or point_to_upub(bruteforce_point2) == check_point:
        even = True
        break
    bruteforce_point1 = point_addition(bruteforce_point1, G)
    bruteforce_point2 = point_addition(bruteforce_point2, G)
if even == True:
    print(f'Point is even')
else:
    print(f'Point is odd')
