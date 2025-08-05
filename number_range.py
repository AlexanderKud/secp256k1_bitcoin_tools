import math

S_table = []
pk = 1
for k in range(256): 
    S_table.append(pk) 
    pk *= 2

M_table = []
pk = 3
for k in range(255): 
    M_table.append(pk) 
    pk *= 2

def get_range(number):
    start = end = 0
    for i in range(256):
        if S_table[i] > number:
            end = int(math.log2(S_table[i]))
            start = end - 1
            break
    print(f'Number ({number}) is within 2^{start}...2^{end} bits')
    pos = ''
    if number > M_table[start - 1]:
        pos = 'higher range half'
    else:
        pos = 'lower range half'
    print(f'Number ({number}) is in the {pos}\n')
    print(f'Number ==========>: {number}\n')
    print(f'Range start  (dec): {2**start}')
    print(f'Range middle (dec): {M_table[start - 1]}')
    print(f'Range end    (dec): {2**(start + 1)}\n')
    print(f'Number ==========>: {hex(number)}\n')
    print(f'Range start  (hex): {hex(2**start)}')
    print(f'Range middle (hex): {hex(M_table[start - 1])}')
    print(f'Range end    (hex): {hex(2**(start + 1))}')
    
number = 1103873984953507439627945351144005829577
get_range(number)
