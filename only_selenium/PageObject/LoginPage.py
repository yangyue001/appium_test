# -*- coding:utf-8 -*-
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import traceback
from Util.ParsePageObjectRepository import *
from Util.ObjectMap import *
import time

class LoginPage():
    def __init__(self,dr):
        self.dr = dr
        self.parse_cofig_file =parsepageobjectrepository()
        self.login_page_items = self.parse_cofig_file.getItemSection('login')
        #print("self.login_page_items:", self.login_page_items)
        self.wait = WebDriverWait(self.dr, 10, 0.2)

    def get_in_button(self):
        locateType, locateExpression = self.login_page_items['login_page.in_button'].split('?')
        in_button = getElement(self.dr, locateType, locateExpression)
        return in_button

    def get_frame(self):
        locateType, locateExpression = self.login_page_items['login_page.frame'].split('?')
        frame = getElement(self.dr,locateType,locateExpression)
        return frame
    def get_name(self):
        locateType, locateExpression = self.login_page_items['login_page.username'].split('?')
        username = getElement(self.dr,locateType,locateExpression)
        return username

    def get_userpsw(self):
        locateType, locateExpression = self.login_page_items['login_page.password'].split('?')
        userpassword = getElement(self.dr, locateType, locateExpression)
        return userpassword
    def get_loginbutton(self):
        locateType, locateExpression = self.login_page_items['login_page.loginbutton'].split('?')
        userpassword = getElement(self.dr, locateType, locateExpression)
        return userpassword



'''
if __name__=='__main__':
    dr = webdriver.Chrome()
    dr.get("http://dev.lantouzi.com/login")
    dr.maximize_window()
    lg = LoginPage(dr)
    lg.get_frame().click()

    lg.get_name().send_keys('17300013249')
    lg.get_userpsw().send_keys('11111111')
    lg.get_loginbutton().click()
    time.sleep(2)
    dr.quit()

'''