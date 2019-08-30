from Common_tools.common01 import get_xls_nrows
from Conf.read_config import *

def get_element(driver,value):
    lis = get_xls_nrows('android_test_case.xlsx', 'android_local_path')
    for i in lis:
        if i[0] == value:

            if i[1] =='id':
                elm = driver.find_element_by_id(i[2])
            elif i[1]=='css':
                elm = driver.find_element_by_css_selector(i[2])
            elif i[1] =='class':
                elm = driver.find_element_by_class_name(i[2])
            elif i[1] == 'android_uiautomator':
                elm = driver.find_element_by_android_uiautomator(i[2])
            elif i[1] == 'xpath':
                elm = driver.find_element_by_xpath(i[2])

        else:
            continue
        return elm


def get_elements(driver,value):
    lis = get_xls_nrows('android_test_case.xlsx', 'android_local_path')
    for i in lis:
        if i[0] == value:

            if i[1] =='id':
                elms = driver.find_elements_by_id(i[2])
            elif i[1]=='css':
                elms = driver.find_elements_by_css_selector(i[2])
            elif i[1] =='class':
                elms = driver.find_elements_by_class_name(i[2])
            elif i[1] == 'android_uiautomator':
                elms = driver.find_elements_by_android_uiautomator(i[2])

            elif i[1] == 'xpath':
                elms = driver.find_elements_by_xpath(i[2])
            else:
                continue
            return elms
