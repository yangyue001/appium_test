from appium import webdriver
from time import sleep

def android_login():
    driver = webdriver.Remote(
        command_executor='http://127.0.0.1:4723/wd/hub',

        desired_capabilities = {
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

    driver.implicitly_wait(10)
    sleep(5)
    try:

        smarbid_icon = driver.find_element_by_android_uiautomator('new UiSelector().text("智选服务")')
        smarbid_icon.click()
        sleep(1)
        smart_in = driver.find_element_by_id('com.lantouzi.app.dev:id/lanren_project_rate')
        smart_in.click()

        smart_in_detail = driver.find_element_by_android_uiautomator('new UiSelector().text("马上加入")')
        smart_in_detail.click()


        #logbtn = driver.find_element_by_id('com.lantouzi.app.dev:id/login_btn')

        #my = driver.find_element_by_id('com.lantouzi.app.dev:id/home_tab').find_elements_by_class_name('android.widget.LinearLayout')[3]

        #my = driver.find_element_by_css_selector('#com.lantouzi.app.dev:id/home_tab > android.widget.LinearLayout > android.widget.LinearLayout:nth-child(3) > android.widget.ImageView')
        #my.click()


        #log = driver.find_element_by_android_uiautomator('new UiSelector().text("登录去赚钱")')
        #log.click()
        #lof = driver.find_element_by_css_selector('#com.lantouzi.app.dev:id/login_btn')
        #lof.click()
    except BaseException as e :
        print('error:'+str(e))
    finally:
        driver.quit()


android_login()