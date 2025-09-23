import ctypes

secp256k1 = ctypes.CDLL("./secp256k1_lib.so")

secp256k1.check.argtypes = None
secp256k1.check.restype = None

secp256k1.scalar_multiplication.argtypes = [ctypes.c_char_p, ctypes.c_char_p]
secp256k1.scalar_multiplication.restype = None

secp256k1.point_multiplication.argtypes = [ctypes.c_char_p, ctypes.c_char_p, ctypes.c_char_p]
secp256k1.point_multiplication.restype = None

secp256k1.point_to_upub.argtypes = [ctypes.c_char_p, ctypes.c_char_p]
secp256k1.point_to_upub.restype = None

secp256k1.point_to_cpub.argtypes = [ctypes.c_char_p, ctypes.c_char_p]
secp256k1.point_to_cpub.restype = None

secp256k1.double_point.argtypes = [ctypes.c_char_p, ctypes.c_char_p]
secp256k1.double_point.restype = None

secp256k1.negate_point.argtypes = [ctypes.c_char_p, ctypes.c_char_p]
secp256k1.negate_point.restype = None

secp256k1.add_points.argtypes = [ctypes.c_char_p, ctypes.c_char_p, ctypes.c_char_p]
secp256k1.add_points.restype = None

secp256k1.add_points_safe.argtypes = [ctypes.c_char_p, ctypes.c_char_p, ctypes.c_char_p]
secp256k1.add_points_safe.restype = None

secp256k1.add_point_scalar.argtypes = [ctypes.c_char_p, ctypes.c_char_p, ctypes.c_char_p]
secp256k1.add_point_scalar.restype = None

secp256k1.add_point_scalar_safe.argtypes = [ctypes.c_char_p, ctypes.c_char_p, ctypes.c_char_p]
secp256k1.add_point_scalar_safe.restype = None

secp256k1.subtract_points.argtypes = [ctypes.c_char_p, ctypes.c_char_p, ctypes.c_char_p]
secp256k1.subtract_points.restype = None

secp256k1.subtract_points_safe.argtypes = [ctypes.c_char_p, ctypes.c_char_p, ctypes.c_char_p]
secp256k1.subtract_points_safe.restype = None

secp256k1.subtract_point_scalar.argtypes = [ctypes.c_char_p, ctypes.c_char_p, ctypes.c_char_p]
secp256k1.subtract_point_scalar.restype = None

secp256k1.subtract_point_scalar_safe.argtypes = [ctypes.c_char_p, ctypes.c_char_p, ctypes.c_char_p]
secp256k1.subtract_point_scalar_safe.restype = None

secp256k1.increment_point.argtypes = [ctypes.c_char_p, ctypes.c_char_p]
secp256k1.increment_point.restype = None

secp256k1.decrement_point.argtypes = [ctypes.c_char_p, ctypes.c_char_p]
secp256k1.decrement_point.restype = None

secp256k1.point_on_curve.argtypes = [ctypes.c_char_p]
secp256k1.point_on_curve.restype = ctypes.c_bool

secp256k1.privatekey_to_hash160.argtypes = [ctypes.c_int, ctypes.c_bool, ctypes.c_char_p, ctypes.c_char_p]
secp256k1.privatekey_to_hash160.restype = None

secp256k1.publickey_to_hash160.argtypes = [ctypes.c_int, ctypes.c_bool, ctypes.c_char_p, ctypes.c_char_p]
secp256k1.publickey_to_hash160.restype = None

secp256k1.privatekey_to_uwif.argtypes = [ctypes.c_char_p, ctypes.c_char_p]
secp256k1.privatekey_to_uwif.restype = None

secp256k1.privatekey_to_cwif.argtypes = [ctypes.c_char_p, ctypes.c_char_p]
secp256k1.privatekey_to_cwif.restype = None

secp256k1.privatekey_to_wif.argtypes = [ctypes.c_bool, ctypes.c_char_p, ctypes.c_char_p]
secp256k1.privatekey_to_wif.restype = None

