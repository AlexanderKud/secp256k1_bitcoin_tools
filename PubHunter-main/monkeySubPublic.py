# 17/11/2022
# Created by Sezgin YILDIRIM

import multiprocessing as MP
from random import randint
from ice.secp256k1 import (
    scalar_multiplication as SM,
    Fill_in_bloom as BL,
    pub2upub as P2U,
    point_addition as PA,
    point_subtraction as PS,
    check_in_bloom as CB,
    point_to_cpub as P2C,
    privatekey_to_address as PTC,
    btc_pvk_to_wif as WIF)
import sys

def result(YHVH):
    F = f'\n{"*"*80}\
        \nSecret KEY  : 0x{hex(YHVH)[2:].zfill(64).upper()}\
        \nPublic KEY  : {P2C(SM(YHVH)).upper()}\
        \nPrivate KEY : {WIF(YHVH, True)}\
        \nAddress     : {PTC(0, True, YHVH)}\n{"*"*80}\n\
        \nDonate      : 0x3329A9C3Dd53e698191cE0af641a528369eCdc2c\
        \nGithub      : https://github.com/geokomplo/PubHunter\n\
        \nThanks @iceland2k14\n'
    print(F), open('found.txt', 'a').write(F)

def bloom(N):
    BELOW = [SM(I)[1:33] for I in range(1, N)]
    bits, hashes, bf = BL(BELOW, 0.000001)
    return bits, hashes, bf, BELOW

class Multi:
    def __init__(self, Q, F, bits, hashes, bf, BELOW, N, P, bit):
        self.Q, self.F, self.bits, self.hashes, self.bf, self.BELOW, \
        self.N, self.P, self.bit = \
        Q, F, bits, hashes, bf, BELOW, N, P, bit
        self.R1, self.R2, self.R3 = 2**(self.bit-1), 2**self.bit, self.bit-5
        self.monkey()
        self.main()

    def found(self, SUM, I):
        for R in self.KeysI:
            TETRAGRAMMATON = [abs(SUM + R), abs(SUM - R), abs(SUM + R - I), abs(SUM - R - I)]
            for YHVH in TETRAGRAMMATON:
                if SM(YHVH) == self.P:
                    result(YHVH)
                    sys.exit()

    def match(self, RIP, C):
        if RIP in self.BELOW:
            print('Match found...')
            self.F.set()
            for I in range(1, self.N):
                if SM(I)[1:33] == RIP:
                    break
            self.found(sum(C) + I, I * 2)

    def monkey(self):
        self.KeysP, self.KeysI, bit, N = [], [], 2**(self.bit-4), 2**10
        for I in range(N):
            R = randint(1, bit)
            A = SM(R)
            self.KeysP.append(PA(self.P, A))
            self.KeysP.append(PS(self.P, A))
            self.KeysI.append(R)

    def paradigm(self):
        ABOVE, B, S = [], self.R2, randint(self.R1, self.R2)
        for A in range(self.R3):
            B //= 2
            S -= B
            if S <= 0:
                S += B
            else:
                ABOVE.append(B)
        return ABOVE

    def main(self):
        c = 0
        while not self.Q.is_set():
            ABOVE = self.paradigm()
            for RIP in self.KeysP:
                C = []
                for A in ABOVE:
                    C.append(A)
                    RIP = PS(RIP, SM(A))
                    if CB(RIP[1:33], self.bits, self.hashes, self.bf):
                        self.match(RIP[1:33], C)
            c += 1
            if c == 1000:
                self.monkey()
                c = 0
                        
if __name__ == '__main__':
    public_key = '03f46f41027bbf44fafd6b059091b900dad41e6845b2241dc3254c7cdd3c5a16c6'  # Public Key
    BitRANGE = 50 # Bit Range
    N = 8000000   # Load subregion into RAM.
    CPU_COUNT = 4 # Number of cores
    P = P2U(public_key)
    print('Filling subregion into memory...')
    bits, hashes, bf, BELOW = bloom(N)
    #######################
    print('Started!')
    Q, F = MP.Event(), MP.Event()
    for j in range(CPU_COUNT):
        PC = MP.Process(target=Multi, args=(Q, F, bits, hashes, bf, BELOW, N, P, BitRANGE))
        PC.start()
    F.wait()
    Q.set()










