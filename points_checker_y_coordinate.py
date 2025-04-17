starting_y = 0x1
p = 0xfffffffffffffffffffffffffffffffffffffffffffffffffffffffefffffc2f
beta = 0x7ae96a2b657c07106e64479eac3434e99cf0497512f58995c1396c28719501ee

def oncurve(x,y): # Checks if point satifies x^3 +7 = y^2 , mod P
  x = (x*x*x+7) % p
  y = (y*y) % p
  return x==y

iterations = 10

for _ in range(iterations):
    y = starting_y
    xcubed = (y*y - 7) % p
    x = pow(xcubed, (p + 2) * pow(9, p - 2, p) % p , p)
    #x = pow(xcubed, (p + 2) // 9 , p)
    plist = list()
    x1 = str(hex(x))[2:].zfill(64)
    plist.append(x1)
    x2 = str(hex((x * beta % p)))[2:].zfill(64)
    plist.append(x2)
    x3 = str(hex((x * beta * beta % p)))[2:].zfill(64)
    plist.append(x3)
    if (y**2) % p == (int(x1,16)**3 + 7) % p:
        print(f"Secp256k1 True Y Coordinate: {hex(y)[2:].zfill(64)} [{y}]")
        print(f'{x1}:{hex(y)[2:].zfill(64)}')
        print( oncurve( int(x1, 16),int(hex(y)[2:].zfill(64), 16)) ) 
        print(f'{x2}:{hex(y)[2:].zfill(64)}')
        print( oncurve( int(x2, 16),int(hex(y)[2:].zfill(64), 16)) )
        print(f'{x3}:{hex(y)[2:].zfill(64)}')
        print( oncurve( int(x3, 16),int(hex(y)[2:].zfill(64), 16)) )
        print('---------------------------------------------------------------------------------------------------------------------------------')
    starting_y += 1
