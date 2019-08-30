from Common_tools.test_ios_get_elements import get_element

def recharge(driver,num,msg_verify,psw):

    recharge_btn = get_element(driver, 'recharge_btn')
    recharge_btn.click()

    recharge_input = get_element(driver, 'recharge_input')
    recharge_input.send_keys(num)

    recharge_immediately = get_element(driver, 'recharge_immediately')
    recharge_immediately.click()

    recharge_know = get_element(driver, 'recharge_know')
    recharge_know.click()

    recharge_msg_input = get_element(driver, 'recharge_msg_input')
    recharge_msg_input.send_keys(msg_verify)

    recharge_psw = get_element(driver, 'recharge_psw')
    recharge_psw.click()
    recharge_psw.send_keys(psw)

    recharge_agree = get_element(driver, 'recharge_agree')
    recharge_agree.click()

    recharge_sure = get_element(driver, 'recharge_sure')
    recharge_sure.click()

    recharge_back = get_element(driver, 'recharge_back')
    recharge_back.click()

    recharge_success_buy = get_element(driver, 'recharge_success_buy')
    recharge_success_buy.click()



