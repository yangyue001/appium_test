
from py_function.getcookie import *

import unittest
import time
from py_function.ssdb_do import ssdb_c
from py_function.get_vcode import ssdb_get_vcode
import requests
from py_function.jiami import *

class_ssdb = ssdb_c()
base_url = 'http://dev.lantouzi.com/'

def sleep(n_secs):
    time.sleep(n_secs)

def ssdb_clear(*mobile):
    l = ['safe_act|10.18.0.1|change_mobile_send_daily', 'safe_act|10.18.0.1|change_mobile_send_daily|warn',
         'safe_act|10.18.0.1|login-fail', 'safe_act|10.18.0.1|login_ip', 'safe_act|10.18.0.1|login_ok',
         'safe_act|10.18.0.1|register_mobile_send_daily', 'safe_act|10.18.0.1|register_mobile_send_daily|warn']
    for a in mobile:
        m_login = 'safe_act|'+str(a)+'|login'
        m_login_fail = 'safe_act|'+str(a)+'|login-fail'
        m_login_name = 'safe_act|'+str(a)+'|login_name'
        m_login_ok = 'safe_act|'+str(a)+ '|login_ok'
        l.append(m_login)
        l.append(m_login_fail)
        l.append(m_login_name)
        l.append(m_login_ok)
    for i in l:
        class_ssdb.ssdb_clear(i)

'''
def get_cookies(LTZ_S,DWJUC_S):
    cookies = "LTZ_S=" + LTZ_S + "; DWJUC_S=" + DWJUC_S
    return cookies
'''

def get_vcode(moblie):
    sv = ssdb_get_vcode()
    vocode = sv.get_voced(moblie)
    return vocode



def get_key():

    r = requests.get('http://dev.lantouzi.com/api/uc/get_key')
    re_r = r.json()
    data = re_r['data']
    entr = data['encrypt']
    pub_key = entr['public_key']
    field_value = entr['field_value']

    print(pub_key)
    return pub_key,field_value

def jiami(key,msg):

    jm_msg = scrit_key(key,msg)
    return jm_msg


def upload_files(name,file):
    files = {'images': (name, open(file, 'rb'), 'image/jpeg')}
    return files

'''
def get_cook(a,b,*kwargs):
    cook = 'LTZ_S='+a+';'+'DWJUC_S='+b
    for var  in kwargs:
        cook = cook+str(var)
    return cook
'''

if __name__ == '__main__':
    ssdb_clear('17300013254')