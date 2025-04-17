import sympy
import gmpy2

print("Searching for prime p and n...")

for i in range(2, 1000):    
    p = i
    if sympy.isprime(p):
        x = 0
        y = 0
        n = 1
        for x in range(0, p):
            for y in range(0, p):
                if (y**2) % p == (x**3 + 7) % p:
                    n += 1
        #print(f'P: {p} N: {counter}')
        if sympy.isprime(n) and p > n:
            #if ((counter - 1) // 2) % 2 == 0:
            if (n - 1) % 6 == 0 and (n - 1) % 3 == 0:
                print(f'prime(p)={p} order(n)={n}')

print('Finished...')
