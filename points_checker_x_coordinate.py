starting_x = 0x1
p = 0xfffffffffffffffffffffffffffffffffffffffffffffffffffffffefffffc2f
beta  = 0x7ae96a2b657c07106e64479eac3434e99cf0497512f58995c1396c28719501ee
beta2 = 0x851695d49a83f8ef919bb86153cbcb16630fb68aed0a766a3ec693d68e6afa40

def oncurve(x,y): # Checks if point satifies x^3 +7 = y^2 , mod P
  x = (x*x*x+7) % p
  y = (y*y) % p
  return x==y
  
iterations = 10

for _ in range(iterations):
    x = starting_x
    ysquared = ((x*x*x+7) % p)      
    y1 = pow(ysquared, (p+1)//4, p)
    y2 = (y1 * -1) % p
    if (y1**2) % p == (x**3 + 7) % p:
        print(f"Secp256k1 True X Coordinate: {hex(x)[2:].zfill(64)} [{x}]")
        print(f'{hex(x)[2:].zfill(64)}:{hex(y1)[2:].zfill(64)}')
        print( oncurve( x,int(hex(y1)[2:].zfill(64), 16)) ) 
        print(f'{hex(x)[2:].zfill(64)}:{hex(y2)[2:].zfill(64)}')
        print( oncurve( x,int(hex(y2)[2:].zfill(64), 16)) )
        print(hex((x*beta) % p)[2:].zfill(64))
        print(hex((x*beta2) % p)[2:].zfill(64))
        print('---------------------------------------------------------------------------------------------------------------------------------')
    starting_x += 1


