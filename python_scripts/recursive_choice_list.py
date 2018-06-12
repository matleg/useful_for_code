# -*- coding: utf-8 -*-
"""

have to choose 3 choices between instr.
have to list all the choices possible (5**3 = 125)

1st method with random
2nd method with recursivity


"""

import random
import time

instr = ['a', 'b', 'c', 'd', 'e']

##################
# first method
##################
t1 = time.time()
combi = []
i = 0
while i < 10000:
    rr = ''
    for j in range(3):
        rr += random.choice(instr)
    if rr not in combi:
        combi.append(rr)
    i += 1

print(len(combi))
print(sorted(combi))
t2 = time.time()
print(t2 - t1)

##################
# second method
##################
t3 = time.time()
combi = []
w = ''


def pickup(combi, w):
    i = 0
    while i < len(instr):
        if len(w) < 3:
            w += instr[i]
            if len(w) == 3:
                combi.append(w)
                w = w[:-1]
                i += 1
                continue
            combi = pickup(combi, w)
        w = w[:-1]
        i += 1
    return (combi)


combi = pickup(combi, w)

print(len(combi))
print(combi)
t4 = time.time()
print(t4 - t3)
