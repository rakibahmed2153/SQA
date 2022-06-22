from selenium import webdriver

import time

driver = webdriver.Chrome(executable_path="C:\\Users\\s\\PycharmProjects\\pythontest\\chromedriver.exe")

driver.get("https://opensource-demo.orangehrmlive.com/")

forgot_password = "/html/body/div[1]/div/div[3]/div[2]/div[2]/form/div[5]/div/a"
driver.find_element_by_xpath(forgot_password).click()

value = "securityAuthentication_userName"

elm = driver.find_element_by_id(value)
elm.send_keys("Admin")
elm.submit()

time.sleep(3)

driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div[3]/form/fieldset/div/input[2]").click()

