import hashlib
import base58       # python3 -m pip install base58
import binascii
from bit import Key # python3 -m pip install bit
import random
import string_utils # python3 -m pip install string-utils

#123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz - Base58
#Kw Kx Ky Kz L1 L2 L3 L4 L5
alphabet = '123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz'
iterations = 100
for _ in range(iterations):
    string_utils.shuffle(alphabet)
    start = 'L5'
    iterator = 52 - len(start)
    for i in range(iterator):
        start += random.choice(alphabet)    
    wif = start
    first_encode = base58.b58decode(wif)
    private_key_full = binascii.hexlify(first_encode)
    private_key = private_key_full[2:-8]
    private_key_hex = private_key.decode("utf-8")[0:64]
    print(f'Private key : {private_key_hex}')
    keyU = Key.from_hex(private_key_hex[0:64])
    print(f"WIF key     : {keyU.to_wif()}")
    print(f'Address     : {keyU.address}')
    print(' ')

