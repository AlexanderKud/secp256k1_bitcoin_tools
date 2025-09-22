from datetime import datetime
import secp256k1

G = secp256k1.scalar_multiplication(1)
bits_down = 2
point = '049dea9d0518a080af709a801be993d91ef96fe0dd17cfcb0b3b29d4b78bb2aa4913d463b7571753495f1be66d695506ad9b79e2fdecbf8703d3faa7c68ebc4e45'
group = list()
group.append(point)
print(f'[{datetime.now().strftime("%H:%M:%S")}] Starting out')
for i in range(bits_down):
    final_group = list()
    for p in group:
        point = secp256k1.publickey_to_point(p)
        final_group.append(secp256k1.point_multiplication(point, 57896044618658097711785492504343953926418782139537452191302581570759080747169).hex())
        point = secp256k1.publickey_to_point(secp256k1.subtract_points_safe(point, G).hex())        
        final_group.append(secp256k1.point_multiplication(point, 57896044618658097711785492504343953926418782139537452191302581570759080747169).hex())
    group = final_group
print(f'Number of points: {len(final_group)}')
#for p in final_group:
    #with open("points.txt", "a", encoding="utf-8") as f:
        #f.write(f"{p} \n")
for p in final_group:
    print(p)
print(f'[{datetime.now().strftime("%H:%M:%S")}] Finished')
