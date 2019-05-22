#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Dob

'''
动态页面模拟点击：
    模拟点击查看手机号码
'''
from selenium import webdriver
#chromedriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--user-data-dir='+r'C:\Users\Administrator\AppData\Local\Google\Chrome\User Data')
driver = webdriver.Chrome(executable_path=r'C:\Users\Administrator\AppData\Local\Google\Chrome\Application\chromedriver',chrome_options=chrome_options)

#过期
#driver = webdriver.PhantomJS(executable_path=r'D:\python3.6.2\plugins\phantomjs\bin\phantomjs')

class Get58Spider(object):

    def __init__(self):
        self.url = '';
        self.driver = driver
        self.file_name = open("58同城.json", "w", encoding="utf-8")

    def run(self):
        self.driver.get(self.url)

        #https://bj.58.com/shuma/?PGTID=0d100000-0000-1f16-d0a5-410b25bcb2b8&ClickID=9
        # soup = BeautifulSoup(self.driver.page_source, "lxml")
        # online_live = soup.find_all('table', {'id': 'jingzhun'})[0]
        # live_list = online_live.find_all('tr')

        #str = self.driver.find_element_by_xpath('//*[@id="view-connect"]').click()
        self.driver.find_element_by_id('view-connect').click();
        soup = BeautifulSoup(self.driver.page_source, "lxml")
        tel = soup.find_all('a', {'id': 'view-connect'})
        print(tel)


    def quit(self):
        self.file_name.close();
        self.driver.quit();

if __name__=='__main__':
    # chrome_options = webdriver.ChromeOptions()
    # #C:\Users\Administrator\AppData\Local\Google\Chrome\User Data
    # chrome_options.add_argument('--user-data-dir=C:\\Users\Administrator\AppData\Local\Google\Chrome\\User Data')  # 设置成用户自己的数据目录
    # browser = webdriver.Chrome(executable_path=r'C:\Users\Administrator\AppData\Local\Google\Chrome\Application\chromedriver',chrome_options=chrome_options)
    # browser.get("http://www.baidu.com")
    # browser.find_element_by_id("kw").send_keys("selenium")
    # browser.find_element_by_id("su").click()
    # browser.quit()

    get58 = Get58Spider();
    get58.run();


    #get58.quit();
