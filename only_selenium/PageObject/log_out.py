from PageObject.LoginPage import *
from selenium import webdriver
from Action.login import *


class logout:
    def __init__(self,dr):
        self.dr = dr
        self.wait = WebDriverWait(self.dr,10,0.2)
        self.parse_cofig_file = parsepageobjectrepository()
        self.logout_items = self.parse_cofig_file.getItemSection('logout')
    def get_logout_button(self):
        locateType, locateExpression = self.logout_items['logout.button'].split('?')
        logout_button = getElement(self.dr, locateType, locateExpression)
        return logout_button

if __name__=='__main__':

    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get('http://dev.lantouzi.com/login')
    login(driver,'17300013245','11111111')
    time.sleep(2)
    lout = logout(driver)

    lout.get_logout_button().click()
    time.sleep(2)
    driver.quit()

