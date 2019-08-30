'''import pyssdb
import os
ssdb = pyssdb.Client('172.26.0.182', 8888)
try:

    lst = ['safe_act|172.26.0.178|login_ip','safe_act|172.26.0.178|login-fail','safe_act|172.26.0.178|login_ok']

    for i in lst:
        ssdb.set(i,'0')
finally:
    ssdb.disconnect()
'''
from datetime import datetime
import unittest
import paramunittest
from Common_tools.common01 import *
from Conf.read_config import *
from Common_tools import HTMLTestRunner
patho  = get_xls_nrows('ios_test_case.xlsx','loginssdb')


@paramunittest.parametrized(*patho)
class trySetup(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('setup class')


    def setParameters(self,case_name,ssdb_name):
        self.case_name = case_name
        self.ssdb_name = ssdb_name
        

    def setUp(self):
        print('set up 01')

    def tearDown(self):
        print('tear down')

    '''@classmethod
    def tearDownClass(cls):
        print('tear down class')
    '''

    def test_case_01(self):
        print('test 01')
        print(self.case_name)

    def test_case_02(self):
        print('test02')
        print(self.ssdb_name)


'''
if __name__ == '__main__':
    suit = unittest.TestSuite()
    suit.addTest(trySetup('test_case_02'))
    suit.addTest(trySetup('test_case_01'))
    runner = unittest.TextTestRunner()
    runner.run(suit)
'''

if __name__ == '__main__':
    reportpath = os.path.join(rootDir,'result',str(datetime.now().strftime("%Y%m%d%H%M%S")))
    if not os.path.exists(reportpath):
        os.mkdir(reportpath)
    oopath = os.path.join(reportpath,"re01.html")
    testdir = './'
    discover = unittest.defaultTestLoader.discover(start_dir=testdir,pattern='test_tyr.py')
    with open(oopath,'wb') as fb:
        runner = HTMLTestRunner.HTMLTestRunner(stream=fb)
        runner.run(discover)



'''from Common_tools.common01 import get_xls_nrows
from Conf.read_config import *

def get_element(value):
    lis = get_xls_nrows('ios_test_case.xlsx','iOS_local_path')
    for i in lis:
        if i[0]==value:
            if i[1]=='accessibility_id':
                print('accessibility_id')
                print(i[2])
            elif i[1] == 'xpath':
                print('xpath')
                print(i[2])
            elif i[1]=='ios_predicate':
                print('ios_predicate')
                print(i[2])

        else:
            continue


get_element('into_hegui')

'''
