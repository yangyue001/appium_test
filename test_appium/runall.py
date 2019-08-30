import os
from Common_tools.myLog import *
from Conf.read_config import *
from Common_tools.common01 import *
import unittest
from Common_tools import HTMLTestRunner
class AllRun:
    def __init__(self):
        global log,logger,resultPath

        log = MyLog.get_log()
        logger = log.get_logger()
        self.caseList = []
        resultPath = os.path.join(rootDir, 'result', str(datetime.now().strftime("%Y%m%d%H%M%S")),'report.html')


        self.caseListFile = os.path.join(prodir,'Conf',"case_list.txt")
        self.caseFile = os.path.join(rootDir, "testCase")

    def set_case_list(self):
        """
        set case list
        :return:
        """
        with open(self.caseListFile) as fb1:

            for value in fb1.readlines():
                data = str(value)
                if data != '' and not data.startswith('#'):
                    self.caseList.append(data.replace("\n",""))


    def set_case_suite(self):
        """
        set case suite
        :return:
        """
        self.set_case_list()
        test_suite = unittest.TestSuite()
        suite_module = []

        for case in self.caseList:
             #找到caselist.txt里的文件名，取各路径如（user/testUpdatePassword）的最后一个值（testUpdatePassword）
            case_name = case.split("/")[-1]
            print(case_name+".py")              #打印加上.py
            py_case_name = str(case_name +'.py')
            discover = unittest.defaultTestLoader.discover(self.caseFile, pattern=py_case_name, top_level_dir=None)

            '''
            所述TestLoader类被用来创建类和模块的测试套件。通常不需要创建该类的实例。
            unittest框架提供了一个可以共享的实例unittest.defaultTestLoader
            '''
            suite_module.append(discover)

        if len(suite_module) > 0:

            for suite in suite_module:
                for test_name in suite:
                    test_suite.addTest(test_name)
        else:
            return None

        return test_suite




    



    def run(self):
        """
        run test
        :return:
        """
        fp = open(resultPath, 'wb')
        try:
            suit = self.set_case_suite()

            if suit is not None:
                logger.info("********TEST START********")
                # fp = open(resultPath, 'wb')
                runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='Test Report', description='Test Description')
                runner.run(suit)   #这里报错了
            else:
                logger.info("Have no case to test.")
        except Exception as ex:
            logger.error(str(ex))
        finally:
            logger.info("*********TEST END*********")
            fp.close()
            # send test report by email



if __name__ == '__main__':
    obj = AllRun()
    obj.run()