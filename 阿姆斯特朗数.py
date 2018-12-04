# -*- coding: utf-8 -*-
"""
Created on Tue Dec  4 16:54:52 2018

@author: SHESHE
"""

i=input()
n=len(i)
print(n)
m=0
for b in i:
    m+=int(b)**n
if int(i)==m:
    print(i+"是阿姆斯特朗数")
else:
    print("不是阿姆斯特朗数")