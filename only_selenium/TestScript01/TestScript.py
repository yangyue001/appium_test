# -*- coding:utf-8 -*-
from selenium import webdriver
import chardet
import string
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException,NoSuchElementException
import traceback
from PageObject.LoginPage import *
from PageObject.buy_smartbid import *

dr = webdriver.Chrome()
dr.maximize_window()
dr.get("http://dev.lantouzi.com/login")
lp = LoginPage(dr)
bs = Buy_smart(dr)
wait = WebDriverWait(dr, 10, 0.2)  # 显示等待

try:
    lp.login()

    time.sleep(1)
    bs.buy_smarbid()


except TimeoutException as e:
    print("timeout",e)
except NoSuchElementException as e:
    print("nosuch ",e)
except Exception as e:
    print("other e",e)
except BaseException as e:
    print("base error",e)
finally:
    dr.close()









