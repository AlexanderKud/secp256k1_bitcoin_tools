from secp256k1 import *

G  = scalar_multiplication(1)
Q = [55066263022277343669578718895168534326250603453777594175500187360389116729240,
     32670510020758816978083085130507043184471273380659243275938904335757337482424]

#def is_even(point): ?
    #pass
     
def get_private_key(point):
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

print(f'Getting the private key')
print(f'Result: {get_private_key(Q)}')
