p = 349
x = 0
y = 0
counter = 1
for x in range(0,p):
    for y in range(0,p):
        if (y**2) % p == (x**3 + 7) % p:
            print(f"{counter}:({x},{y})")
            counter += 1
print(f'prime(p)={p} order(n)={counter}')
