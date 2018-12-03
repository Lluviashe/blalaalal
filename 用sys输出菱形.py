# -*- coding: utf-8 -*-
"""
Created on Mon Dec  3 21:33:35 2018

@author: SHESHE

"""

from sys import stdout
for i in range(0,4):
    for j in range(0,2*i+1):
        stdout.write("*")
    print()
for i in range(0,3):
    for j in range(0,-2*i+5):
        stdout.write("*")
    print()