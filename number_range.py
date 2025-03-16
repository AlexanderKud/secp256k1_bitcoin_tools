import math

S_table = []
pk = 1
for k in range(256): 
    S_table.append(pk) 
    pk *= 2

def get_range(number):
    start = end = 0
    for i in range(256):
        if S_table[i] > number:
            end = int(math.log2(S_table[i]))
            start = end - 1
            break
    print(f'Number({number}) is within 2^{start}...2^{end}')
    
number = 128898777
get_range(number)
