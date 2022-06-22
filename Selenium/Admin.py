from selenium import webdriver

import time

sec = 1

driver = webdriver.Chrome(executable_path="C:\\Users\\s\\PycharmProjects\\pythontest\\chromedriver.exe")

driver.get("https://opensource-demo.orangehrmlive.com")

login_user_field = "/html/body/div[1]/div/div[3]/div[2]/div[2]/form/div[2]/input"
driver.find_element_by_xpath(login_user_field).send_keys("Admin")
login_pass_field = "/html/body/div[1]/div/div[3]/div[2]/div[2]/form/div[3]/input"
elm = driver.find_element_by_xpath(login_pass_field)
elm.send_keys("admin123")
elm.submit()

time.sleep(sec)

admin = "/html/body/div[1]/div[2]/ul/li[1]/a/b"
driver.find_element_by_xpath(admin).click()

time.sleep(sec)

System_Users_Search_username = "/html/body/div[1]/div[3]/div[1]/div[2]/form/fieldset/ol/li[1]/input"
username = driver.find_element_by_xpath(System_Users_Search_username)
username.send_keys("Aravind")
username.submit()

time.sleep(sec)

system_users_search_Employee_name = ""
