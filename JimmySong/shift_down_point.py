from ecc import S256Point, G, N
from datetime import datetime

px = 0xceb6cbbcdbdf5ef7150682150f4ce2c6f4807b349827dcdbdd1f2efa885a2630
py = 0x2b195386bea3f5f002dc033b92cfc2c9e71b586302b09cfe535e1ff290b1b5ac
point = S256Point(px, py)
group = list()
group.append(point)
final_group = list()
dip = 4
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
    with open("points.txt", "a", encoding="utf-8") as f:
        f.write(f"04{p.x}{p.y} \n")
now = datetime.now()
time = now.strftime("%H:%M:%S")
print(f"[{time}] Finished")

