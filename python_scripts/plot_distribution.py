#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Created on 2015-02-10 12:55:33

@author: mat

"""
from __future__ import (unicode_literals, absolute_import,
                        print_function, division)
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import math
import os
import time
from datetime import datetime

cwd = os.getcwd()
print(cwd)
lstfi = os.listdir(cwd)

t0 = time.ctime()
print(t0)

listMarkers = ['-', '--', '-.', ':', '_', '.', ',', '|', 'o', 'v', '^', '<', '>', '1', '2'
                                                                                       '3', '4', 's', 'p', 'h', '+',
               'H', '*', 'x', 'D', 'd']

event = [1, 2, 4, 3, 4, 6, 8, 3, 7, 5, 6, 2, 0, 1, 8, 4, 6, 5, 9,
         2, 7, 5, 6, 0, 1, 7, 3, 0, 2, 5, 7, 1, 0, 6, 3, 5, 7, 0,
         2, 3, 5, 7, 2, 5, 9, 2, 4, 3, 6, 1, 0, 9, 2, 8, 1, 3, 0,
         2, 9, 1, 5, 6, 0, 2, 0, 2, 9, 5, 2, 9, 3, 2, 8, 4, 7, 6,
         5, 9, 3, 8, 4, 2, 7]

nb_interval = 6

##Python 3
compte3 = {k: event.count(k) for k in set(event)}

##Python 2
# compte2 = dict([(k,event.count(k)) for k in set(event)])


print(compte3)

# plt.figure(1)
# plt.bar(compte3.keys(), compte3.values())


mu0, mu1 = 0, 1
sigma0, sigma1 = 1, 1


# distribution function
def normal_dist(x, mu=mu0, sigma=sigma0):
    return (1 / (sigma * math.sqrt(2 * math.pi)) * math.exp(-(x - mu) ** 2 / (2 * sigma ** 2)))


def integr(f, mi, ma, h):
    s = 0
    for x in np.linspace(mi, ma, round((ma - mi) / h), endpoint=True):
        a = f(x)
        b = f(x + h)
        s += (a + b) / 2 * h
    return s


# integration = integr(normal_dist, -5, 5, 0.0001)
# print ("test " + str(integration))


h = 0.01
integr2 = 0
mi = -5  # min interval
ma = 5  # max interval
x = np.arange(mi, ma, h)
y1 = np.asarray([normal_dist(x1, mu0, sigma0) for x1 in x])
y2 = np.asarray([normal_dist(x1, mu1, sigma1) for x1 in x])

for i, xi in enumerate(np.linspace(mi, ma, round((ma - mi) / h), endpoint=True)):
    if y1[i] > y2[i]:
        integr2 += normal_dist(xi, mu1, sigma1) * h
        print("1 " + str(i) + "  " + str(y2[i]))
    else:
        integr2 += normal_dist(xi, mu0, sigma0) * h
        print("2 " + str(i) + "  " + str(y1[i]))

print("integral = " + str(integr2))

plt.figure(2)
plt.plot(x, y1, label="mu=" + str(mu0) + ", sigma=" + str(sigma0))
plt.plot(x, y2, label="mu=" + str(mu1) + ", sigma=" + str(sigma1))
plt.fill_between(x, 0, y2, where=y2 <= y1, interpolate=True)
plt.fill_between(x, 0, y1, where=y2 >= y1, interpolate=True)

plt.xlabel("X")
plt.ylabel("probabiblity density function")
plt.legend()

plt.show()
