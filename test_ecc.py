P = 115792089237316195423570985008687907853269984665640564039457584007908834671663
N = 115792089237316195423570985008687907852837564279074904382605163141518161494337

Gx = 55066263022277343669578718895168534326250603453777594175500187360389116729240
Gy = 32670510020758816978083085130507043184471273380659243275938904335757337482424
G = (Gx,Gy)

last = (55066263022277343669578718895168534326250603453777594175500187360389116729240,83121579216557378445487899878180864668798711284981320763518679672151497189239)
m1 = (86918276961810349294276103416548851884759982251107,28597260016173315074988046521176122746119865902901063272803125467328307387891)
m2 = (86918276961810349294276103416548851884759982251107,87194829221142880348582938487511785107150118762739500766654458540580527283772)

def mod(x,m): #modulo operation based on addition and subtraction x(number) m(modulus) for arbitrarily large integers
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
        
def add(a,b):
    LamAdd = ((b[1]-a[1]) * modinv(b[0]-a[0],P))
    LamAdd = LamAdd % P
    x = (LamAdd*LamAdd-a[0]-b[0])
    x = x % P    
    y = (LamAdd*(a[0]-x)-a[1])
    y = y % P
    return (x,y)

def add_full(a,b):
    if not oncurve(a) and a != (0,0):
        raise TypeError('Point Addition Error: Point a:{} is not on the curve'.format(a))
    if not oncurve(b) and b != (0,0):
        raise TypeError('Point Addition Error: Point b:{} is not on the curve'.format(b))
    if a[0]==0 and a[1]==0:
       return b
    if b[0]==0 and b[1]==0:
        return a
    if a[0]==b[0] and a[1] != b[1]:
        return (0,0)
    elif a[0]==b[0] and a[1]==b[1]:
        return double(a)
    else:
        LamAdd = ((b[1]-a[1]) * modinv(b[0]-a[0],P)) % P
        x = (LamAdd*LamAdd-a[0]-b[0]) % P
        y = (LamAdd*(a[0]-x)-a[1]) % P
        return (x,y)

def sub(a,b):
    return add(a,inv(b))

def mult(GenPoint,ScalarHex):
    ScalarBin = str(bin(ScalarHex))[2:]
    Q=GenPoint
    for i in range (1, len(ScalarBin)):
        Q=double(Q)
        if ScalarBin[i] == "1": 
            Q=add(Q,GenPoint)
    return (Q)

def div(a,b): # Point multiplication by multiplicative inverse, returns a point such that mult( div(a,b) , b ) == a
    return mult(a,modinv(b,N))

def half(a): # Inverse of point doubling, same as div(a,2)
    return mult(a,57896044618658097711785492504343953926418782139537452191302581570759080747169)

def set_point(point):
    x = int(point[2:66], 16)
    y = int(point[66:], 16)
    return (x,y)

G2  = set_point('04c6047f9441ed7d6d3045406e95c07cd85c778e4b8cef3ca7abac09b95c709ee51ae168fea63dc339a3c58419466ceaeef7f632653266d0e1236431a950cfe52a')
G16 = set_point('04e60fce93b59e9ec53011aabc21c23e97b2a31369b87a5ae9c44ee89e2a6dec0af7e3507399e595929db99f34f57937101296891e44d23f0be1f32cce69616821')
print(mult(G2,16))
print(mult(G16,2))
