# -*- coding: utf-8 -*-
"""
Created on Tue Jan 15 17:02:36 2019

@author: SHESHE
"""

a=int(input("输入数字"))
b=int(input("输入数字"))
m=0

if a>b:
    s=b
else:
    s=a
    
for i in range(1,s+1):
    if(a%i==0)and(b%i==0):
        m=i
print('最大公约数为:',m)
print('最小公倍数为：',a*b/m)  #最小公倍数等于两数乘积除以最大公约数