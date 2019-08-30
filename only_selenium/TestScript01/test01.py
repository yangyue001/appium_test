from selenium import webdriver
import time
import requests
from Util.ParsePageObjectRepository import *
from Util.ObjectMap import *
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementNotVisibleException
from datetime import datetime
from time import sleep

def test_sure():

    url = 'http://www.baidu.com'
    dr = webdriver.Chrome()
    dr.get(url)
    try:
        input01 = dr.find_element_by_id('kw')
        input01.send_keys('selenium')
        sure = dr.find_element_by_id('submit')
        sure.click()
        sure01 = dr.find_element_by_id('su')
        sure01.click()
        sleep(1)


    except NoSuchElementException as no:
        filename = os.path.join(project_path,"Result",filestr+"error.png")
        dr.get_screenshot_as_file(filename)
        print("errorMessage:Unable to find element"+str(no))
        raise no
    except ElementNotVisibleException as ele:
        print("errorMessage:Unable to find element" + str(ele))
        raise ele
    except Exception as e:

        raise e
    finally:
        dr.quit()
test_sure()


