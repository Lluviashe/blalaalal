# -*- coding: utf-8 -*-
"""
Created on Thu Dec 13 21:17:34 2018

@author: SHESHE
"""

sentence=input("请输入：")
for filter_word in open('filtered_words.txt'):
    fw=filter_word.rstrip()
    if fw in sentence:
        fw_len=len(fw)
        sentence=sentence.replace(fw,'*'*fw_len)
        print(sentence)
    else:
        print(sentence)
    