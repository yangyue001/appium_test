# -*- coding:utf-8 -*

import logging

import logging.config
from Util.ParsePageObjectRepository import *
from datetime import datetime




proDir = project_path

resultPath = os.path.join(proDir, "Result")

if not os.path.exists(resultPath):
    os.mkdir(resultPath)

logPath = os.path.join(resultPath, str(datetime.now().strftime("%Y%m%d%H%M%S")))
logPath1 = os.path.join(logPath,'output.log')

# 读取日志的配置文件

logging.config.fileConfig(project_path + r"/Conf/logger.conf")

# 选择一个日志格式

logger = logging.getLogger("example02")


def error(message):
    # 打印debug级别的信息

    logger.error(message)


def info(message):
    # 打印info级别的信息

    logger.info(message)


def warning(message):
    # 打印warning级别的信息

    logger.warning(message)


if __name__ == "__main__":
    # 测试代码

    info("hi")

    error("world!")

    warning("gloryroad!")





'''
if title1 == "一账通资金划转":
    one_transfer = wait.until(lambda x: x.find_element_by_id('password'))
    one_transfer.send_keys('123456')
    time.sleep(1)
    gree = wait.until(lambda x: x.find_element_by_css_selector('.icon-check>img'))
    gree.click()
    nextButton = wait.until(lambda x: x.find_element_by_css_selector("#nextButton"))
    nextButton.click()
else:
    print("false")

else:
recharge = wait.until(lambda x: x.find_element_by_css_selector('.recharge-summary >button'))
recharge.click()
passwd = wait.until(lambda x: x.find_element_by_id('password'))
passwd.send_keys('123456')
isAgreeReg = wait.until(lambda x: x.find_element_by_id('isAgreeReg'))
isAgreeReg.click()
nextButton = wait.until(lambda x: x.find_element_by_id('nextButton'))
nextButton.click()
except TimeoutException as e:
print("timeout", e)
except NoSuchElementException as e:
print("nosuch ", e)
except Exception as e:
print("other e", e)
 '''