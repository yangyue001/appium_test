from time import sleep
from appium import webdriver
import os



app = os.path.abspath('/Users/yangyue/Library/Developer/Xcode/DerivedData/ios-cnzthtppmgfufodekufbnedifnox/Build/Products/Debug-iphonesimulator/ios.app')
driver = webdriver.Remote(
            command_executor='http://127.0.0.1:4723/wd/hub',
            desired_capabilities={
                'app': app,
                'platformName': 'iOS',
                'platformVersion': '12.1',
                'deviceName': 'iPhone 6'
            })

#获取屏幕尺寸
def get_size():
    x=driver.get_window_size()['width']
    y=driver.get_window_size()['height']
    return x,y

#显示屏幕尺寸（width,height）
l=get_size()
print(l)

#向左滑动
def swipeLeft():
    l=get_size()
    x1=int(l[0]*0.9)
    y1=int(l[1]*0.5)
    x2=int(l[0]*0.1)
    driver.swipe(x1,y1,x2,y1,1000)


def test_allow():
    butt = driver.find_element_by_xpath('//XCUIElementTypeButton[@name="Allow"]')
    butt.click()

if __name__ == '__main__':

    test_allow()
    for i in range(3):
        swipeLeft()
        sleep(0.5)

    #driver.find_element_by_id('').click()