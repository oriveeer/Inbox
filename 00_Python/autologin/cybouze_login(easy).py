from selenium import webdriver
from time import sleep

def login_():
    driver = webdriver.Chrome(".chromedriver")
    driver.get("https://cybozulive.com/")

    login_id = driver.find_element_by_name("loginMailAddress")
    password = driver.find_element_by_name("password")

    login_id.send_keys("mail-address")
    password.send_keys("xxxxx")
    driver.find_element_by_name(
                                "czJzdHJ1dHMuQkFTRTY0X0ZPUk1BVDpzMnN0cnV0cy5BQ1RJT05fRVhQUkVTU0lPTj0lNDAlN0Jsb2dpbl9sb2dpbkFjdGlvbi5kb0xvZ2luJTdE").click()

login_()
sleep(999)
