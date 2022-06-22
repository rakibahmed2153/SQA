from selenium import webdriver

import time

# Driver Path and browser set for run website on it
PATH = "/home/rakib/Downloads/chromedriver_linux64/chromedriver"
driver =  webdriver.Chrome(PATH)
# Website add
driver.get("https://opensource-demo.orangehrmlive.com")

login_user_field = "/html/body/div[1]/div/div[3]/div[2]/div[2]/form/div[2]/input"
driver.find_element_by_xpath(login_user_field).send_keys("Admin")
login_pass_field = "/html/body/div[1]/div/div[3]/div[2]/div[2]/form/div[3]/input"
elm = driver.find_element_by_xpath(login_pass_field)
elm.send_keys("admin123")
elm.submit()

time.sleep(2)

Profile = "/html/body/div[1]/div[1]/a[2]"
driver.find_element_by_xpath(Profile).click()

time.sleep(2)

logout = "#welcome-menu > ul > li:nth-child(3) > a"
driver.find_element_by_css_selector(logout).click()
