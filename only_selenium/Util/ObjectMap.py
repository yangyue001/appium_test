from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementNotVisibleException
from selenium.common.exceptions import TimeoutException
from datetime import datetime
from Util.ParsePageObjectRepository import project_path
import os

# 获取单个元素对象

filestr = str(datetime.now().strftime('%Y%m%d%H%M%S'))
filename = os.path.join(project_path, "Result", filestr + "error.png")
def getElement(driver, locateType, locateExpression):
    try:
        element = WebDriverWait(driver, 10).until(lambda x: x.find_element(by=locateType, value=locateExpression))
        return element

    except NoSuchElementException as no:

        driver.get_screenshot_as_file(filename)
        print("errorMessage:Unable to find element"+str(no))
        raise no
    except ElementNotVisibleException as ele:
        print("errorMessage:Unable to find element" + str(ele))
        raise ele
    except TimeoutException as timeout:
        driver.get_screenshot_as_file(filename)
        raise timeout

    except Exception as e:

        raise e


# 获取多个相同页面元素对象，以list返回

def getElements(driver, locateType, locatorExpression):
    try:

        elements = WebDriverWait(driver, 5).until(lambda x: x.find_elements(by=locateType, value=locatorExpression))

        return elements

    except Exception as e:

        raise e