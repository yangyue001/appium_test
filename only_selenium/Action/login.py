from PageObject.LoginPage import *
from selenium import webdriver
def login(dr,username,psw):
    lp = LoginPage(dr)
    lp.get_frame().click()
    lp.get_name().send_keys(username)
    lp.get_userpsw().send_keys(psw)
    lp.get_loginbutton().click()