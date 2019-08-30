# coding:utf-8
import logging
import logging.config
from Util.ParsePageObjectRepository import *
from datetime import datetime
import threading



class Log:
    def __init__(self):
        # global logPath, resultPath, proDir
        self.proDir = project_path
        self.resultPath = os.path.join(self.proDir, "Result")
        if not os.path.exists(self.resultPath):
            os.mkdir(self.resultPath)
        logPath = os.path.join(self.resultPath, str(datetime.now().strftime("%Y%m%d%H%M%S"))) #目录名称为时间
        if not os.path.exists(logPath):
            os.mkdir(logPath)
            #/Users/yangyue/PycharmProjects/only_selenium/Action/excel_read.py

        self.logger = logging.getLogger()  #初始化日志类
        self.logger.setLevel(logging.INFO)
        # defined handler
        # 2、创建一个handler, log名称为output.log
        self.logPath1 = os.path.join(logPath, 'output.log')
        handler = logging.FileHandler(self.logPath1)
        # 4、给handler添加formatter
        formater = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        # 4、给handler添加formatter
        handler.setFormatter(formater)
        self.logger.addHandler(handler)





    def get_logger(self):

        return self.logger

    def error(self,message):

        # 打印debug级别的信息

        self.logger.error(message)

    def info(self,message):
            # 打印info级别的信息

        self.logger.info(message)

    def debug(self,message):

        self.logger.debug(message)




class MyLog:
    log = None
    mutex = threading.Lock() #锁

    def __init__(self):
        pass

    @staticmethod
    def get_log():

        if MyLog.log is None:
            MyLog.mutex.acquire()   #枷锁
            MyLog.log = Log()
            MyLog.mutex.release()   #释放锁

        return MyLog.log


if __name__ =='__main__':
    log = MyLog.get_log()
    logger = log.get_logger()
    logger.info('tyuio')


    '''
        
        # 1、创建一个logger
        self.logger = logging.getLogger()   #初始化日志类
        self.logger.setLevel(logging.INFO)  #默认日志级别

        # defined handler
        # 2、创建一个handler, log名称为output.log
        handler = logging.FileHandler(os.path.join(logPath, "output.log"))
        # defined formatter
        # 3、定义handler的输出格式（formatter）
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        # 4、给handler添加formatter
        handler.setFormatter(formatter)
        # 5、给logger添加handler
        self.logger.addHandler(handler)
        '''