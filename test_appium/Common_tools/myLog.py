import logging
from datetime import datetime
from Conf import read_config
import os
import threading

class Log:
    def __init__(self):
        global loggPath,resultpath,proDir
        proDir = read_config.rootDir
        resultpath = os.path.join(proDir,'result')
        if not os.path.exists(resultpath):
            os.mkdir(resultpath)
        loggPath = os.path.join(resultpath,str(datetime.now().strftime("%Y%m%d%H%M%S")))
        if not os.path.exists(loggPath):
            os.mkdir(loggPath)
        #1.创建一个logger
        self.logger = logging.getLogger()
        #设置日志级别
        self.logger.setLevel(logging.INFO)
        #创建一个handler log名称为output
        handler  = logging.FileHandler(os.path.join(loggPath,'output.log'))
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)

        self.logger.addHandler(handler)

    def get_logger(self):
        """
        get logger
        :return:
        """
        return self.logger

class MyLog:
    log = None
    mutex = threading.Lock()
    def __init__(self):
        pass
    @staticmethod
    def get_log():
        if MyLog.log is None:
            MyLog.mutex.acquire() # 加锁
            MyLog.log = Log()
            MyLog.mutex.release() # 释放锁

        return MyLog.log

