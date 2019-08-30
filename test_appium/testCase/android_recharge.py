import unittest
from appium import webdriver
from time import sleep
from Common_tools import get_massage
from Common_tools.test_android_get_elements import *
from Common_tools import myLog
import paramunittest
from Common_tools.common01 import *


login_xls = get_xls_nrows('android_test_case.xlsx','login')

@paramunittest.parametrized(*login_xls)
class Recharge_case(unittest.TestCase):

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
        cls.logger = cls.log.get_logger()
        # set up appium
        cls.driver = webdriver.Remote(
            command_executor='http://127.0.0.1:4723/wd/hub',

            desired_capabilities={
                "platformName": "Android",
                "platformVersion": "7.1.1",
                "deviceName": "Pixel 2 XL API 25",
                "appPackage": "com.lantouzi.app.dev",
                "appActivity": "com.lantouzi.app.ui.EnterActivity",
                "app": "/Users/yangyue/Documents/各测试用例及需求/app3.17.0/qa包/lantouzi_v3.17.0_2019-04-22_ltest_qa.apk",
                "noReset": True,
                "unicodeKeyboard": True,
                "newCommandTimeout": 600,
                "resetKeyboard": True,
                "autoGrantPermission": True,
                "udid": "emulator-5554",
                "uiautomator": "XCUITest"
            })
        #butt = cls.driver.find_element_by_ios_predicate('type="XCUIElementTypeButton" and name="Allow"')
        #butt = get_element(cls.driver,'right_allowed')
        cls.driver.implicitly_wait(10)

    def setUp(self):
        my_btn = get_element(self.driver, 'my_btn')
        sleep(2)
        ls= get_elements(my_btn, 'my_btn_01')[3]
        ls.click()
        # self.driver.find_element_by_ios_predicate('type="XCUIElementTypeButton" and name=" 登录去赚钱"').click()
        my_login_btn = get_element(self.driver, 'my_login_btn')
        my_login_btn.click()
        # inpu = self.driver.find_element_by_ios_predicate("type='XCUIElementTypeTextField'")
        inpu = get_element(self.driver, 'login_input')
        inpu.clear()
        inpu.send_keys(self.number)
        sleep(1)
        # psw = self.driver.find_element_by_ios_predicate('type="XCUIElementTypeSecureTextField"')
        psw = get_element(self.driver, 'login_psw')
        psw.send_keys(self.psw)
        sleep(1)
        # login = self.driver.find_element_by_ios_predicate('type="XCUIElementTypeButton" and name="登录"')
        login = get_element(self.driver, 'login_btn')
        login.click()
        sleep(1)
        # jump = self.driver.find_element_by_ios_predicate('type="XCUIElementTypeButton" and name="跳过"')
        jump = get_element(self.driver, 'jump_btn')
        jump.click()

        sleep(1)
        l = get_massage.get_size(self.driver)
        x1 = int(l[0] * 0.1)
        y1 = int(l[1] * 0.95)
        self.driver.tap([(x1, y1)], 200)
        sleep(3)



    def tearDown(self):
        #print('w')
        my_btn = get_element(self.driver, 'my_btn')
        my_btn.click()

        setting = get_element(self.driver,'setting')
        setting.click()
        logout_btn = get_element(self.driver,'logout_btn')
        logout_btn.click()
        self.driver.quit()

    def test_recharge(self):
        my_btn = get_element(self.driver, 'my_btn')
        sleep(2)
        ls = get_elements(my_btn, 'my_btn_01')[3]
        ls.click()


        recharge_btn = get_element(self.driver,'recharge_btn')
        recharge_btn.click()
        sleep(1)
        recharge_inp = get_element(self.driver,'recharge_inp')
        recharge_inp.send_keys('10')
        recharge_imd = get_element(self.driver,'recharge_imd')
        recharge_imd.click()
        sleep(1)
        recharge_iknow = get_element(self.driver,'recharge_iknow')
        recharge_iknow.click()
        sleep(1)
        recharge_v =get_element(self.driver,'recharge_v')
        recharge_v.send_keys('123456')
        sleep(1)
        recharge_psw = get_element(self.driver,'recharge_psw')
        recharge_psw.send_keys('123456')
        sleep(1)

        recharge_agree = get_element(self.driver,'recharge_agree')
        recharge_agree01 = get_elements(recharge_agree,'recharge_agree01')[7]
        recharge_agree02 = get_element(recharge_agree01,'recharge_agree02')
        recharge_agree03 = get_element(recharge_agree02,'recharge_agree03')
        recharge_agree03.click()
        

        #recharge_agree04 = get_element(self.driver,'recharge_agree04')
        #recharge_agree04.click()
        sleep(1)
        recharge_sure = get_element(self.driver,'recharge_sure')
        recharge_sure.click()
        sleep(1)
        recharge_back = get_element(self.driver,'recharge_back')
        recharge_back.click()
        sleep(1)
        self.driver.back()






if __name__ == '__main__':
    unittest.main()
