import secp256k1
import math
import time
import sys

start_range = 2**33
end_range   = 2**34
start_range_P = secp256k1.scalar_multiplication(start_range)
m = int(math.floor(math.sqrt(start_range)))
m_P = secp256k1.scalar_multiplication(m)
P = secp256k1.publickey_to_point('027cc6be21a94b322672a78a48f58781dddad31552d0725c97521516b7bb33aac2')

print('- Creating babyTable...')
points = []
for i in range(0, m + 1):
    Ps = secp256k1.scalar_multiplication(i)
    cpub = secp256k1.point_to_cpub(Ps)
    points.append(cpub[2:12])

print('- BSGS Search in progress')
S = secp256k1.subtract_points(P, start_range_P)
step = 0
b = 0
baby_table = tuple(points)
st = time.time()
while step < (end_range - start_range):
    cpub_slice = secp256k1.point_to_cpub(S)[2:12]
    if cpub_slice in baby_table:
        b = baby_table.index(cpub_slice)
        k = start_range + step + b
        print(f'- m={m} step={step} b={b}')
        print(f'- Key found: {k}')
        print("- Time Spent : {0:.2f} seconds".format(time.time()-st))
        sys.exit()
    else:
        S = secp256k1.subtract_points(S, m_P)
        step += m
        
print('- Key not found')
print("- Time Spent : {0:.2f} seconds".format(time.time()-st))
