from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Chrome()
driver.get(url='https://login.taobao.com')
J_Quick2Static = driver.find_element_by_id('J_Quick2Static')
J_Quick2Static.click()
TPL_username_1 = driver.find_element_by_id('TPL_username_1')
TPL_password_1 = driver.find_element_by_id('TPL_password_1')

TPL_username_1.send_keys('测试账号1')
TPL_password_1.send_keys('1234567')
time.sleep(1)

captcha = driver.find_elements_by_xpath('//div[@id="nocaptcha" and @style]')

if captcha:
    button = driver.find_element_by_id('nc_1_n1z')
    ActionChains(driver).click_and_hold(button).perform()
    ActionChains(driver).move_by_offset(258, 0).perform()
    ActionChains(driver).release(button).perform()
    login_button = driver.find_element_by_id('J_SubmitStatic')
    login_button.click()
    time.sleep(5)
else:
    print('不需要验证码')
    login_button = driver.find_element_by_id('J_SubmitStatic')
    login_button.click()
    time.sleep(5)
driver.quit()
