# -*- coding: utf-8 -*-
"""
Created on Sat Dec  1 15:47:41 2018

@author: SHESHE
"""

import os  #打开文件时需要
from PIL import Image
import re

Start_path='E:/image/'
iphonex_width=2436
iphonex_depth=1125
list=os.listdir(Start_path)

count=0
for pic in list:
    path=Start_path+pic
    print(path)
    im=Image.open(path)
    w,h=im.size


    if w>iphonex_width:
        print (pic)
        print ("图片名称为"+pic+"图片被修改")
        h_new=iphonex_width*h/w
        w_new=iphonex_width
        count=count+1
        out = im.resize((w_new,h_new),Image.ANTIALIAS)
        new_pic=re.sub(pic[:-4],pic[:-4]+'_new',pic)
        new_path=Start_path+new_pic
        out.save(new_path)

    if h>iphonex_depth:
        print (pic)
        print ("图片名称为"+pic+"图片被修改")
        w_new=iphonex_depth*w/h
        h_new=iphonex_depth
        count=count+1
        out = im.resize((w_new,h_new),Image.ANTIALIAS)
        new_pic=re.sub(pic[:-4],pic[:-4]+'_new',pic)
        new_path=Start_path+new_pic
        out.save(new_path)

print ('END')
count=str(count)
print ("共有"+count+"张图片尺寸被修改")

