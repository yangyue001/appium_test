import unittest
import os
from random import randint
from appium import webdriver
from time import sleep
from pykeyboard import PyKeyboard
from selenium.webdriver.common.keys import Keys

class SimpleIOSTests1(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # set up appium
        app = os.path.abspath('/Users/yangyue/Library/Developer/Xcode/DerivedData/ios-cnzthtppmgfufodekufbnedifnox/Build/Products/Debug-iphonesimulator/ios.app')
        cls.driver = webdriver.Remote(
            command_executor='http://127.0.0.1:4723/wd/hub',
            desired_capabilities={
                'app': app,
                'platformName': 'iOS',
                'platformVersion': '10.0',
                'noReset':True,
                'deviceName': 'iPhone 6'
            })
        cls.driver.implicitly_wait(10)
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_one(self):

        self.driver.find_element_by_accessibility_id('马上加入').click()
        sleep(3)


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(SimpleIOSTests1)
    unittest.TextTestRunner(verbosity=2).run(suite)