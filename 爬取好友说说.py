# -*- coding: utf-8 -*-
"""
Created on Thu Dec  6 20:33:48 2018

@author: SHESHE
"""

from selenium import webdriver
import time
import jieba
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import os
from lxml import etree

driver = webdriver.Firefox()
driver.maximize_window() 

def get_shuoshuo(qq,path):
    driver.set_page_load_timeout(10)
    driver.get("http://user.qzone.qq.com/{}/311".format(qq))
    time.sleep(3)
    try:
        driver.find_element_by_id('login_div')    
    except:
        print(u"网页异常")
    else:
        driver.switch_to.frame('login_frame')
        driver.find_element_by_id('switcher_plogin').click()
        driver.find_element_by_id('u').clear()
        driver.find_element_by_id('u').send_keys('1042005814')
        driver.find_element_by_id('p').clear()
        driver.find_element_by_id('p').send_keys('Sxj9810266')
        driver.find_element_by_id('login_button').click()
        driver.switch_to_default_content
    driver.implicitly_wait(3)
    try:
        driver.find_element_by_id('QM_OwnerInfo_Icon')
    except:
        print(u"没有权限进入好友空间")
        driver.quit


    for j in range(1,5):
            driver.execute_script('window.scrollBy(0,5000)')
            time.sleep(2)
            selector=etree.HTML(driver.page_source)
            title=selector.xpath('//li/div/div/pre/text()')
    
    for i in title:
        if not os.path.exists(path):
            print(u'创建成功')
        with open(path,'a+')as path:
            path.write(i+'\n\n')
            path.close()
        get_wordcloud(path)

def get_wordcloud(file):
    f=open(file,'r',encoding='gbk').read()
    cut_text=" ".join(jieba.cut(f))
    wordcloud=WordCloud(
            font_path="C:/Windows/Fonts/simfang.ttf",
            background_color="white",width=2000,height=1380).generate(cut_text)
    plt.imshow(wordcloud,interpolation="bilinear")
    plt.axis("off")
    plt.show()

if __name__ == '__main__':
    work_path='C:/Users/SHESHE/Desktop/a/b.text'
    get_shuoshuo('5625476',work_path)