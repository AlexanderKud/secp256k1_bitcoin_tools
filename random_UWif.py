import hashlib
import base58       # python3 -m pip install base58
import binascii
from bit import Key # python3 -m pip install bit
import random
import string_utils # python3 -m pip install string-utils

#123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz - Base58
#5H 5J 5K
alphabet = '123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz'
iterations = 10
for _ in range(iterations):
    string_utils.shuffle(alphabet)
    start = '5KFunnyShit'
    iterator = 51 - len(start)
    for i in range(iterator):
        start += random.choice(alphabet)
    wif = start    
    first_encode = base58.b58decode(wif)
    private_key_full = binascii.hexlify(first_encode)
    private_key = private_key_full[2:-8]
    private_key_hex = private_key.decode("utf-8")
    print(f'Private key : {private_key_hex}')
    keyU = Key.from_hex(private_key_hex)
    keyU._public_key = keyU._pk.public_key.format(compressed=False)
    print(f'WIF key     : {keyU.to_wif()}')
    print(f'Address     : {keyU.address}')
    print(' ')
    
