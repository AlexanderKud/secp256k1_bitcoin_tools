from secp256k1 import *

G  = scalar_multiplication(1)
curve_2G = scalar_multiplication(2)
curve_3G = scalar_multiplication(3)

def parse_pubkey(pubkey):
    if pubkey.startswith('04'):
        x = pubkey[2:66]
        print(f'X: {x}')
        y = pubkey[66:]
        print(f'Y: {y}')
        Q = [int(x, 16), int(y, 16)]
        return Q
    p = 0xfffffffffffffffffffffffffffffffffffffffffffffffffffffffefffffc2f
    if pubkey.startswith('02'):
        print(f'X: {pubkey[2:66]}')
        x = int(pubkey[2:66], 16)
        ysquared = ((x*x*x+7) % p)      
        y1 = pow(ysquared, (p+1)//4, p)
        y2 = p - y1
        if int(str(y1)[-1]) % 2 == 0:
            print(f'Y: {hex(y1)[2:]}')
            Q = [x, y1]
            return Q
        else:
            print(f'Y: {hex(y2)[2:]}')
            Q = [x, y2]
            return Q
    if pubkey.startswith('03'):
        print(f'X: {pubkey[2:66]}')
        x = int(pubkey[2:66], 16)
        ysquared = ((x*x*x+7) % p)      
        y1 = pow(ysquared, (p+1)//4, p)
        y2 = p - y1
        if int(str(y1)[-1]) % 2 == 0:
            print(f'Y: {hex(y2)[2:]}')
            Q = [x, y2]
            return Q
        else:
            print(f'Y: {hex(y1)[2:]}')
            Q = [x, y1]
            return Q
    
def is_even(point):  
    while True:
        if point == curve_2G:
            return True
        if point == curve_3G:
            return False
        point = point_subtraction(point, curve_2G)
    
     
def get_private_key(pubkey):
    point = parse_pubkey(pubkey)
    str_bin = ''
    if point == G:
        str_bin = '1'
        return hex(int(str_bin, 2))[2:].zfill(64)
    else:
        while point != G:
            if is_even(point):
                point = point_division(point, 2)
                str_bin += '0'
            else:
                point = point_subtraction(point, G)
                point = point_division(point, 2)
                str_bin += '1'
    return hex(int('1' + str_bin[::-1], 2))[2:].zfill(64)

#public_key = '04e60fce93b59e9ec53011aabc21c23e97b2a31369b87a5ae9c44ee89e2a6dec0af7e3507399e595929db99f34f57937101296891e44d23f0be1f32cce69616821'
public_key = '0412301309e0414fec1e8d12317490f03fcad401153fd71c7bb79de0373a4644272720501d39866f4362516379bf0c95d83e74c33ed256d76b7ac312e95cedca76'
print(f'Getting the private key of {public_key}')
print(f'Private key: {get_private_key(public_key)}')
