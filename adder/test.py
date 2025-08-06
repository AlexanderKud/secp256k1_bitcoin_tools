import ctypes
import os

#dllfile = 'adder.dll'
dllfile = 'adder.so'
if os.path.isfile(dllfile) == True:
    pathdll = os.path.realpath(dllfile)
    adder = ctypes.CDLL(pathdll)
adder.add_int.argtypes = [ctypes.c_int, ctypes.c_int]
adder.add_int.restype = ctypes.c_int
print(adder.add_int(79,77))
a = ctypes.c_float(5.5)
b = ctypes.c_float(5.5)
add_float = adder.add_float
add_float.restype = ctypes.c_float
print(add_float(a, b))
adder.print_str.argtypes = [ctypes.c_char_p]
print_str = adder.print_str
print_str(str.encode("027f7757d71324a8e6d4c8d1a029ca84de6f0649fd1b122aa91f8bf0a9a9bdb625"))
print_str("Fuckit".encode("utf-8"))
adder.str_return.restype = ctypes.c_char_p
s = adder.str_return()
print(s.decode())
#adder.print_hello()
