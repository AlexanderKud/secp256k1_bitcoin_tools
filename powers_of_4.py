base = 4
exponent = 0
power_2_expo = 0
for i in range(129):
    num = base ** exponent
    print(f'{i}:[4^{exponent}] [2^{power_2_expo}] {num}')
    exponent += 1
    power_2_expo += 2
