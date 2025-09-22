import time
import random
import gmpy2
import secp256k1

modulo = 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEFFFFFC2F
order  = 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEBAAEDCE6AF48A03BBFD25E8CD0364141


G = secp256k1.scalar_multiplication(1)
Z = secp256k1.scalar_multiplication(0)

def comparator():
    A, Ak, B, Bk = [], [], [], []
    with open('tame.txt') as f:
        for line in f:
            L = line.split()
            a = int(L[0],16)
            b = int(L[1])
            A.append(a)
            Ak.append(b)
    with open('wild.txt') as f:
        for line in f: 
            L = line.split()
            a = int(L[0],16)
            b = int(L[1])
            B.append(a)
            Bk.append(b)
    result = list(set(A) & set(B))
    if len(result) > 0: 
        sol_kt = A.index(result[0])
        sol_kw = B.index(result[0])
        print('total time: %.2f sec' % (time.time()-starttime))
        d = Ak[sol_kt] - Bk[sol_kw]
        print('SOLVED:', d)
        file = open("results.txt",'a')
        file.write(('%d'%(Ak[sol_kt] - Bk[sol_kw])) + "\n")
        file.write("---------------\n")
        file.close()
        return True
    else:
        return False

def check(P, Pindex, DP_rarity, file2save):
    if int(secp256k1.point_to_cpub(P)[2:], 16) % (DP_rarity) == 0:
        file = open(file2save,'a')
        file.write(('%064x %d'%(int(secp256k1.point_to_cpub(P)[2:], 16), Pindex)) + "\n")
        file.close()
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
    hop_modulo = ((problem-1) // 2) + kangoo_power 
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
    oldtime = time.time()
    starttime = oldtime
    Hops, Hops_old = 0, 0
    t0 = time.time()
    oldtime = time.time()
    starttime = oldtime
    while (1):
        for k in range(Nt):
            Hops += 1
            pw = int(secp256k1.point_to_cpub(T[k])[2:], 16) % hop_modulo
            dt[k] = 1 << pw
            solved = check(T[k], t[k], DP_rarity, "tame.txt")
            if solved: break
            t[k] += dt[k]
            T[k] = secp256k1.add_points(P_table[pw], T[k])
        if solved: break            
        for k in range(Nw):
            Hops += 1
            pw = int(secp256k1.point_to_cpub(W[k])[2:], 16) % hop_modulo
            dw[k] = 1 << pw
            solved = check(W[k], w[k], DP_rarity, "wild.txt")
            if solved: break
            w[k] += dw[k]
            W[k] = secp256k1.add_points(P_table[pw], W[k])
        if solved: break
        t1 = time.time()
        if (t1-t0) > 5:
            print('%.3f h/s'%((Hops-Hops_old)/(t1-t0)))
            t0 = t1
            Hops_old = Hops
    hops_list.append(Hops)        
    print(f'Hops: {Hops}')       
    return('sol. time: %.2f sec' % (time.time()-starttime))   

problems = [\
    ('029d8c5d35231d75eb87fd2c5f05f65281ed9573dc41853288c62ee94eb2590b7a',16),\
    ('036ea839d22847ee1dce3bfc5b11f6cf785b0682db58c35b63d1342eb221c3490c',24),\
    ('0209c58240e50e3ba3f833c82655e8725c037a2294e14cf5d73a5df8d56159de69',32),\
    ('03a2efa402fd5268400c77c20e574ba86409ededee7c4020e4b9f0edbee53de0d4',40),\
    #('025e466e97ed0e7910d3d90ceb0332df48ddf67d456b9e7303b50a3d89de357336',44),\#puzzle
    ('03c068310e31abda589343561e60ec3d30899e0dc9e704ad203bf45ce50c1d2ab1',44),\
    ('026ecabd2d22fdb737be21975ce9a694e108eb94f3649c586cc7461c8abf5da71a',45),\
    ('03f46f41027bbf44fafd6b059091b900dad41e6845b2241dc3254c7cdd3c5a16c6',50),\
    ('0230210c23b1a047bc9bdbb13448e67deddc108946de6de639bcc75d47c0216b1b',65),\
    ('03bcf7ce887ffca5e62c9cabbdb7ffa71dc183c52c04ff4ee5ee82e0c55c39d77b',105)]

problem = 40
for elem in problems:
    search_pub, n = elem
    if problem == n: break
kangoo_power = 3
#kangoo_power = 5
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
    open("tame.txt",'w').close()
    open("wild.txt",'w').close()
    kangaroo_search()
