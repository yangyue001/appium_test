# -*- coding:utf-8 -*-
from selenium import webdriver

import time

from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.common.by import By

from selenium.common.exceptions import TimeoutException, NoSuchElementException

import traceback
from Util.ParsePageObjectRepository import *

from PageObject.LoginPage import *


class Buy_smart:
    def __init__(self,dr):
        self.dr = dr
        self.wait = WebDriverWait(self.dr,10,0.2)
        self.parse_cofig_file = parsepageobjectrepository()
        self.recharge_items = self.parse_cofig_file.getItemSection('smart_buy')

    def get_frame(self):
        locateType, locateExpression = self.recharge_items['buy_smartbid.frame'].split('?')
        smart_frame = getElement(self.dr,locateType,locateExpression)
        return smart_frame
    def get_joinsmart(self):
        locateType, locateExpression = self.recharge_items['buy_smartbid.joinsmart'].split('?')
        joinsmart = getElement(self.dr,locateType,locateExpression)
        return joinsmart
    def get_smartamout(self):#输入金额框
        locateType, locateExpression = self.recharge_items['buy_smartbid.smart_amount'].split('?')
        smart_amount = getElement(self.dr,locateType,locateExpression)
        return smart_amount
    def get_remaining(self):
        locateType, locateExpression = self.recharge_items['buy_smartbid.remaining'].split('?')
        remaining = getElement(self.dr,locateType,locateExpression)
        return remaining
    def get_amount_submit(self):
        locateType, locateExpression = self.recharge_items['buy_smartbid.amount_submit'].split('?')
        amount_submit = getElement(self.dr,locateType, locateExpression)
        return amount_submit

    def get_buy_now(self):
        locateType, locateExpression = self.recharge_items['buy_smartbid.buy_now'].split('?')
        buy_now =getElement(self.dr,locateType, locateExpression )
        return buy_now
    def get_one_transfer(self):
        locateType, locateExpression = self.recharge_items['buy_smartbid.one_transfer'].split('?')
        one_transfer = getElement(self.dr,locateType,locateExpression)
        return one_transfer
    def get_greet(self):
        locateType, locateExpression = self.recharge_items['buy_smartbid.gree'].split('?')
        gree = getElement(self.dr,locateType, locateExpression)
        return gree

    def get_onesure(self):
        locateType, locateExpression = self.recharge_items['buy_smartbid.onesure'].split('?')
        onesure = getElement(self.dr,locateType, locateExpression)
        return onesure

    def get_recharge(self):
        locateType, locateExpression = self.recharge_items['buy_smartbid.recharge'].split('?')
        recharge = getElement(self.dr, locateType, locateExpression)
        return recharge

    def get_i_know(self):
        locateType, locateExpression = self.recharge_items['buy_smartbid.iknown'].split('?')
        iknow = getElement(self.dr, locateType, locateExpression)
        return iknow
    def get_phoneV(self):
        locateType, locateExpression = self.recharge_items['buy_smartbid.phonev'].split('?')
        phoneV = getElement(self.dr, locateType, locateExpression)
        return phoneV

    def get_passwd(self):
        locateType, locateExpression = self.recharge_items['buy_smartbid.passwd'].split('?')
        passwd= getElement(self.dr, locateType, locateExpression)
        return passwd


    def get_isAgreeReg(self):
        locateType, locateExpression = self.recharge_items['buy_smartbid.reg'].split('?')
        reg = getElement(self.dr, locateType, locateExpression)
        return reg

    def get_renextButton(self):
        locateType, locateExpression = self.recharge_items['buy_smartbid.re_nextbutton'].split('?')
        renextButton = getElement(self.dr, locateType, locateExpression)
        return renextButton

    def get_check_order(self):
        locateType, locateExpression = self.recharge_items['buy_smartbid.check_order'].split('?')
        check_order = getElement(self.dr, locateType, locateExpression)
        return check_order

if __name__=='__main__':
    dr = webdriver.Chrome()
    l = Buy_smart(dr)
    l.get_one_nextButton()



