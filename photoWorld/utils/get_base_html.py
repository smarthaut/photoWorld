#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/5/29 上午9:15
# @Author  : huanghe
# @Site    : 
# @File    : get_base_html.py
# @Software: PyCharm
#scrapy 获取的页面总是缺少元素 导致数据获取不全，采用selenium 获取静态页面

from selenium import webdriver
import time
import os



def get_base_page(page=0):
    
    chromeDriver = webdriver.Chrome('/Users/huanghe/Desktop/project/auto_test/drivers/chromedriver')
    chromeDriver.get("http://www.photoworld.com.cn/page/"+str(page))
    time.sleep(20)
    html = chromeDriver.execute_script("return document.documentElement.outerHTML")
    with open("page"+str(page)+".html","w") as f:
        f.write(html)
    chromeDriver.quit()
    return "file:////"+os.path.split(os.path.abspath(__file__))[0]+"/"+"page"+str(page)+".html"





if __name__ == '__main__':
    print(get_base_page())

