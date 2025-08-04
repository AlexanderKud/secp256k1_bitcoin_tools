#P 3.7
import hashlib
##import ecdsa
import codecs
import binascii

def extended_gcd(aa, bb):
    lastremainder, remainder = abs(aa), abs(bb)
    x, lastx, y, lasty = 0, 1, 1, 0
    while remainder:
        lastremainder, (quotient, remainder) = remainder, divmod(lastremainder, remainder)
        x, lastx = lastx - quotient*x, x
        y, lasty = lasty - quotient*y, y
    return lastremainder, lastx * (-1 if aa < 0 else 1), lasty * (-1 if bb < 0 else 1)

def modinv(a, m):
    g, x, y = extended_gcd(a, m)
    if g != 1:
        raise ValueError
    return x % m


N=79
P=97
x0=13; y0=19; # G, basic point

m=(3*x0**2)*modinv(2*y0,P)%P
x=(m**2-x0-x0)%P
y=(-y0+m*(x0-x))%P

print ("n, x,y", str(1).zfill(2), "-","(", x0,y0,")")
print ("n, x,y", str(2).zfill(2),"-","(",x,y,")")

n=3
while n<N:
    m=((y-y0)*modinv(x-x0,P))%P
    mm=m**2%P
    x=(m**2-x-x0)%P
    y=(-y0+m*(x0-x))%P
    print ("n, x,y", str(n).zfill(2),"-","(" ,x,y,")")
    n=n+1
