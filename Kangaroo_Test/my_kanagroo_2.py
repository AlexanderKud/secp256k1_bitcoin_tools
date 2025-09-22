import time
import random
import secp256k1
import sys

G = secp256k1.scalar_multiplication(1)
Z = secp256k1.scalar_multiplication(0)
tame_x = []
tame_pindex = []
wild_x = []
wild_pindex = []

def comparator():
    result = list(set(tame_x) & set(wild_x))
    if len(result) > 0:
        tame_pind = tame_pindex[tame_x.index(result[0])]
        wild_pind = wild_pindex[wild_x.index(result[0])]
        print(f'\nSolved -> {tame_pind - wild_pind}')
        print('Time   -> %.2f sec' % (time.time()-starttime))
        file = open("results.txt",'a')
        file.write(('%s' % str(tame_pind - wild_pind)) + "\n")
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
        return comparator()
    else:
        return False
    
P_table = []
pk = 1
for k in range(255): 
    P_table.append(secp256k1.scalar_multiplication(pk)) 
    pk *= 2    
print('P-table prepared')    

def kangaroo_search():
    global solved
    DP_rarity = 1 << ((problem -  2*kangoo_power)//2 - 2)
    print(f'DP_rarity: {DP_rarity}')
    hop_modulo = ((problem-1) // 2) + kangoo_power
    print(f'Hop_modulo: {hop_modulo}')
    T, t, dt = [], [], []
    W, w, dw = [], [], []
    for k in range(Nt):
        t.append((3 << (problem - 2)) + random.randint(1, (1 << (problem - 1))))#-(1 << (problem - 2)) )
        #t.append((1 << (problem - 1)) + random.randint(1, (1 << (problem - 1))))#-(1 << (problem - 2)) )
        T.append(secp256k1.scalar_multiplication(t[k]))
        dt.append(0)
    for k in range(Nw):
        w.append(random.randint(1, (1 << (problem - 1))))
        #w.append(random.randint(1, (1 << (problem - 2))))
        W.append(secp256k1.add_points(W0, secp256k1.scalar_multiplication(w[k])))
        dw.append(0)
    print('tame and wild herds are prepared')
    Hops, Hops_old = 0, 0
    t0 = time.time()
    oldtime = time.time()
    starttime = oldtime
    while (1):
        for k in range(Nt):
            Hops += 1
            pw = int(secp256k1.point_to_cpub(T[k])[2:], 16) % hop_modulo
            dt[k] = 1 << pw
            solved = check(T[k], t[k], DP_rarity, "tame")
            if solved: break
            t[k] += dt[k]
            T[k] = secp256k1.add_points(P_table[pw], T[k])
        if solved: break            
        for k in range(Nw):
            Hops += 1
            pw = int(secp256k1.point_to_cpub(W[k])[2:], 16) % hop_modulo
            dw[k] = 1 << pw
            solved = check(W[k], w[k], DP_rarity, "wild")
            if solved: break
            w[k] += dw[k]
            W[k] = secp256k1.add_points(P_table[pw], W[k])
        if solved: break
        t1 = time.time()
        if (t1-t0) > 5:
            #print('%.3f h/s'%((Hops-Hops_old)/(t1-t0)))
            sys.stdout.write('\r%.3f h/s  '%((Hops-Hops_old)/(t1-t0)))
            t0 = t1
            Hops_old = Hops
    hops_list.append(Hops)        
    print(f'Hops   -> {Hops}')        

problems = [\
    ('029d8c5d35231d75eb87fd2c5f05f65281ed9573dc41853288c62ee94eb2590b7a',16),\
    ('036ea839d22847ee1dce3bfc5b11f6cf785b0682db58c35b63d1342eb221c3490c',24),\
    ('0209c58240e50e3ba3f833c82655e8725c037a2294e14cf5d73a5df8d56159de69',32),\
    ('03a2efa402fd5268400c77c20e574ba86409ededee7c4020e4b9f0edbee53de0d4',40),\
    ('025e466e97ed0e7910d3d90ceb0332df48ddf67d456b9e7303b50a3d89de357336',44),\
    ('026ecabd2d22fdb737be21975ce9a694e108eb94f3649c586cc7461c8abf5da71a',45),\
    ('03fd5487722d2576cb6d7081426b66a3e2986c1ce8358d479063fb5f2bb6dd5849',46),\
    ('023a12bd3caf0b0f77bf4eea8e7a40dbe27932bf80b19ac72f5f5a64925a594196',47),\
    ('03f46f41027bbf44fafd6b059091b900dad41e6845b2241dc3254c7cdd3c5a16c6',50),\
    ('0374c33bd548ef02667d61341892134fcf216640bc2201ae61928cd0874f6314a7',52),\
    ('0230210c23b1a047bc9bdbb13448e67deddc108946de6de639bcc75d47c0216b1b',65),\
    ('03bcf7ce887ffca5e62c9cabbdb7ffa71dc183c52c04ff4ee5ee82e0c55c39d77b',105)]

problem = 40
for elem in problems:
    search_pub, n = elem
    if problem == n: break
    
kangoo_power = 6
Nt = Nw = 2**kangoo_power
W0 = secp256k1.publickey_to_point(search_pub)
starttime = oldtime = time.time()
search_range = 2**(problem-1)
Hops = 0
random.seed()
hops_list = []
N_tests = 1

for k in range(N_tests):
    solved = False
    kangaroo_search()
