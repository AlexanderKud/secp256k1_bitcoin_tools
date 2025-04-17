from bitcoinlib.keys import *

'''
self.public_hex = None
        self._public_uncompressed_hex = None
        self.public_compressed_hex = None
        self.public_byte = None
        self._public_uncompressed_byte = None
        self.public_compressed_byte = None
        self.private_byte = None
        self.private_hex = None
        self._x = None
        self._y = None
        self.x_hex = None
        self.y_hex = None
        self.secret = None
        self.compressed = compressed
        self._hash160 = None
        self.key_format = None
        self.is_private = None
'''
pk = 567
address_U = Key(import_key=pk, network='bitcoin', compressed=False)
print(address_U.address())
print(address_U.public_hex)
print(address_U._x)
print(address_U._y)
print(address_U.hash160.hex())
print(address_U.wif())
print('***************')
address_C = Key(import_key=pk, network='bitcoin', compressed=True)
print(address_C.address())
print(address_C.public_hex)
print(address_C._x)
print(address_C._y)
print(address_C.hash160.hex())
print(address_C.wif())
print('***************')
print(Address(address_C.public_hex, encoding='base58', script_type='p2sh', witness_type='p2sh-segwit').address)
print(Address(address_C.public_hex, encoding='bech32', script_type='p2wpkh').address)
print(Address(address_C.public_hex, encoding='bech32', script_type='p2wsh').address)

'''
print(k.address_uncompressed())
#print(k.public_hex)
print(k.public_uncompressed_hex)
print(k.public_compressed_hex)
print(k._x)
print(k._y)
print(k.hash160.hex())
print(Address(k.public_hex, encoding='bech32', script_type='p2wsh').address)
print(Address(k.public_hex, encoding='bech32', script_type='p2wpkh').address)
print(Address(k.public_hex, encoding='base58', script_type='p2sh', witness_type='p2sh-segwit').address)
print(k.private_hex)
print(k.secret)
#print(help(k))
print(k.wif())
#k.info()
'''
