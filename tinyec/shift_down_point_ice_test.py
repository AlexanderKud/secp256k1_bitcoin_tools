from datetime import datetime
import secp256k1 as ice

G = ice.scalar_multiplication(1)
down_range = 3
scalar = 664613997892457936451903530140173312 #649037107316853453566312041152512
point = ice.scalar_multiplication(scalar).hex()
numb = 0
for i in range(down_range):
    if scalar % 2 == 0: 
        numb = scalar // 2
    else:
        scalar = scalar - 1
        numb = scalar // 2
    scalar = numb
group = list()
group.append(point)

time = datetime.now().strftime("%H:%M:%S")
print(f"[{time}] Starting out")
for i in range(down_range):
    final_group = list()
    for p in group:
        point = bytes.fromhex(p)
        final_group.append(ice.point_multiplication(57896044618658097711785492504343953926418782139537452191302581570759080747169, point).hex())
        point = bytes.fromhex(ice.point_subtraction(point,G).hex())       
        final_group.append(ice.point_multiplication(57896044618658097711785492504343953926418782139537452191302581570759080747169, point).hex())
    group = final_group

#for p in final_group:
    #print(p)
index = 1
for p in final_group:
    if p == ice.scalar_multiplication(scalar).hex():
        print(f'Found: [{index}] {scalar} {p}')
    index += 1

print(f'Number of points: {len(final_group)}')
time = datetime.now().strftime("%H:%M:%S")
print(f"[{time}] Finished")
