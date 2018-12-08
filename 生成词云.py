# -*- coding: utf-8 -*-
"""
Created on Sat Dec  8 17:20:11 2018

@author: SHESHE
"""
import jieba
from wordcloud import WordCloud
import matplotlib.pyplot as plt

file='C:/Users/SHESHE/Desktop/a/b.txt'

f=open(file,'r',encoding='UTF-8').read()
cut_text=" ".join(jieba.cut(f))
wordcloud=WordCloud(
            font_path="C:/Windows/Fonts/simfang.ttf",
            background_color="white",width=2000,height=1380).generate(cut_text)
plt.imshow(wordcloud,interpolation="bilinear")
plt.axis("off")
plt.show()