"""
Simple iOS tests, showing accessing elements and getting/setting text from them.
"""
import unittest
import os
from random import randint
from appium import webdriver
from time import sleep
from Common_tools.test_ios_get_elements import *
from pykeyboard import PyKeyboard
from selenium.webdriver.common.keys import Keys

class SimpleIOSTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # set up appium
        app = os.path.abspath('/Users/yangyue/Library/Developer/Xcode/DerivedData/ios-cnzthtppmgfufodekufbnedifnox/Build/Products/Debug-iphonesimulator/ios.app')
        cls.driver = webdriver.Remote(
            command_executor='http://127.0.0.1:4723/wd/hub',
            desired_capabilities={
                'app': app,
                'platformName': 'iOS',
                'platformVersion': '12.1',
                #"noReset":True,
                'deviceName': 'iPhone 6'
            })
        cls.driver.implicitly_wait(10)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def _populate(self):
        # populate text fields with two random numbers
        els = [self.driver.find_element_by_accessibility_id('TextField1'),
               self.driver.find_element_by_accessibility_id('TextField2')]

        self._sum = 0
        for i in range(2):
            rnd = randint(0, 10)
            els[i].send_keys(rnd)
            self._sum += rnd

    '''
    def test_ui_computation(self):
        # populate text fields with values
        self._populate()

        # trigger computation by using the button
        self.driver.find_element_by_accessibility_id('ComputeSumButton').click()

        # is sum equal ?
        # sauce does not handle class name, so get fourth element
        sum = self.driver.find_element_by_accessibility_id('Answer').text
        self.assertEqual(int(sum), self._sum)

    def test_scroll(self):
        els = self.driver.find_elements_by_class_name('XCUIElementTypeButton')
        els[5].click()

        sleep(1)
        try:
            el = self.driver.find_element_by_accessibility_id('Allow')
            el.click()
            sleep(1)
        except:
            pass

        el = self.driver.find_element_by_xpath('//XCUIElementTypeApplication[@name="TestApp"]/XCUIElementTypeOther/XCUIElementTypeOther')

        location = el.location
        self.driver.swipe(start_x=location['x'], start_y=location['y'], end_x=0.5, end_y=location['y'], duration=800)
    
    def test_myexample01(self):
        try:
            el01 = self.driver.find_element_by_name('Check calendar authorized')
            el01.click()
            sleep(2)
        except BaseException as e :
            print(e)
            
        def test_allow(self):
        butt = self.driver.find_element_by_ios_predicate('type="XCUIElementTypeButton" and name="Allow"')
        butt.click()
        sleep(2)
    '''
    def test_allow(self):

        s = get_element(self.driver,'right_allowed')
        s.click()

# 获取屏幕尺寸
    def get_size(self):
        x = self.driver.get_window_size()['width']
        y = self.driver.get_window_size()['height']
        print('\n',x,y)
        return x, y

# 显示屏幕尺寸（width,height）

        # 向左滑动
    def swipeLeft(self):
        l = self.get_size()
        x1 = int(l[0] * 0.9)
        y1 = int(l[1] * 0.5)
        x2 = int(l[0] * 0.1)
        self.driver.swipe(x1, y1, x2, y1, 1000)

    def swipeUp(self):
        l = self.get_size()
        x1 = int(l[0]*0.5)
        y1 = int(l[1]*0.5)
        y2 = int(l[1]*0.1)
        self.driver.swipe(x1, y1, x1, y2, 500)

    def test_arun(self):

        for i in range(3):
            self.swipeLeft()
            sleep(1)

    def test_click_in(self):
        self.driver.find_element_by_accessibility_id('intro btn').click()

    def test_login_btn(self):
        self.driver.find_element_by_ios_predicate('type="XCUIElementTypeButton" and name=" 登录去赚钱"').click()

    def test_login_input(self):
        # login01=self.driver.find_element_by_xpath('/UIWindow/UITransitionView/UILayoutContainerView/UIViewControllerWrapperView/UIView/UIScrollView/UCTextField')
        #login01.send_keys('17300013251')
        inpu = self.driver.find_element_by_ios_predicate("type='XCUIElementTypeTextField'")

        #k = PyKeyboard()
        #k.press_keys(['Command','UP_ARROW_KEY','k'])

        #k.release_key(['Command','Up','k'])

        inpu.send_keys('17300013251')
        sleep(1)
        psw = self.driver.find_element_by_ios_predicate('type="XCUIElementTypeSecureTextField"')
        psw.send_keys('11111111')
        sleep(1)
        login = self.driver.find_element_by_ios_predicate('type="XCUIElementTypeButton" and name="登录"')
        login.click()
        sleep(2)
        jump = self.driver.find_element_by_ios_predicate('type="XCUIElementTypeButton" and name="跳过"')
        jump.click()
        sleep(2)
        l = self.get_size()
        x1 = int(l[0] * 0.1)
        y1 = int(l[1] * 0.95)

        self.driver.tap([(x1, y1)], 200)
        sleep(2)
        sleep(3)

    def test_smarbid(self):
        sleep(1)
        smarbidbut = self.driver.find_element_by_accessibility_id('智选服务')
        smarbidbut.click()
        sleep(1)
        l = self.get_size()
        x1 = int(l[0] * 0.1)
        y1 = int(l[1] * 0.95)
        self.driver.tap([(x1,y1)],200)
        sleep(2)
        self.driver.find_element_by_accessibility_id('马上加入').click()
        sleep(3)
        inptm = self.driver.find_element_by_ios_predicate('type="XCUIElementTypeTextField"')
        inptm.click()

        self.driver.find_element_by_accessibility_id('1').click()
        sleep(1)
        for i in range(3):

            self.driver.find_element_by_accessibility_id('0').click()
            sleep(1)
        self.driver.find_element_by_accessibility_id('确定').click()

        sleep(2)
        self.driver.find_element_by_accessibility_id('马上加入').click()
        sleep(2)
        self.driver.find_element_by_accessibility_id('确认').click()
        self.driver.find_element_by_xpath()
        sleep(4)
        self.repay()


    def repay(self):
        spwd = self.driver.find_element_by_ios_predicate('type="XCUIElementTypeSecureTextField"')
        spwd.send_keys('123456')

        sleep(1)
        self.swipeUp()
        self.driver.find_element_by_accessibility_id('Done').click()
        sleep(1)
        self.driver.find_element_by_accessibility_id('我同意').click()
        sleep(1)
        self.driver.find_element_by_accessibility_id('确认协议并划转').click()
        sleep(1)
        self.driver.find_element_by_accessibility_id('查看订单').click()
        sleep(1)
        self.driver.find_element_by_accessibility_id('wapBack').click()
        sleep(1)
        self.driver.find_element_by_accessibility_id('wapBack').click()
        sleep(1)




if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(SimpleIOSTests)
    unittest.TextTestRunner(verbosity=2).run(suite)