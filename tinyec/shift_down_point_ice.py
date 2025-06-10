from datetime import datetime
import secp256k1 as ice

G = ice.scalar_multiplication(1)
down_range = 8 
#point = '04ceb6cbbcdbdf5ef7150682150f4ce2c6f4807b349827dcdbdd1f2efa885a26302b195386bea3f5f002dc033b92cfc2c9e71b586302b09cfe535e1ff290b1b5ac' #120_puzzle_point
point = '0470d3293b23e80baf01bcfa00e03657a6b4e582c7cb8ce9f897d49dddbf3c04ba464542d108eb962e0229c9ef9c235a0c8a2c4b248e28d49a3612b3f59f53ef8d' #120_test_point
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

for p in final_group:
    with open("points_ice.txt", "a", encoding="utf-8") as f:
        f.write(f"{p} \n")

print(f'Number of points: {len(final_group)}')
time = datetime.now().strftime("%H:%M:%S")
print(f"[{time}] Finished")
