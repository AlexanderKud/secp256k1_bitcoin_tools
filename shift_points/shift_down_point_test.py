from datetime import datetime
import secp256k1

G = secp256k1.scalar_multiplication(1)
bits_down = 2
scalar = 1171823477249417952904755003699827898
point = secp256k1.scalar_multiplication(scalar).hex()
numb = 0
for i in range(bits_down):
    if scalar % 2 == 0: 
        numb = scalar // 2
    else:
        scalar = scalar - 1
        numb = scalar // 2
    scalar = numb
group = list()
group.append(point)
#final_group = list()
now = datetime.now()
time = now.strftime("%H:%M:%S")
print(f"[{time}] Starting out")
for i in range(bits_down):
    final_group = list()
    for p in group:
        point = bytes(bytearray.fromhex(p))
        final_group.append(secp256k1.point_multiplication(point, 57896044618658097711785492504343953926418782139537452191302581570759080747169).hex())
        point = bytes(bytearray.fromhex(secp256k1.subtract_points(point, G).hex()))        
        final_group.append(secp256k1.point_multiplication(point, 57896044618658097711785492504343953926418782139537452191302581570759080747169).hex())
    group = final_group
print(f'Number of points: {len(final_group)}')
for p in final_group:
    print(p)
index = 1
for p in final_group:
    if p == secp256k1.scalar_multiplication(scalar).hex():
        print(f'Found: [{index}] {scalar} {p}')
    index += 1
now = datetime.now()
time = now.strftime("%H:%M:%S")
print(f"[{time}] Finished")
