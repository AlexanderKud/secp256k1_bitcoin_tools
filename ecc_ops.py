P = 115792089237316195423570985008687907853269984665640564039457584007908834671663
N = 115792089237316195423570985008687907852837564279074904382605163141518161494337

Gx = 55066263022277343669578718895168534326250603453777594175500187360389116729240
Gy = 32670510020758816978083085130507043184471273380659243275938904335757337482424
G = (Gx,Gy)

def oncurve(p):
  x = p[0]
  y = p[1]
  x = (x*x*x+7) % P
  y = (y*y) % P
  return x==y

def modinv(a,n):
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
    
def double(a):
    Lam = ((3*a[0]*a[0]) * modinv((2*a[1]),P)) % P
    x = (Lam*Lam-2*a[0]) % P
    y = (Lam*(a[0]-x)-a[1]) % P
    return (x,y)
    
def add(a,b):
    LamAdd = ((b[1]-a[1]) * modinv(b[0]-a[0],P)) % P
    x = (LamAdd*LamAdd-a[0]-b[0]) % P
    y = (LamAdd*(a[0]-x)-a[1]) % P
    return (x,y)

def add_full(a,b):
    if not oncurve(a) and a != (0,0):
        raise TypeError('Point Addition Error: Point a:{} is not on the curve'.format(a))
    if not oncurve(b) and b != (0,0):
        raise TypeError('Point Addition Error: Point b:{} is not on the curve'.format(b))
    if a[0]== 0 and a[1]==0:
       return b
    elif b[0]==0 and b[1]==0:
        return a
    if a[0]==b[0] and a[1] != b[1]:
        return "Inverse points added: " + str((0,0)) + str(a) + str(b)
    elif a[0]==b[0] and a[1]==b[1]:
        return double(a)
    else:
        LamAdd = ((b[1]-a[1]) * modinv(b[0]-a[0],P)) % P
        x = (LamAdd*LamAdd-a[0]-b[0]) % P
        y = (LamAdd*(a[0]-x)-a[1]) % P
        return (x,y)

def inv(a):
    return (a[0],P-a[1])

def sub(a,b):
    return add(a,inv(b))

def mult(GenPoint,ScalarHex):
    #if ScalarHex == 0 or ScalarHex >= N: raise Exception("Invalid Scalar/Private Key")
    ScalarBin = str(bin(ScalarHex))[2:]
    #print(f"Binary: {ScalarBin}")
    Q=GenPoint
    #print(f"Start Point: {Q}")
    for i in range (1, len(ScalarBin)):
        Q=double(Q)
        #print(f"Double: {Q}")
        if ScalarBin[i] == "1": 
            Q=add_full(Q,GenPoint) # print "ADD", Q[0]; print
           #print(f"Add: {Q}")
    #print(f"Return Value: {Q}")
    return (Q)

def div(a,b): # Point multiplication by multiplicative inverse, returns a point such that mult( div(a,b) , b ) == a
    return inv(mult(a,modinv(b,N)))

def half(a): # Inverse of point doubling, same as div(a,2)
    return mult(a,57896044618658097711785492504343953926418782139537452191302581570759080747169)

def set(a):
    return mult(G,a)

def xtoy(pk):
   x = pk
   y_sq = (pow(x, 3, P) + 7) % P
   y = pow(y_sq, (P + 1) // 4, P)
   return y

srt = 1
dip = 10
for i in range(srt,dip+1):
    p = mult(G,i)
    print(f'{p[0]}')
