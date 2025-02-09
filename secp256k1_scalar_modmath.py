n = 115792089237316195423570985008687907852837564279074904382605163141518161494337
lambda1 = 37718080363155996902926221483475020450927657555482586988616620542887997980018
lambda2 = 78074008874160198520644763525212887401909906723592317393988542598630163514318
    
def multiplicative_inverse(x):
    return pow(x, n - 2, n)
    
def additive_inverse(a):
    return n - a
    
def add(a, b): #addition
    return (a + b) % n

def sub(a, b): #subtraction
    return (a + additive_inverse(b)) % n

def mul(a, b): #multiplication
    return (a * b) % n
    
def div(a, b): #division
    return (a * multiplicative_inverse(b)) % n

print(div(1, 2))
print(multiplicative_inverse(2))
