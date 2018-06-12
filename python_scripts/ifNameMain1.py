#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 22 22:04:50 2014
to see the effect of "if name == __main__"
@author: mat
"""


def croco():
    print ("just trying 007")


if __name__ == "__main__":
    croco()

print ("my name is " + str(__name__) + " in ifNameMain1")
