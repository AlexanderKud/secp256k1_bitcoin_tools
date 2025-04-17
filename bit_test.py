from bit import Key
#from bit.format import bytes_to_wif

keyU = Key.from_int(1)
keyU._public_key = keyU._pk.public_key.format(compressed=False)
print(keyU.address)
print(keyU.public_key.hex())
print(keyU.to_wif())
keyC = Key.from_int(1)
print(keyC.address)
print(keyC.public_key.hex())
print(keyC.to_wif())
print(keyC.segwit_address)
print('**********')
print(Key.from_int(1).address)
