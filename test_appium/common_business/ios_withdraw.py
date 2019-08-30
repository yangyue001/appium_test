from Common_tools.test_ios_get_elements import get_element
import time
import  os


def time_format():
    current_time = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))
    return str(current_time)


def ios_withdraw_all(driver,one_psw):
    my_btn = get_element(driver, 'my_btn')
    my_btn.click()

    withdraw_btn = get_element(driver, 'withdraw_btn')
    withdraw_btn.click()

    withdraw_all = get_element(driver, 'withdraw_all')
    withdraw_all.click()

    withdraw_one_btn = get_element(driver, 'withdraw_one_btn')
    withdraw_one_btn.click()

    withdraw_psw_input = get_element(driver, 'withdraw_psw_input')
    withdraw_psw_input.send_keys(one_psw)
    withdraw_sure = get_element(driver, 'withdraw_sure')
    withdraw_sure.click()
    withdraw_back = get_element(driver, 'withdraw_back')
    withdraw_back.click()
    s = os.getcwd()

    driver.get_screenshot_as_file(str(s) + time_format() + ".png")

    withdraw_mine = get_element(driver,'withdraw_mine')
    withdraw_mine.click()