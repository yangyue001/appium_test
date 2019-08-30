import unittest
from Action.common_bussy import *
import paramunittest
from Util.excel_read import *

login_xls = parseExcel('lantouzi_unit_case.xlsx','login').get_xls()


@paramunittest.parametrized(*login_xls)
class loginTest(unittest.TestCase):

    def setParameters(self,case_name,name,psw):
        self.case_name = str(case_name)
        self.name = str(name)
        self.psw =str(psw)


    def setUp(self):
        self.dr = webdriver.Chrome()
        self.baseurl = 'http://dev.lantouzi.com'
        #self.WebDriverWait(self.dr,10,0.2)
        self.dr.maximize_window()
        self.lg = LoginPage(self.dr)
    def test_login011(self):
        self.dr.get(self.baseurl+r'/login')
        self.lg.get_frame().click()
        self.lg.get_name().send_keys(self.name)
        self.lg.get_userpsw().send_keys(self.psw)
        self.lg.get_loginbutton().click()
    '''
    def test_login001(self):
        self.dr.get(self.baseurl)
        self.lg.get_in_button().click()
        self.lg.get_frame().click()
        self.lg.get_name().send_keys(self.name)
        self.lg.get_userpsw().send_keys(self.psw)
        self.lg.get_loginbutton().click()
'''
    def tearDown(self):
        logout_bussy(self.dr)
        time.sleep(2)
        self.dr.quit()


if __name__ =='__main__':
    suit = unittest.TextTestRunner()
    suit.addTests(unittest.TestLoader().loadTestsFromTestCase('loginTest'))
    with open('UnittestTextReport.txt', 'a') as f:

        runner = unittest.TestRunner(stream = f , verbosity=2)
        runner.run(suit)