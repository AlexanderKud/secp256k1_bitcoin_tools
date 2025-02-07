import secp256k1 as ice
import math
import time
import sys

start_range = 2**33
end_range   = 2**34
start_range_P = ice.scalar_multiplication(start_range)
m = int(math.floor(math.sqrt(start_range)))
m_P = ice.scalar_multiplication(m)
puzzle_pubkey = '027cc6be21a94b322672a78a48f58781dddad31552d0725c97521516b7bb33aac2'
P = ice.pub2upub(puzzle_pubkey)
slice_width = 6

print('- Creating babyTable...')
points = []
for i in range(0, m + 1):
    Ps = ice.scalar_multiplication(i)
    cpub = ice.point_to_cpub(Ps)
    points.append(cpub[2:slice_width])

print('- BSGS Search in progress')
S = ice.point_subtraction(P, start_range_P)
step = 0
b = 0
baby_table = tuple(points)
st = time.time()
while step < (end_range - start_range):
    cpub_slice = ice.point_to_cpub(S)[2:slice_width]
    if cpub_slice in baby_table:
        b = baby_table.index(cpub_slice)
        k = start_range + step + b
        if ice.point_to_cpub(ice.scalar_multiplication(k)) == puzzle_pubkey:
            print(f'- m={m} step={step} b={b}')
            print(f'- Key found: {k}')
            print("- Time Spent : {0:.2f} seconds".format(time.time()-st))
            sys.exit()
    
    S = ice.point_subtraction(S, m_P)
    step += m
        
print('- Key not found')
print("- Time Spent : {0:.2f} seconds".format(time.time()-st))
