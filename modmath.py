N = 115792089237316195423570985008687907852837564279074904382605163141518161494337
lambda1 = 37718080363155996902926221483475020450927657555482586988616620542887997980018
lambda2 = 78074008874160198520644763525212887401909906723592317393988542598630163514318
last = 115792089237316195423570985008687907852837564279074904382605163141518161494336
m1 = 57896044618658097711785492504343953926418782139537452191302581570759080747168
m2 = 57896044618658097711785492504343953926418782139537452191302581570759080747169

def modinv(a, n): #Extended Euclidean Algorithm/"division" in elliptic curves
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

def multiplicative_inverse(x):
    return pow(x, N - 2, N)
    
def additive_inverse(a):
    return N - a
    
def add(a, b): #addition
    return (a + b) % N

def sub(a, b): #subtraction
    return (a + additive_inverse(b)) % N

def mul(a, b): #multiplication
    return (a * b) % N
    
def div(a, b): #division
    return (a * multiplicative_inverse(b)) % N
