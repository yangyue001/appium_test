from PageObject.log_out import *
from PageObject.LoginPage import *

def login_bussy(dr,username,psw):
    lp = LoginPage(dr)
    lp.get_frame().click()
    lp.get_name().send_keys(username)
    lp.get_userpsw().send_keys(psw)
    lp.get_loginbutton().click()


def logout_bussy(dr):
    lo = logout(dr)
    lo.get_logout_button().click()