secp256k1.wif_to_privatekey.argtypes = [ctypes.c_char_p]
secp256k1.wif_to_privatekey.restype = None

secp256k1.privatekey_to_address.argtypes = [ctypes.c_int, ctypes.c_bool, ctypes.c_char_p, ctypes.c_char_p]
secp256k1.privatekey_to_address.restype = None

secp256k1.publickey_to_address.argtypes = [ctypes.c_int, ctypes.c_bool, ctypes.c_char_p, ctypes.c_char_p]
secp256k1.publickey_to_address.restype = None

secp256k1.hash160_to_address.argtypes = [ctypes.c_int, ctypes.c_bool, ctypes.c_char_p, ctypes.c_char_p]
secp256k1.hash160_to_address.restype = None

secp256k1.publickey_to_point.argtypes = [ctypes.c_char_p, ctypes.c_char_p]
secp256k1.publickey_to_point.restype = None

secp256k1.p2pkh_address_to_hash160.argtypes = [ctypes.c_char_p, ctypes.c_char_p]
secp256k1.p2pkh_address_to_hash160.restype = None

secp256k1.init_bloom.argtypes = [ctypes.c_int, ctypes.c_ulonglong, ctypes.c_double]
secp256k1.init_bloom.restype = None

secp256k1.bloom_info.argtypes = [ctypes.c_int]
secp256k1.bloom_info.restype = None

secp256k1.bloom_save.argtypes = [ctypes.c_int, ctypes.c_char_p]
secp256k1.bloom_save.restype = None

secp256k1.bloom_load.argtypes = [ctypes.c_int, ctypes.c_char_p]
secp256k1.bloom_load.restype = None

secp256k1.bloom_add.argtypes = [ctypes.c_int, ctypes.c_char_p, ctypes.c_int]
secp256k1.bloom_add.restype = None

secp256k1.bloom_check.argtypes = [ctypes.c_int, ctypes.c_char_p, ctypes.c_int]
secp256k1.bloom_check.restype = ctypes.c_int

N = 0xfffffffffffffffffffffffffffffffebaaedce6af48a03bbfd25e8cd0364141
def multiplicative_inverse(x):
    return pow(x, N - 2, N)
    
secp256k1.Init()

def check():
    secp256k1.check()
    
def scalar_multiplication(pk):
    pvk = str(pk % N).encode()
    res = bytes(65)
    secp256k1.scalar_multiplication(pvk, res)
    return res

def point_multiplication(p, pk):
    pvk = str(pk).encode()
    res = bytes(65)
    secp256k1.point_multiplication(p, pvk, res)
    return res

def point_division(p, pk):
    pvk = str(multiplicative_inverse(pk)).encode()
    res = bytes(65)
    secp256k1.point_multiplication(p, pvk, res)
    return res

def point_to_upub(pBytes):
    res = bytes(65)
    secp256k1.point_to_upub(pBytes, res)
    return res.hex()
    
def point_to_cpub(pBytes):
    res = bytes(33)
    secp256k1.point_to_cpub(pBytes, res)
    return res.hex()

def double_point(pBytes):
    res = bytes(65)
    secp256k1.double_point(pBytes, res)
    return res

def negate_point(pBytes):
    res = bytes(65)
    secp256k1.negate_point(pBytes, res)
    return res

def add_points(p1, p2):
    res = bytes(65)
    secp256k1.add_points(p1, p2, res)
    return res

def add_points_safe(p1, p2):
    res = bytes(65)
    secp256k1.add_points_safe(p1, p2, res)
    return res

def add_point_scalar(p, pk):
    pvk = str(pk).encode()
    res = bytes(65)
    secp256k1.add_point_scalar(p, pvk, res)
    return res

def add_point_scalar_safe(p, pk):
    pvk = str(pk).encode()
    res = bytes(65)
    secp256k1.add_point_scalar_safe(p, pvk, res)
    return res

