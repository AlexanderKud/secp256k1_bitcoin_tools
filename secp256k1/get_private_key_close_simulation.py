from secp256k1 import *
from datetime import datetime
import time
import random

G  = scalar_multiplication(1)

def generate_parity_list(scalar):
    parity_list = list()
    while scalar > 1:
        if scalar % 2 == 0:
            scalar //= 2
            parity_list.append("even")
        else:
            scalar -= 1
            scalar //= 2
            parity_list.append("odd")
    return parity_list

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
    
def get_private_key(pubkey, parity_list):
    point = parse_pubkey(pubkey)
    str_bin = ''
    parity_list_index = 0
    if point == G:
        str_bin = '1'
        return hex(int(str_bin, 2))[2:].zfill(64)
    else:
        while point != G:
            if parity_list[parity_list_index] == 'even':
                point = point_division(point, 2)
                str_bin += '0'
                parity_list_index += 1
            else:
                point = point_subtraction(point, G)
                point = point_division(point, 2)
                str_bin += '1'
                parity_list_index += 1
    return hex(int('1' + str_bin[::-1], 2))[2:].zfill(64)

print(f'[{datetime.now().strftime("%H:%M:%S")}] Start')
#scalar = 29876543297543324336679899823453421323445
scalar = random.randrange(1, curve.n)
print(f'Random: {scalar}')
print(f'Random: {hex(scalar)}')
parity_list = generate_parity_list(scalar)
public_key = point_to_upub(scalar_multiplication(scalar))
print(f'Getting the private key of {public_key}')
print(f'Private key: {get_private_key(public_key, parity_list)}')
print(f'[{datetime.now().strftime("%H:%M:%S")}] Finish')
