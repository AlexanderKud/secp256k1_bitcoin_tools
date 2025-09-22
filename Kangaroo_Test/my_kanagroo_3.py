import time
import random
import secp256k1
import sys

tame_x = []
tame_pindex = []
wild_x = []
wild_pindex = []
wild_x_inv = []
wild_pindex_inv = []

def comparator():
    result1 = list(set(tame_x) & set(wild_x))
    result2 = list(set(tame_x) & set(wild_x_inv))
    if len(result1) > 0:
        #print(f'Result:{result1}')
        tame_pind = tame_pindex[tame_x.index(result1[0])]
        wild_pind = wild_pindex[wild_x.index(result1[0])]
        print(f'\nKey[w1] -> {tame_pind - wild_pind}')
        print('Time    -> %.2f sec' % (time.time()-starttime))
        file = open("results.txt",'a')
        file.write(('%s' % str(tame_pind - wild_pind)) + "\n")
        file.write("---------------\n")
        file.close()
        return True
    elif len(result2) > 0:
        #print(f'Result:{result2}')
        tame_pind = tame_pindex[tame_x.index(result2[0])]
        wild_pind = wild_pindex_inv[wild_x_inv.index(result2[0])]
        print(f'\nKey[w2] -> {inverse_find - (tame_pind - wild_pind)}')
        print('Time    -> %.2f sec' % (time.time()-starttime))
        file = open("results.txt",'a')
        file.write(('%s' % str(inverse_find - (tame_pind - wild_pind))) + "\n")
        file.write("---------------\n")
        file.close()
        return True
    else:
        return False

def check(P, Pindex, DP_rarity, set_type):
    if int(secp256k1.point_to_cpub(P)[2:], 16) % (DP_rarity) == 0:
        if set_type == 'tame':
            tame_x.append(secp256k1.point_to_cpub(P)[2:].zfill(64))
            tame_pindex.append(Pindex)
        if set_type == 'wild':
            wild_x.append(secp256k1.point_to_cpub(P)[2:].zfill(64))
            wild_pindex.append(Pindex)
        if set_type == 'wild_inv':
            wild_x_inv.append(secp256k1.point_to_cpub(P)[2:].zfill(64))
            wild_pindex_inv.append(Pindex)
        return comparator()
    else:
        return False
    
P_table = []
pk = 1
for k in range(255): 
    P_table.append(secp256k1.scalar_multiplication(pk)) 
    pk *= 2    
print('P_table generated')    

