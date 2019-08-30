from Common_tools.common01 import get_xls_nrows
from Conf.read_config import *
from selenium.webdriver.support.ui import WebDriverWait

'''
def get_element(driver,value):
    lis = get_xls_nrows('ios_test_case.xlsx', 'iOS_local_path')
    for i in lis:
        if i[0] == value:
            if i[1] =='ios_predicate':
                elm = driver.find_element_by_ios_predicate(i[2])
            elif i[1]=='accessibility_id':
                elm = driver.find_element_by_accessibility_id(i[2])
            elif i[1] =='xpath':
                elm = driver.find_element_by_xpath(i[2])


        else:
            continue
        return elm
        
'''
def get_element(driver,value):
    lis = get_xls_nrows('ios_test_case.xlsx', 'iOS_local_path')
    for i in lis:
        if i[0] == value:
            if i[1] =='ios_predicate':
                elm = WebDriverWait(driver, 15).until(lambda x: x.find_element(by='-ios predicate string', value=i[2]))
            elif i[1]=='accessibility_id':
                elm = WebDriverWait(driver, 15).until(lambda x: x.find_element(by='accessibility id', value=i[2]))
            elif i[1] =='xpath':
                elm = WebDriverWait(driver, 15).until(lambda x: x.find_element(by= "xpath", value=i[2]))

        else:
            continue
        return elm




def get_elements(driver, value):
    lis = get_xls_nrows('ios_test_case.xlsx', 'iOS_local_path')
    for i in lis:
        if i[0] == value:

            if i[1] == 'ios_predicate':
                elms = WebDriverWait(driver, 15).until(lambda x: x.find_elements_by_ios_predicate(i[2]))
            elif i[1] == 'accessibility_id':
                elms = WebDriverWait(driver, 15).until(lambda x: x.find_elements_by_accessibility_id(i[2]))
            elif i[1] == 'xpath':
                elms = WebDriverWait(driver, 15).until(lambda x: x.find_elements_by_xpath(i[2]))
            else:
                continue
            return elms
    '''lis = get_xls_nrows('ios_test_case.xlsx','iOS_local_path')
    if lis[i][1] == 'ios_predicate':
        driver.find_element_by_ios_predicate(lis[i][2])
    elif lis[i][1] == 'ios_predicate':
        driver.find_element_by_ios_predicate(lis[i][2])
        '''
