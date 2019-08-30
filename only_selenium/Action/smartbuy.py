# -*- coding:utf-8 -*-

from PageObject.buy_smartbid import *
from Action.login import *
from selenium import webdriver

def smart_buy(drvier,buy_amnout,buy_psw):

    time.sleep(2)
    bs = Buy_smart(drvier)
    bs.get_frame().click() #切换到智选页面
    bs.get_joinsmart().click()#选择一个智选服务
    bs.get_smartamout().send_keys(buy_amnout)
    rs = bs.get_remaining().text  # 获余额金额
    rs1 = rs.split('元')
    rs2 = rs1[0].split(',')
    rs3 = ''
    for i in rs2:
        rs3= rs3+i
    smart_amount = float(rs3)
    print(smart_amount)

    bs.get_amount_submit().click()#点击马上加入
    if smart_amount >=float(buy_amnout): #余额金额与输入金额比较，如果余额>
        bs.get_buy_now().click()
        time.sleep(9)
        title1 = drvier.title
        if title1 == r'一帐通资金划转':
            print('ssss1')
            bs.get_one_transfer().send_keys(buy_psw)#输入一帐通密码
            bs.get_greet().click()#同一风险协议
            bs.get_one_nextButton().click()#点击划转
        elif title1 == u'一账通资金划转':
            print('ssss2')
            bs.get_one_transfer().send_keys(buy_psw)  # 输入一帐通密码
            bs.get_greet().click()  # 同一风险协议
            bs.get_one_nextButton().click()  # 点击划转
        elif title1 == '一账通资金划转':
            print('sss3')
            bs.get_one_transfer().send_keys(buy_psw)  # 输入一帐通密码
            bs.get_greet().click()  # 同一风险协议
            bs.get_one_nextButton().click()  # 点击划转
        elif title1 == "一账通资金划转":
            print('ssss7')
            bs.get_one_transfer().send_keys(buy_psw)  # 输入一帐通密码
            bs.get_greet().click()  # 同一风险协议
            bs.get_one_nextButton().click()  # 点击划转
        else:
            print('false')


    else:
        bs.get_recharge().click()#余额不足就充值
        bs.get_i_know().click()#点击我知道了
        bs.get_phoneV().send_keys('111111')
        bs.get_passwd().send_keys(buy_psw)#输入密码
        bs.get_isAgreeReg().click()#勾选协议
        drvier.switch_to.default_content()
        time.sleep(1)
        nb = bs.get_renextButton()
        nb.click()#点击充值确定




