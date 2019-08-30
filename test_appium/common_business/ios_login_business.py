from Common_tools.test_ios_get_elements import get_element

def ios_login(driver,number,psw):
    my_btn = get_element(driver, 'my_btn')
    my_btn.click()
    # self.driver.find_element_by_ios_predicate('type="XCUIElementTypeButton" and name=" 登录去赚钱"').click()
    my_login_btn = get_element(driver, 'my_login_btn')
    my_login_btn.click()
    # inpu = self.driver.find_element_by_ios_predicate("type='XCUIElementTypeTextField'")
    inpu = get_element(driver, 'login_input')
    inpu.clear()
    inpu.send_keys(number)

    # psw = self.driver.find_element_by_ios_predicate('type="XCUIElementTypeSecureTextField"')
    psw = get_element(driver, 'login_psw')
    psw.send_keys(psw)

    # login = self.driver.find_element_by_ios_predicate('type="XCUIElementTypeButton" and name="登录"')
    login = get_element(driver, 'login_btn')
    login.click()

    jump = get_element(driver, 'jump_btn')
    jump.click()