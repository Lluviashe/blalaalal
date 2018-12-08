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
from lxml import etree

qq=1042005814
file='C:/Users/SHESHE/Desktop/a/{}.text'.format(qq)
save='/Users/SHESHE/Downloads/{}.jpg'.format(qq)
driver = webdriver.Firefox()
driver.maximize_window() 

def get_shuoshuo():
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
        driver.switch_to_default_content()
    driver.implicitly_wait(3)
    try:
        driver.find_element_by_id('QM_OwnerInfo_Icon')
    except:
        print(u"没有权限进入好友空间")
        driver.quit

    else:
        for j in range(1,5):
            driver.execute_script('window.scrollBy(0,5000)')
            time.sleep(2)          #page_source方法可以直接返回页面源码#
            selector=etree.HTML(driver.page_source) #etree.HTML():构造了一个XPath解析对象并对HTML文本进行自动修正#
            title=selector.xpath('//li/div/div/pre/text()')

        for i in title:
            with open(file, 'a+') as f:
                f.write(i+'\n\n')
            f.close()
        
        get_wordcloud(file)

def get_wordcloud(file):
    f=open(file,'r',encoding='gbk').read()
    cut_text=" ".join(jieba.cut(f))
    wordcloud=WordCloud(
            font_path="C:/Windows/Fonts/simfang.ttf",
            background_color="white",width=2000,height=1500).generate(cut_text)
    plt.imshow(wordcloud,interpolation="bilinear")
    plt.axis("off")
    plt.show()
    wordcloud.to_file(save)

get_shuoshuo()
