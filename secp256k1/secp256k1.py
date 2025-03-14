import gmpy2

class Curve:

    def __init__(self):
        self.a = 0
        self.b = 7
        self.p = 2**256-2**32-2**9-2**8-2**7-2**6-2**4-1
        gx = 0x79BE667EF9DCBBAC55A06295CE870B07029BFCDB2DCE28D959F2815B16F81798
        gy = 0x483ada7726a3c4655da4fbfc0e1108a8fd17b448a68554199c47d08ffb10d4b8
        self.g = [gx,gy]
        self.n = 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEBAAEDCE6AF48A03BBFD25E8CD0364141

    def valid(self, point):
        xP = point[0]
        if xP == None:
            return False
        yP = point[1]
        return yP**2 % self.p == (pow(xP, 3, self.p) + self.a*xP + self.b) % self.p

    def uncompressed(self, P):
        byte = '04'
        return str(byte + hex(int(P[0])).lstrip('0x').zfill(64) + hex(int(P[1])).lstrip('0x').zfill(64))
        
    def compressed(self, P):
        byte = "02"
        if P[1] % 2:
            byte = "03"
        return str(byte + hex(int(P[0])).lstrip('0x').zfill(64))

    def inv(self, point):
        xP = point[0]
        yP = point[1]
        R = [xP,-yP % self.p]
        return R

    def add(self, P, Q):
        if P == Q: # P+P=2P
            return self.dbl(P)        
        if P[0] == None: # P+0=P
            return Q
        if Q[0] == None:
            return P
        if Q == self.inv(P): # P+-P=0
            return [None,None]
        xP = P[0]
        yP = P[1]
        xQ = Q[0]
        yQ = Q[1]
        s = (yP - yQ) * gmpy2.invert(xP - xQ, self.p) % self.p
        xR = (pow(s,2,self.p) - xP -xQ) % self.p
        yR = (-yP + s*(xP-xR)) % self.p
        R = [xR,yR]
        return R

    def dbl(self,P):        
        if P[0] == None: # 2*0=0
            return P
        if P[1] == 0: # yP==0
            return [None,None]
        xP = P[0]
        yP = P[1]
        s = (3*pow(xP,2,self.p)+self.a) * gmpy2.invert(2*yP, self.p) % self.p
        xR = (pow(s,2,self.p) - 2*xP) % self.p
        yR = (-yP + s*(xP-xR)) % self.p
        R = [xR,yR]
        return R

    def mul(self, P, k):
        if P[0] == None: # x0=0
            return P
        N = P
        R = [None,None]
        while k:
            bit = k % 2
            k >>= 1
            if bit:
                R = self.add(R,N)
            N = self.dbl(N)
        return R

curve = Curve()

def scalar_multiplication(k):
    return curve.mul(curve.g, k)
    
def point_multiplication(P, k):
    return curve.mul(P, k)
    
def point_division(P, k):
    return curve.mul(P, gmpy2.invert(gmpy2.mpz(k), curve.n))
    
def point_addition(P, Q):
    return curve.add(P, Q)

def point_subtraction(P, Q):
    return curve.add(P, curve.inv(Q))
    
def point_negation(P):
    return curve.inv(P)
    
def point_doubling(P):
    return curve.add(P, P)
    
def point_halving(P):
    return curve.mul(P, gmpy2.invert(gmpy2.mpz(2), curve.n))
    
def point_to_upub(P):
    return curve.uncompressed(P)

def point_to_cpub(P):
    return curve.compressed(P)
    
def on_curve(P):
    return curve.valid(P)
