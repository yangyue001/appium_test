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
class An_SmartBid_Buy_Huazhuan(unittest.TestCase):
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
            '/Users/yangyue/Library/Developer/Xcode/DerivedData/ios-cnzthtppmgfufodekufbnedifnox/Build/Products/Debug-iphonesimulator/ios.app')
        cls.driver = webdriver.Remote(
            command_executor='http://127.0.0.1:4723/wd/hub',
            desired_capabilities={
                'app': app,
                'platformName': 'iOS',
                'platformVersion': '12.1',
                # "noReset":True,
                'deviceName': 'iPhone 6'
            })
        #butt = cls.driver.find_element_by_ios_predicate('type="XCUIElementTypeButton" and name="Allow"')
        #butt = get_element(cls.driver,'right_allowed')
        cls.driver.implicitly_wait(10)

    def setUp(self):
        my_btn = get_element(self.driver, 'my_btn')
        my_btn.click()
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
        #login = get_element(self.driver, 'login_btn')
        #login.click()
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


        for i in range(4):
            my_btn = get_element(self.driver, 'my_btn')
            if my_btn:
                my_btn.click()
                break
            else:
                self.driver.back()


        setting = get_element(self.driver,'setting')
        setting.click()
        logout_btn = get_element(self.driver,'logout_btn')
        logout_btn.click()
        self.driver.quit()