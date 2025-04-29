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
        \nThanks @iceland2k14'
    print(F), open('found.txt', 'a').write(F)

def bloom(N):
    BELOW = [SM(I)[1:33] for I in range(1, N)]
    bits, hashes, bf = BL(BELOW, 0.000001)
    return bits, hashes, bf, BELOW

def sub(P, BitRANGE):
    KeysP, KeysI, bit, N = [], [], 2**(BitRANGE-2), 2**10
    bit //= N
    for I in range(1, N):
        R = bit * I
        A = SM(R)
        KeysP.append(PA(P, A))
        KeysP.append(PS(P, A))
        KeysI.append(R)
    return KeysP, KeysI

class Multi:
    def __init__(self, Q, F, bits, hashes, bf, BELOW, N, P, KeysP, KeysI, bit):
        self.Q, self.F, self.bits, self.hashes, self.bf, self.BELOW, \
        self.N, self.P, self.KeysP, self.KeysI, self.bit = \
        Q, F, bits, hashes, bf, BELOW, N, P, KeysP, KeysI, bit
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

    def paradigm(self):
        ABOVE, B, S = [], 2**(self.bit), randint(2**(self.bit-1), 2**self.bit)
        for A in range(self.bit-5):
            B //= 2
            S -= B
            if S <= 0:
                S += B
            else:
                ABOVE.append(B)
        return ABOVE

    def main(self):
        while not self.Q.is_set():
            ABOVE = self.paradigm()
            for RIP in self.KeysP:
                C = []
                for A in ABOVE:
                    C.append(A)
                    RIP = PS(RIP, SM(A))
                    if CB(RIP[1:33], self.bits, self.hashes, self.bf):
                        self.match(RIP[1:33], C)
                        
if __name__ == '__main__':
    public_key = '03a2efa402fd5268400c77c20e574ba86409ededee7c4020e4b9f0edbee53de0d4' # Public Key
    BitRANGE = 40   # Bit Range
    N = 1000000     # Load subregion into RAM.
    CPU_COUNT = 4   # Number of cores
    P = P2U(public_key)
    KeysP, KeysI = sub(P, BitRANGE)
    print('Filling subregion into memory...')
    bits, hashes, bf, BELOW = bloom(N)
    #######################
    print('Started!')
    Q, F = MP.Event(), MP.Event()
    for j in range(CPU_COUNT):
        PC = MP.Process(target=Multi, args=(Q, F, bits, hashes, bf, BELOW, N, P, KeysP, KeysI, BitRANGE))
        PC.start()
    F.wait()
    Q.set()

