# -*- coding: utf-8 -*-
import os
import datetime
import shutil
from selenium import webdriver
from time import sleep


# Variable
URL = "https://cybozulive.com/"
ID = ["xxx"]
PASS = ["xxx"]


# Login
def LOGIN():
	
    # ChromeStarting
    _driver = webdriver.Chrome("./chromedriver")
    _driver.set_window_size(1280, 720)
    _driver.get(URL)

    # Login
    _login_id = _driver.find_element_by_name("loginMailAddress")
    _password = _driver.find_element_by_name("password")
    _login_id.send_keys(ID[_num])
    _password.send_keys(PASS[_num])
    _driver.find_element_by_name(
                                "czJzdHJ1dHMuQkFTRTY0X0ZPUk1BVDpzMnN0cnV0cy5BQ1RJT05fRVhQUkVTU0lPTj0lNDAlN0Jsb2dpbl9sb2dpbkFjdGlvbi5kb0xvZ2luJTdE").click()

    # ScreenShot
    _now = datetime.datetime.now()
    _fmt_name = "LoginCheck_{0:%Y%m%d-%H%M%S}.png".format(_now)
    _driver.save_screenshot(_fmt_name)

    # Logout
    _driver.find_element_by_id("cba_logout").click()


# Main #####################
if __name__ == '__main__':
    _num = 0
    for _loop in ID:
        LOGIN()
        sleep(3)
        _num += 1
############################
