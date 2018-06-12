#! /usr/bin/python
# -*- coding: utf-8 -*-

"""
Created on Sun Apr 19 10:53:47 2015

delete duplicate files! to be used with the command fdupes on linux, redirecting its output to the file dupes
fdupes . > dupes

@author: mat
"""

import os
import time

cwd = os.getcwd()
print(cwd)

t0 = time.ctime()
print(t0)

filename = "dupes"

size = 0
nb_f = 0

with open(filename, 'r') as f:
    contents = f.readlines()
    for i, l in enumerate(contents):
        if l == "\n":
            print(i + 1, contents[i + 1][:-1])
            size += os.stat(contents[i + 1][:-1]).st_size
            nb_f += 1
            # os.remove(contents[i+1][:-1])

print(nb_f, size)
