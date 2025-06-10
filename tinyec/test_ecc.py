P = 349
N = 313
G = (288, 15)

def mod(x, m): #modulo operation based on addition and subtraction x(number) m(modulus) for arbitrarily large integers
    if x > 0: #to check how many cut_down or add_up ops are necessary
        if x < m:
            return x
        else:
            res = x // m
            print(f'Positive[+] number of cut_down ops [{res}]')
            x = x - (res*m)
            return x
    else:
        res = abs(x) // m
        x = x + (res*m)
        if x == 0:
            print(f'Negative[-] number of add_up ops [{res}]')
        else:
            x += m
            print(f'Negative[-] number of add_up ops [{res+1}]')     
        return x
        
def oncurve(p):
  x = p[0]
  y = p[1]
  x = (x*x*x+7) % P
  y = (y*y) % P
  return x==y

def modinv(a, n):
    lm = 1
    hm = 0
    low = a%n
    high = n
    while low > 1:
        ratio = high//low
        nm = hm-lm*ratio
        new = high-low*ratio
        high = low
        low = new
        hm = lm
        lm = nm
    return lm % n

def inv(a):
    return (a[0],P-a[1])
    
    
def double(a):
    Lam = ((3*a[0]*a[0]) * modinv((2*a[1]),P))
    Lam = Lam % P
    x = (Lam*Lam-2*a[0])
    x = x % P
    y = (Lam*(a[0]-x)-a[1])
    y = y % P
    return (x,y)
        
def add(a, b):
    LamAdd = ((b[1]-a[1]) * modinv(b[0]-a[0],P))
    LamAdd = LamAdd % P
    x = (LamAdd*LamAdd-a[0]-b[0])
    x = x % P    
    y = (LamAdd*(a[0]-x)-a[1])
    y = y % P
    return (x,y)

def add_full(a, b):
    if a[0]==0 and a[1]==0:
       return b
    if b[0]==0 and b[1]==0:
        return a
    if a[0]==b[0] and a[1] != b[1]:
        return (0, 0)
    elif a[0]==b[0] and a[1]==b[1]:
        return double(a)
    else:
        LamAdd = ((b[1]-a[1]) * modinv(b[0]-a[0],P)) % P
        x = (LamAdd*LamAdd-a[0]-b[0]) % P
        y = (LamAdd*(a[0]-x)-a[1]) % P
        return (x,y)

def sub(a, b):
    return add(a,inv(b))

def mult(GenPoint,ScalarHex):
    ScalarBin = str(bin(ScalarHex))[2:]
    Q=GenPoint
    for i in range (1, len(ScalarBin)):
        Q=double(Q)
        if ScalarBin[i] == "1": 
            Q=add_full(Q,GenPoint)
    return (Q)

def div(a,b): # Point multiplication by multiplicative inverse, returns a point such that mult( div(a,b) , b ) == a
    return mult(a,modinv(b,N))

def half(a): # Inverse of point doubling, same as div(a,2)
    return mult(a, 57896044618658097711785492504343953926418782139537452191302581570759080747169)

def set_point(point):
    x = int(point[2:66], 16)
    y = int(point[66:], 16)
    return (x,y)

y_coords = set()
ys_map = {}
#for i in range(157, N):
for i in range(1, 157):
    point = mult(G, i)
    print(f'{i}: {point}')
    y_coords.add(point[1]) # getting all distinct y coordinates
    if point[1] in ys_map: # dictionary to show that every y coordinate has three times occurences
        val = ys_map.get(point[1])
        ys_map[point[1]] = val +1
    else:
        ys_map[point[1]] = 1

print(f"distinct y-coordinates: {len(y_coords)}")
print(y_coords)
sorted_tuple = sorted(ys_map.items(), key=lambda x: x[0])
print(sorted_tuple)
one = two = three = 0
for key in ys_map:
    if ys_map[key] == 1:
        one += 1
    elif ys_map[key] == 2:
        two += 1
    else:
        three += 1
print(f'1:{one} 2:{two} 3:{three}')
