# -*- coding: utf-8 -*-
import os
import unittest
from Util.Log import *
import HTMLTestRunner
from datetime import datetime
#import HtmlTestRunner
#from Util.Email_send import *
from Util import HTMLTestRuuner


class RunAll:
    def __init__(self):
        global log, logger
        test_dir = os.path.dirname(os.path.dirname(__file__))
        test_dir1 = test_dir + u'/TestScript'
        filename = str(datetime.now().strftime('%Y%m%d%H%M%S'))
        self.resultPath = os.path.join(test_dir1, filename + 'report.html')
        log  = MyLog().get_log()
        logger = log.get_logger()
        self.discover = unittest.defaultTestLoader.discover(test_dir1, pattern='log_test.py')

'''
    def run(self):
        with open(self.resultPath,'wb') as fb:
            try:
                logger.info("********TEST START********")
                runner = HTMLTestRunner.HTMLTestRunner(stream=fb, title='Test Report', description='Test Description')

                runner.run(self.discover)

            except Exception as ex:
                logger.error(str(ex))
            finally:
                logger.info("********TEST END********")

        #email = MyEmail.get_email(fb)
        #email.send_email()
'''








'''if __name__ =='__main__':

    rall = RunAll()
    rall.run()



#  unittest.main()
'''













if __name__ =='__main__':
    test_dir = os.path.dirname(os.path.dirname(__file__))
    print(test_dir)

    test_dir1 = test_dir + u'/TestScript'
    filename = str(datetime.now().strftime('%Y%m%d%H%M%S'))
    test_dir2 = os.path.join(test_dir, 'Result', filename + 'report.html')
    discover = unittest.defaultTestLoader.discover(test_dir1, pattern='*test.py')

    with open(test_dir2, 'wb') as fb:
        runner = HTMLTestRuuner.HTMLTestRunner(stream=fb,title='test_screen')
        runner.run(discover)




'''
if __name__ =='__main__':

    test_dir = os.path.dirname(os.path.dirname(__file__))
    print(test_dir)
    test_dir1 = test_dir+u'/TestScript'
    filename = str(datetime.now().strftime('%Y%m%d%H%M%S'))
    test_dir2 = os.path.join(test_dir,'Result',filename+'report.html')
    discover = unittest.defaultTestLoader.discover(test_dir1,pattern='*test.py')

    with open(test_dir2,'wb') as fb:

        runner = HTMLTestRunner.HTMLTestRunner(stream=fb, title='lantouzi report', description='Test Description')
        runner.run(discover)

'''


#    runner = unittest.TextTestRunner()
#    runner.run(discover)

#    suit.addTests(unittest.TestLoader().loadTestsFromTestCase('buysmart_test'))
#    with open('UnittestTextReport.txt', 'a') as f:
#        runner = unittest.TestRunner(stream = f , verbosity=2)
#        runner.run(suit)
