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
    
bits_down = 6
print(f'Bits down: {bits_down}')
scalar = 1288
print(scalar)

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
    print(f'{p}')
    index += 1
