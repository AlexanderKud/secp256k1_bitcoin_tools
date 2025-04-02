def mod(x,m): #modulo operation based on addition and subtraction x(number) m(modulus) for arbitrarily large integers
    if x > 0: #to check how many cut_down or add_up ops are necessary
        if x < m:
            return x
        else:
            res = x // m
            print(f'Positive[+] number of cut_down ops [{res}]')
            x = x - (res*m)
            return x
    else:
        res = abs(x) // m
        x = x + (res*m)
        if x == 0:
            print(f'Negative[-] number of add_up ops [{res}]')
        else:
            x += m
            print(f'Negative[-] number of add_up ops [{res+1}]')     
        return x

P = 115792089237316195423570985008687907853269984665640564039457584007908834671663
N = 115792089237316195423570985008687907852837564279074904382605163141518161494337
print(mod(P*2, P))
print(mod(-P, P))
print(mod(P+2*88,P))
print(mod(-111,11))
print(mod(35+36,37))
