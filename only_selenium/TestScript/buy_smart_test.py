# -*- coding: utf-8 -*-
import unittest
from Action.common_bussy import *
from PageObject.buy_smartbid import *
from Util.excel_read import*
import paramunittest

buysmart_xls = parseExcel('lantouzi_unit_case.xlsx','buysmart').get_xls()

#@paramunittest.parametrized(*buysmart_xls)
class buysmart_test(unittest.TestCase):
    '''
    def setParameters(self,case_name,amount,buy_psw,one_psw):
        self.case_name = str(case_name)
        self.amount = str(amount)
        self.buy_psw = str(buy_psw)
        self.one_psw = str(one_psw)
    '''



    def setUp(self):
        self.dr = webdriver.Chrome()
        self.baseurl = 'http://dev.lantouzi.com'
        self.dr.get(self.baseurl+r'/login')
        login(self.dr,'17300013252','11111111')



    def test_buysmart_001(self):
        time.sleep(1)
        self.bs = Buy_smart(self.dr)
        self.bs.get_frame().click()  # 切换到智选页面
        self.bs.get_joinsmart().click()  # 选择一个智选服务
        self.bs.get_smartamout().send_keys(self.amount)
        rs = self.bs.get_remaining().text  # 获余额金额
        rs1 = rs.split('元')
        rs2 = rs1[0].split(',')
        rs3 = ''
        for i in rs2:
            rs3 = rs3 + i
        smart_amount = float(rs3)
        print(smart_amount)

        self.bs.get_amount_submit().click()  # 点击马上加入


        if smart_amount >= float(self.amount):
            self.bs.get_buy_now().click() #点击马上加入
            time.sleep(9)
            title1 = self.dr.title
            current_url = self.dr.current_url

            if title1 == r'一账通资金划转':
                print('ssss1')
                self.bs.get_one_transfer().send_keys(self.one_psw)  # 输入一帐通密码
                self.bs.get_greet().click()  # 同一风险协议
                self.bs.get_onesure().click()  # 点击划转

            elif "http://dev.lantouzi.com/smartbid/buy" in current_url:
                print('buy success')
                self.bs.get_check_order().click()
                self.dr.back()

            else:
                print('false')
                self.dr.back()
        else:
            self.bs.get_recharge().click()  # 余额不足就充值
            self.bs.get_i_know().click()  # 点击我知道了
            self.bs.get_phoneV().send_keys('111111')
            self.bs.get_passwd().send_keys(self.buy_psw)  # 输入密码
            self.bs.get_isAgreeReg().click()  # 勾选协议
            self.dr.switch_to.default_content()
            time.sleep(1)
            nb = self.bs.get_renextButton()
            nb.click()  # 点击充值确定


    def tearDown(self):
        logout_bussy(self.dr)
        time.sleep(1)
        self.dr.quit()


if __name__ =='__main__':
    unittest.main()



