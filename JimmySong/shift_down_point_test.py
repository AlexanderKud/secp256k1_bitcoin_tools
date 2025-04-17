from ecc import S256Point, G, N
from datetime import datetime

dip = 4
scalar = 1067469088711506941037814609297164223
point = scalar*G
numb = 0
for i in range(dip):
    if scalar % 2 == 0: 
        numb = scalar // 2
    else:
        scalar = scalar - 1
        numb = scalar // 2
    scalar = numb
group = list()
group.append(point)
final_group = list()
now = datetime.now()
time = now.strftime("%H:%M:%S")
print(f"[{time}] Starting out")
for i in range(dip):
    final_group = list()
    for p in group:
        point = p        
        final_group.append(point/2)
        final_group.append((point-G)/2)
    group = final_group
print(f'Final group length: {len(final_group)}')
for p in final_group:
    print(p)
index = 1
for p in final_group:
    if p == scalar*G:
        print(f'Found: [{index}] {scalar}:{p}')
    index += 1
now = datetime.now()
time = now.strftime("%H:%M:%S")
print(f"[{time}] Finished")
