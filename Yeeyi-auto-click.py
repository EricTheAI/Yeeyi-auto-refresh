#coding=utf-8
import datetime
import time
from splinter import Browser
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

USERNAME = ''
PASSWORD = ''
URL = ''

def auto_refresh(url):
    browser.get(url)
    
    elem = browser.find_element_by_name('username')  # Find the 用户名 box
    elem.send_keys(USERNAME + Keys.TAB)
    elem = browser.find_element_by_name('password')  # Find the 密码 box
    elem.send_keys(PASSWORD + Keys.TAB)
    elem = browser.find_element_by_name('cookietime')  # Find the “自动登录” box
    elem.send_keys(Keys.SPACE + Keys.RETURN)
    
    try:
        wait = WebDriverWait(browser, 10)
        element = wait.until(
            EC.presence_of_element_located((By.XPATH, "/html/body[@id='nv_forum']/div[@id='wp']/div[@id='ct']/div[@id='postlist']/div[@id='post_27072678']/table[@id='pid27072678']/tbody/tr[1]/td[@class='plc']/div[@class='pi']/div[@class='pti']/div[@class='authi']/a[@id='k_refresh']/i"))
        )
        browser.find_element_by_xpath("/html/body[@id='nv_forum']/div[@id='wp']/div[@id='ct']/div[@id='postlist']/div[@id='post_27072678']/table[@id='pid27072678']/tbody/tr[1]/td[@class='plc']/div[@class='pi']/div[@class='pti']/div[@class='authi']/a[@id='k_refresh']/i").click()  # Click the 提升帖子 button
        print("成功提升!")
        time.sleep(3)    # to observe whether succeeded or not
    finally:
        browser.quit()
        print("退出浏览器")

# need to download the driver first
browser = webdriver.Chrome(executable_path="/usr/local/bin/chromedriver")
t = datetime.datetime.now().timetuple()    # get current time

while True:    
    if (8 <= t[3] <= 24) or (t[3] == 0):    # choose better time
        auto_refresh(URL)
        print(datetime.datetime.now())
        time.sleep(3600)
        t = datetime.datetime.now().timetuple()
    else:
        print("大半夜的别刷了")
        print(datetime.datetime.now())
        browser.quit()
        time.sleep(3600)
        t = datetime.datetime.now().timetuple()
