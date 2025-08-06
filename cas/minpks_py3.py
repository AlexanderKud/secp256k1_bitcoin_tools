#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ./minpks_py3.py | ./brainflayer -v -a -c uc -b btcs.blf -o found.keys
import random
import hashlib

chars = u"23456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz"

while True:
    password =  ('%s%s' % ('S', ''.join([chars[ random.randrange(0,len(chars)) ] for i in range(29)])))
    t = (password + '?').encode('utf-8')
    CasHash = hashlib.sha256(t).digest()
    if CasHash[0] == '\x00':
        print("%s" % password)
    else:
    	continue
