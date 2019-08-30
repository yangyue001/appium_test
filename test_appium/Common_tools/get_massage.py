from time import sleep
from Common_tools.test_ios_get_elements import *

def get_size(driver):
    x = driver.get_window_size()['width']
    y = driver.get_window_size()['height']
    print('\n', x, y)
    return x, y


def swipeLeft(driver):
    l = get_size(driver)
    x1 = int(l[0] * 0.9)
    y1 = int(l[1] * 0.5)
    x2 = int(l[0] * 0.1)
    driver.swipe(x1, y1, x2, y1, 1000)

def swipeUp(driver):
    l = get_size(driver)
    x1 = int(l[0]*0.5)
    y1 = int(l[1]*0.5)
    y2 = int(l[1]*0.1)
    driver.swipe(x1, y1, x1, y2, 500)
def click_in(driver):
    hegui = get_element(driver,'into_hegui')
    hegui.click()


def page_arun(driver):
    for i in range(3):
        swipeLeft(driver)
        sleep(1)
