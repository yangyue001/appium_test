from xlrd import open_workbook
from Conf.read_config import *
import pyssdb
def get_xls_nrows(xlsname,sheetname):
    clv =[] #建立一个空列表
    xls_path = os.path.join(rootDir,'test_File','case',xlsname)#找到对应文件地址
    file = open_workbook(xls_path)#打开此文件
    sheet = file.sheet_by_name(sheetname)#获取对应名称sheet
    nrows = sheet.nrows #获取行的总数
    for i in range(nrows):
        if sheet.row_values(i)[0]!= 'case_name': #如果此行的第一列名称不是case_name（过滤掉第一行）
            clv.append(sheet.row_values(i)) #获取各个行的值
    return clv

def clear_ssdb(*mobile):
    ssdb = pyssdb.Client('127.0.0.1', 8866)
    try:
        l = ['safe_act|10.18.0.1|change_mobile_send_daily', 'safe_act|10.18.0.1|change_mobile_send_daily|warn',
                 'safe_act|10.18.0.1|login-fail', 'safe_act|10.18.0.1|login_ip', 'safe_act|10.18.0.1|login_ok',
                 'safe_act|10.18.0.1|register_mobile_send_daily', 'safe_act|10.18.0.1|register_mobile_send_daily|warn']
        for a in mobile:
            m_login = 'safe_act|' + str(a) + '|login'
            m_login_fail = 'safe_act|' + str(a) + '|login-fail'
            m_login_name = 'safe_act|' + str(a) + '|login_name'
            m_login_ok = 'safe_act|' + str(a) + '|login_ok'
            l.append(m_login)
            l.append(m_login_fail)
            l.append(m_login_name)
            l.append(m_login_ok)
        for i in l:
            ssdb.set(i,0)
    finally:
        ssdb.disconnect()



def get_ssdb():
    ssdb1 = pyssdb.Client('127.0.0.1', 8866)
    try:
        l = 'safe_act|10.18.0.1|change_mobile_send_daily'
        s= ssdb1.get(l)
        print(s)

    except Exception as e:
        print(e)
    finally:
        ssdb1.disconnect()