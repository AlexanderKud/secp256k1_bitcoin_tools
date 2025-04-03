import bit
from bit.crypto import ripemd160_sha256
from bit.base32 import encode
from bit import Key
from bit.format import public_key_to_address, public_key_to_segwit_address

'''
public_key = bit.PrivateKey(
    'L4YRXnWPJx1QbXrf1c8cYeXZ1XSAChHP2vHao86PmfsBwhaogSxq').public_key
public_key = ripemd160_sha256(public_key)

segwit_addr = encode('bc', 0, public_key)
print(segwit_addr)
'''
keyC = Key.from_int(3)
print(keyC.public_key)
public_key = ripemd160_sha256(keyC.public_key)
segwit_addr = encode('bc', 0, public_key)
print(segwit_addr)
print()
pub = '04f9308a019258c31049344f85f89d5229b531c845836f99b08601f113bce036f9388f7b0f632de8140fe337e62a37f3566500a99934c2231b6cb9fd7584b8e672'
pub = '02f9308a019258c31049344f85f89d5229b531c845836f99b08601f113bce036f9'
public_key = bytearray.fromhex(pub)
public_key = ripemd160_sha256(keyC.public_key)
bech32_p2wpkh = encode('bc', 0, public_key)
print(bech32_p2wpkh)
print(public_key_to_address(bytearray.fromhex(pub)))
print(public_key_to_segwit_address(bytearray.fromhex(pub)))