def kangaroo_search():
    global solved
    DP_rarity = 1 << ((problem -  2*kangoo_power)//2 - 2)
    print(f'DP_rarity: {DP_rarity}')
    hop_modulo = ((problem-1) // 2) + kangoo_power
    print(f'Hop_modulo: {hop_modulo}')
    T, t, dt = [], [], []
    W, w, dw = [], [], []
    Wi, wi, dwi = [], [], []
    for k in range(herd_size):
        #t.append((3 << (problem - 2)) + random.randint(1, (1 << (problem - 1))))#-(1 << (problem - 2)) )
        t.append((1 << (problem - 1)) + random.randint(1, (1 << (problem - 1))))#-(1 << (problem - 2)) )
        T.append(secp256k1.scalar_multiplication(t[k]))
        dt.append(0)
    for k in range(herd_size):
        #w.append(random.randint(1, (1 << (problem - 1))))
        w.append(random.randint(1, (1 << (problem - 2))))
        W.append(secp256k1.add_points(W0, secp256k1.scalar_multiplication(w[k])))
        dw.append(0)
    for k in range(herd_size):
        #wi.append(random.randint(1, (1 << (problem - 1))))
        wi.append(random.randint(1, (1 << (problem - 2))))
        Wi.append(secp256k1.add_points(W1, secp256k1.scalar_multiplication(wi[k])))
        dwi.append(0)
    print('tame and wild herds are ready to go')
    Hops, Hops_old = 0, 0
    t0 = time.time()
    starttime = time.time()
    while (1):
        for k in range(herd_size):
            Hops += 1
            pw = int(secp256k1.point_to_cpub(T[k])[2:], 16) % hop_modulo
            dt[k] = 1 << pw
            solved = check(T[k], t[k], DP_rarity, "tame")
            if solved: break
            t[k] += dt[k]
            T[k] = secp256k1.add_points(P_table[pw], T[k])
        if solved: break            
        for k in range(herd_size):
            Hops += 1
            pw = int(secp256k1.point_to_cpub(W[k])[2:], 16) % hop_modulo
            dw[k] = 1 << pw
            solved = check(W[k], w[k], DP_rarity, "wild")
            if solved: break
            w[k] += dw[k]
            W[k] = secp256k1.add_points(P_table[pw], W[k])
        if solved: break
        for k in range(herd_size):
            Hops += 1
            pw = int(secp256k1.point_to_cpub(Wi[k])[2:], 16) % hop_modulo
            dwi[k] = 1 << pw
            solved = check(Wi[k], wi[k], DP_rarity, "wild_inv")
            if solved: break
            wi[k] += dwi[k]
            Wi[k] = secp256k1.add_points(P_table[pw], Wi[k])
        if solved: break
        t1 = time.time()
        if (t1-t0) > 3:
            sys.stdout.write('\r%.3f h/s  '%((Hops-Hops_old)/(t1-t0)))
            t0 = t1
            Hops_old = Hops
    hops_list.append(Hops)        
    print(f'Hops    -> {Hops}')        

problems = [\
    ('029d8c5d35231d75eb87fd2c5f05f65281ed9573dc41853288c62ee94eb2590b7a',16),\
    ('036ea839d22847ee1dce3bfc5b11f6cf785b0682db58c35b63d1342eb221c3490c',24),\
    ('0209c58240e50e3ba3f833c82655e8725c037a2294e14cf5d73a5df8d56159de69',32),\
    ('02f6a8148a62320e149cb15c544fe8a25ab483a0095d2280d03b8a00a7feada13d',35),\
    ('03c060e1e3771cbeccb38e119c2414702f3f5181a89652538851d2e3886bdd70c6',38),\
    ('03a2efa402fd5268400c77c20e574ba86409ededee7c4020e4b9f0edbee53de0d4',40),\
    ('03b357e68437da273dcf995a474a524439faad86fc9effc300183f714b0903468b',41),\
    ('03eec88385be9da803a0d6579798d977a5d0c7f80917dab49cb73c9e3927142cb6',42),\
    ('025e466e97ed0e7910d3d90ceb0332df48ddf67d456b9e7303b50a3d89de357336',44),\
    ('026ecabd2d22fdb737be21975ce9a694e108eb94f3649c586cc7461c8abf5da71a',45),\
    ('03fd5487722d2576cb6d7081426b66a3e2986c1ce8358d479063fb5f2bb6dd5849',46),\
    ('023a12bd3caf0b0f77bf4eea8e7a40dbe27932bf80b19ac72f5f5a64925a594196',47),\
    ('03f46f41027bbf44fafd6b059091b900dad41e6845b2241dc3254c7cdd3c5a16c6',50),\
    ('0374c33bd548ef02667d61341892134fcf216640bc2201ae61928cd0874f6314a7',52),\
    ('020faaf5f3afe58300a335874c80681cf66933e2a7aeb28387c0d28bb048bc6349',53),\
    ('034af4b81f8c450c2c870ce1df184aff1297e5fcd54944d98d81e1a545ffb22596',54),\
    ('0385a30d8413af4f8f9e6312400f2d194fe14f02e719b24c3f83bf1fd233a8f963',55),\
    ('0230210c23b1a047bc9bdbb13448e67deddc108946de6de639bcc75d47c0216b1b',65),\
    ('03bcf7ce887ffca5e62c9cabbdb7ffa71dc183c52c04ff4ee5ee82e0c55c39d77b',105),\
    ('02145d2611c823a396ef6712ce0f712f09b9b4f3135e3e0aa3230fb9b6d08d1e16',135)]

problem = 44
for elem in problems:
    search_pub, n = elem
    if problem == n: break
    
kangoo_power = 5
herd_size = 2**kangoo_power

start = 2**(problem-1)
end   = 2**problem
inverse_find = start + end
start_point = P_table[problem - 1]
end_point   = P_table[problem]
inverse_find_point = secp256k1.add_points(start_point, end_point)

W0 = secp256k1.publickey_to_point(search_pub)
W1 = secp256k1.subtract_points(inverse_find_point, W0)

starttime = time.time()
search_range = 2**(problem-1)
Hops = 0
random.seed()
hops_list = []
N_tests = 1

for k in range(N_tests):
    solved = False
    kangaroo_search()

