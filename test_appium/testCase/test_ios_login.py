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
from Common_tools.common01 import clear_ssdb
import paramunittest
from common_business.ios_recharge import recharge
from common_business.ios_withdraw import ios_withdraw_all


login_xls = get_xls_nrows('ios_test_case.xlsx','login')

@paramunittest.parametrized(*login_xls)
class LoginCase(unittest.TestCase):

    def setParameters(self,case_name,number,psw,name,one_psw):
        self.case_name = str(case_name)
        self.number = str(number)
        self.psw = str(psw)
        self.name = str(name)
        self.one_psw = str(one_psw)



    @classmethod
    def setUpClass(cls):

        cls.log = myLog.MyLog.get_log()
        cls.logger =cls.log.get_logger()
        # set up appium
        app = os.path.abspath('/Users/yangyue/Library/Developer/Xcode/DerivedData/ios-bcfdjtsoncuvfdepygsrhjarjcya/Build/Products/Debug-iphonesimulator/ios.app')
        cls.driver = webdriver.Remote(
            command_executor='http://127.0.0.1:4723/wd/hub',
            desired_capabilities={
                'app': app,
                'platformName': 'iOS',
                'platformVersion': '12.1',
                'noReset' : True,
                'deviceName': 'iPhone XR'
            })
        #butt = cls.driver.find_element_by_ios_predicate('type="XCUIElementTypeButton" and name="Allow"')
        #butt = get_element(cls.driver,'right_allowed')

        cls.driver.implicitly_wait(10)

        #butt = cls.driver.find_element(by='-ios predicate string', value='type="XCUIElementTypeButton" and name="Allow"')
        #butt.click()
        #sleep(2)
        #get_massage.page_arun(cls.driver)
        #get_massage.click_in(cls.driver)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def setUp(self):
        clear_ssdb(self.number)

    def tearDown(self):
        #print('w')
        my_btn = get_element(self.driver,'my_btn')
        my_btn.click()
        setting = get_element(self.driver,'setting')
        setting.click()
        logout_btn = get_element(self.driver,'logout_btn')
        logout_btn.click()
        clear_ssdb(self.number)

    def test_login(self):
        my_btn = get_element(self.driver, 'my_btn')
        my_btn.click()
        #self.driver.find_element_by_ios_predicate('type="XCUIElementTypeButton" and name=" 登录去赚钱"').click()
        my_login_btn=get_element(self.driver,'my_login_btn')
        my_login_btn.click()
        #inpu = self.driver.find_element_by_ios_predicate("type='XCUIElementTypeTextField'")
        inpu = get_element(self.driver,'login_input')
        inpu.clear()
        inpu.send_keys(self.number)

        #psw = self.driver.find_element_by_ios_predicate('type="XCUIElementTypeSecureTextField"')
        psw= get_element(self.driver,'login_psw')
        psw.send_keys(self.psw)

        #login = self.driver.find_element_by_ios_predicate('type="XCUIElementTypeButton" and name="登录"')
        login = get_element(self.driver,'login_btn')
        login.click()

        jump = get_element(self.driver, 'jump_btn')
        jump.click()

        recharge(self.driver, num='1000', msg_verify='111111', psw=self.one_psw)

        ios_withdraw_all(self.driver,self.one_psw)

#提现页面
        '''
        withdraw_btn = get_element(self.driver,'withdraw_btn')
        withdraw_btn.click()

        withdraw_all = get_element(self.driver,'withdraw_all')
        withdraw_all.click()

        withdraw_one_btn = get_element(self.driver,'withdraw_one_btn')
        withdraw_one_btn.click()

        withdraw_psw_input = get_element(self.driver,'withdraw_psw_input')
        withdraw_psw_input.send_keys(self.one_psw)
        withdraw_sure = get_element(self.driver,'withdraw_sure')
        withdraw_sure.click()
        withdraw_back = get_element(self.driver,'withdraw_back')
        withdraw_back.click()

        withdraw_mine = get_element(self.driver,'withdraw_mine')
        withdraw_mine.click()
'''


#        recharge(self.driver,num='1000',msg_verify='111111',psw=self.one_psw)





        '''
        l = get_massage.get_size(self.driver)
        x1 = int(l[0] * 0.1)
        y1 = int(l[1] * 0.95)
        self.driver.tap([(x1, y1)], 200)
        '''


def runn():
        log = myLog.Log()
        logger = log.get_logger()
        reportpath = os.path.join(rootDir, "result", str(datetime.now().strftime("%Y%m%d%H%M%S")), "report1.html")
        with open(reportpath, 'wb') as fp:
            try:
                suit = unittest.TestSuite()
                suit.addTest(LoginCase('test_login'))
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
    SS = LoginCase()
    SS.run()
