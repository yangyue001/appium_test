from PageObject.log_out import *

def log_out(dr):
    lo = logout(dr)
    lo.get_logout_button().click()
