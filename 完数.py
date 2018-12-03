# -*- coding: utf-8 -*-
"""
Created on Mon Dec  3 21:12:08 2018

@author: SHESHE
"""

k=[ ]
for i in range(1,1001):
    a=i
    for j in range(1,i):
        if i%j==0:
            a=a-j
    if a==0:
        print(i)