def subtract_points(p1, p2):
    res = bytes(65)
    secp256k1.subtract_points(p1, p2, res)
    return res

def subtract_points_safe(p1, p2):
    res = bytes(65)
    secp256k1.subtract_points_safe(p1, p2, res)
    return res

def subtract_point_scalar(p, pk):
    pvk = str(pk).encode()
    res = bytes(65)
    secp256k1.subtract_point_scalar(p, pvk, res)
    return res

def subtract_point_scalar_safe(p, pk):
    pvk = str(pk).encode()
    res = bytes(65)
    secp256k1.subtract_point_scalar_safe(p, pvk, res)
    return res

def increment_point(pBytes):
    res = bytes(65)
    secp256k1.increment_point(pBytes, res)
    return res

def decrement_point(pBytes):
    res = bytes(65)
    secp256k1.decrement_point(pBytes, res)
    return res

def point_on_curve(pBytes):
    return secp256k1.point_on_curve(pBytes)

def privatekey_to_hash160(addr_type, compressed, pk):
    pvk = str(pk).encode()
    res = bytes(20)
    secp256k1.privatekey_to_hash160(addr_type, compressed, pvk, res)
    return res.hex()
    
def publickey_to_hash160(addr_type, compressed, pBytes):
    res = bytes(20)
    secp256k1.publickey_to_hash160(addr_type, compressed, pBytes, res)
    return res.hex()

def privatekey_to_uwif(pk):
    pvk = str(pk).encode()
    res = bytes(51)
    secp256k1.privatekey_to_uwif(pvk, res)
    return res.decode()

def privatekey_to_cwif(pk):
    pvk = str(pk).encode()
    res = bytes(52)
    secp256k1.privatekey_to_cwif(pvk, res)
    return res.decode()

def privatekey_to_wif(compressed, pk):
    pvk = str(pk).encode()
    res = bytes(52)
    secp256k1.privatekey_to_wif(compressed, pvk, res)
    return res.rstrip(b'\x00').decode()

def wif_to_privatekey(wif):
    pvk = wif.encode()
    res = bytes(32)
    secp256k1.wif_to_privatekey(pvk, res)
    return int.from_bytes(res, 'big')

def privatekey_to_address(addr_type, compressed, pk):
    pvk = str(pk).encode()
    res = bytes(42)
    secp256k1.privatekey_to_address(addr_type, compressed, pvk, res)
    return res.rstrip(b'\x00').decode()
    
def publickey_to_address(addr_type, compressed, p):
    res = bytes(42)
    secp256k1.publickey_to_address(addr_type, compressed, p, res)
    return res.rstrip(b'\x00').decode()

def hash160_to_address(addr_type, compressed, hash160):
    res = bytes(42)
    secp256k1.hash160_to_address(addr_type, compressed, bytes.fromhex(hash160), res)
    return res.rstrip(b'\x00').decode()

def publickey_to_point(p):
    pub = p.encode()
    res = bytes(65)
    secp256k1.publickey_to_point(pub, res)
    return res

def p2pkh_address_to_hash160(address):
    addr = address.encode()
    res = bytes(25)
    secp256k1.p2pkh_address_to_hash160(addr, res)
    return res.hex()[2:42]
    
def init_bloom(index, entries, error):
    secp256k1.init_bloom(index, entries, error)

def bloom_info(index):
    secp256k1.bloom_info(index)

def bloom_save(index, filename):
    secp256k1.bloom_save(index, filename.encode())
    
def bloom_load(index, filename):
    secp256k1.bloom_load(index, filename.encode())

def bloom_add(index, item):
    if type(item) != bytes: item = str(item).encode()
    secp256k1.bloom_add(index, item, len(item))

def bloom_check(index, item):
    if type(item) != bytes: item = str(item).encode()
    return secp256k1.bloom_check(index, item, len(item))
