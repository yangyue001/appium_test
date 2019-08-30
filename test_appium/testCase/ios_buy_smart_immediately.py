import unittest
import os
from random import randint
from appium import webdriver
from time import sleep
from datetime import datetime
from Common_tools import HTMLTestRunner
from Common_tools import get_massage
from Common_tools.test_ios_get_elements import *
from Common_tools import myLog
import paramunittest
from Common_tools.common01 import clear_ssdb
from common_business.ios_login_business import ios_login


login_xls = get_xls_nrows('ios_test_case.xlsx','login')

@paramunittest.parametrized(*login_xls)
class SmartBid_Buy_Immediately(unittest.TestCase):

    def setParameters(self,case_name,number,psw,name,one_psw):
        self.case_name = str(case_name)
        self.number = str(number)
        self.psw = str(psw)
        self.name = str(name)
        self.one_psw = str(one_psw)



    @classmethod
    def setUpClass(cls):
        clear_ssdb()
        cls.log = myLog.MyLog.get_log()
        cls.logger =cls.log.get_logger()
        # set up appium
        app = os.path.abspath(
            '/Users/yangyue/Library/Developer/Xcode/DerivedData/ios-bcfdjtsoncuvfdepygsrhjarjcya/Build/Products/Debug-iphonesimulator/ios.app')
        cls.driver = webdriver.Remote(
            command_executor='http://127.0.0.1:4723/wd/hub',
            desired_capabilities={
                'app': app,
                'platformName': 'iOS',
                'platformVersion': '12.1',
                "noReset":True,
                'deviceName': 'iPhone XR'
            })
        #butt = cls.driver.find_element_by_ios_predicate('type="XCUIElementTypeButton" and name="Allow"')
        #butt = get_element(cls.driver,'right_allowed')

    def setUp(self):
        clear_ssdb(self.number)

        ios_login(self.driver,self.number,self.psw)
        my_btn = get_element(self.driver, 'my_btn')
        my_btn.click()
        # self.driver.find_element_by_ios_predicate('type="XCUIElementTypeButton" and name=" 登录去赚钱"').click()
        my_login_btn = get_element(self.driver, 'my_login_btn')
        my_login_btn.click()
        # inpu = self.driver.find_element_by_ios_predicate("type='XCUIElementTypeTextField'")
        inpu = get_element(self.driver, 'login_input')
        inpu.clear()
        inpu.send_keys(self.number)

        # psw = self.driver.find_element_by_ios_predicate('type="XCUIElementTypeSecureTextField"')
        psw = get_element(self.driver, 'login_psw')
        psw.send_keys(self.psw)

        # login = self.driver.find_element_by_ios_predicate('type="XCUIElementTypeButton" and name="登录"')
        login = get_element(self.driver, 'login_btn')
        login.click()

        # jump = self.driver.find_element_by_ios_predicate('type="XCUIElementTypeButton" and name="跳过"')
        jump = get_element(self.driver, 'jump_btn')
        jump.click()


        l = get_massage.get_size(self.driver)
        x1 = int(l[0] * 0.1)
        y1 = int(l[1] * 0.95)
        self.driver.tap([(x1, y1)], 200)
        sleep(3)



    def tearDown(self):
        #print('w')
        my_btn = get_element(self.driver,'my_btn')
        my_btn.click()
        setting = get_element(self.driver,'setting')
        setting.click()
        logout_btn = get_element(self.driver,'logout_btn')
        logout_btn.click()
        self.driver.quit()



    def test_buy_smart_one(self):


        #点击智选的icon
        smarbid_icon = get_element(self.driver,'smarbid_icon')
        smarbid_icon.click()
        #找到智选的马上加入按钮
        smart_join = get_element(self.driver,'smart_join')
        smart_join.click()

        smart_input_lan = get_element(self.driver,'smart_input_lan')
        smart_input_lan.click()

        key1 = get_element(self.driver,'self_key_1')
        key1.click()
        for i in range(3):
            self_key_0 = get_element(self.driver,'self_key_0')
            self_key_0.click()
        self_key_sure = get_element(self.driver,'self_key_sure')
        self_key_sure.click()

        smart_sure_jion = get_element(self.driver,'smart_sure_jion')
        smart_sure_jion.click()
        balance_buy_sure = get_element(self.driver,'balance_buy_sure')
        balance_buy_sure.click()

        check_order = get_element(self.driver,'check_order')
        check_order.click()
        for a in range(2):
            page_back = get_element(self.driver,'page_back')
            page_back.click()

    def runn(self):
        log = myLog.Log()
        logger = log.get_logger()
        reportpath = os.path.join(rootDir, "result", str(datetime.now().strftime("%Y%m%d%H%M%S")), "report1.html")
        with open(reportpath, 'wb') as fp:
            try:
                suit = unittest.TestSuite()
                suit.addTest(SmartBid_Buy_Immediately('test_buy_smart_one'))
                if suit is not None:
                    logger.info("********TEST START********")
                    runner = HTMLTestRunner.HTMLTestRunner(stream=fp)
                    runner.run(suit)
                else:
                    logger.info("Have no case to test.")
            except Exception as e:
                logger.error(e)
            finally:
                logger.info("*********TEST END*********")


if __name__ == '__main__':
    SS = SmartBid_Buy_Immediately()
    SS.run()