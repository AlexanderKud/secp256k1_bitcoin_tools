N    = 115792089237316195423570985008687907852837564279074904382605163141518161494337
mid2 = 57896044618658097711785492504343953926418782139537452191302581570759080747169

#def multiplicative_inverse(x, m):
    #return pow(x, m - 2, m)
    
def multiplicative_inverse(a,n): #Extended Euclidean Algorithm "division" in elliptic curves
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
    
bits_down = 3
scalar = 1732
print(scalar)
print(f'Sub&div : {(scalar - 1024) / 4}')
print(f'Div by 4: {div(scalar, 4)} { scalar / 4}')
add_sc = add(mid2, scalar)
print(f'mid2+sc : {add_sc}')
dd = mul(add_sc, 2)
print(f'Dbl sc  : {dd}')
scalar_aux = scalar
numb = 0
for i in range(bits_down):
    if scalar_aux % 2 == 0: 
        numb = scalar_aux // 2
    else:
        scalar_aux = scalar_aux - 1
        numb = scalar_aux // 2
    scalar_aux = numb
print(f'Quarter : {scalar_aux}')
group = list()
group.append(scalar)
for i in range(bits_down):
    final_group = list()
    for p in group:
        final_group.append(div(p,2))
        p = sub(p, 1)        
        final_group.append(div(p,2))
    group = final_group
print(f'Number of scalars: {len(final_group)}')
print()
index = 1
for p in final_group:
    print(f'{index}: {p}')
    index += 1
    
print()
'''
index = 1
for p in final_group:
    num = p
    for i in range(bits_down):
        num = mul(num, 2)
    print(f'{index}: {num}')
    index += 1

print()
'''
t = 2
'''
a = final_group[0]
b = final_group[1]
for i in range(t):
    a = add(a, b)
print(a)
a1 = a
a = final_group[1]
b = final_group[0]
for i in range(t):
    a = add(a, b)
print(a)
a2 = a
print()

a = final_group[2]
b = final_group[3]
for i in range(t):
    a = add(a, b)
print(a)
a3 = a
a = final_group[3]
b = final_group[2]
for i in range(t):
    a = add(a, b)
print(a)
a4 = a

print()
'''

a = final_group[0]
b = final_group[3]
for i in range(t):
    a = add(a, b)
print(f'1: {a}')
#print(f'1: {mul(a, 2)}')

a = final_group[1]
b = final_group[2]
for i in range(t):
    a = add(a, b)
print(f'2: {a}')

print()

print(f'1: {mul(final_group[0], 3)}')
print(f'2: {mul(final_group[1], 3)}')
#print(f'2: {mul(a, 2)}')

#print()
#print(add(2977295128470898845278694445825232315757005765668176263664881903198046356448, 20291113249042998852354728983389728747391929301735209484989154491319042367872))
'''
k = pow(4, N-2, N)
print(mul(k, a1))
print(mul(k, a2))
print(mul(k, a3))
print(mul(k, a4))
'''
'''
s = sub(scalar, 1024)
#print(s)
sd = div(s, 4)
#print(sd)
sd_a = 290
print()
print(add(sd_a, a1))
print(add(sd_a, a2))
print(add(sd_a, a3))
print(add(sd_a, a4))
'''
'''
#******************************
a = 28948022309329048855892746252171976963209391069768726095651290785379540374961
num = a
for i in range(2):
    num = add(num, a)
print()
h = num
hs = sub(h, dd)
print()
print(add(28948022309329048855892746252171976963209391069768726095651290785379540374961, hs))
print(add(86844066927987146567678238756515930889628173209306178286953872356138621122130, hs))
print(add(1376, hs))
print(add(57896044618658097711785492504343953926418782139537452191302581570759080748545, hs))
print()
#*****************************
a = 86844066927987146567678238756515930889628173209306178286953872356138621122130
num = a
for i in range(2):
    num = add(num, a)
print()
h = num
hs = sub(h, dd)
print()
print(add(28948022309329048855892746252171976963209391069768726095651290785379540374961, hs))
print(add(86844066927987146567678238756515930889628173209306178286953872356138621122130, hs))
print(add(1376, hs))
print(add(57896044618658097711785492504343953926418782139537452191302581570759080748545, hs))
#*****************************
a = 1376
num = a
for i in range(2):
    num = add(num, a)
print()
h = num
hs = sub(h, dd)
print()
print(add(28948022309329048855892746252171976963209391069768726095651290785379540374961, hs))
print(add(86844066927987146567678238756515930889628173209306178286953872356138621122130, hs))
print(add(1376, hs))
print(add(57896044618658097711785492504343953926418782139537452191302581570759080748545, hs))
#*****************************
a = 57896044618658097711785492504343953926418782139537452191302581570759080748545
num = a
for i in range(2):
    num = add(num, a)
print()
h = num
hs = sub(h, dd)
print()
print(add(28948022309329048855892746252171976963209391069768726095651290785379540374961, hs))
print(add(86844066927987146567678238756515930889628173209306178286953872356138621122130, hs))
print(add(1376, hs))
print(add(57896044618658097711785492504343953926418782139537452191302581570759080748545, hs))
'''
