from selenium import webdriver
import time

sec = 1

driver = webdriver.Chrome(executable_path="C:\\Users\\s\\PycharmProjects\\pythontest\\chromedriver.exe")

driver.get("https://opensource-demo.orangehrmlive.com/")

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

PIM = "/html/body/div[1]/div[2]/ul/li[2]/a/b"
driver.find_element_by_xpath(PIM).click()

time.sleep(sec)



Leave = "/html/body/div[1]/div[2]/ul/li[3]/a/b"
driver.find_element_by_xpath(Leave).click()

time.sleep(sec)

Time = "/html/body/div[1]/div[2]/ul/li[4]/a/b"
driver.find_element_by_xpath(Time).click()

time.sleep(sec)

Rec = "/html/body/div[1]/div[2]/ul/li[5]/a/b"
driver.find_element_by_xpath(Rec).click()

time.sleep(sec)

My_info = "/html/body/div[1]/div[2]/ul/li[6]/a/b"
driver.find_element_by_xpath(My_info).click()

time.sleep(sec)

Performance = "/html/body/div[1]/div[2]/ul/li[7]/a/b"
driver.find_element_by_xpath(Performance).click()

time.sleep(sec)

Dashboard = "/html/body/div[1]/div[2]/ul/li[8]/a/b"
driver.find_element_by_xpath(Dashboard).click()

time.sleep(sec)

Directory = "/html/body/div[1]/div[2]/ul/li[8]/a/b"
driver.find_element_by_xpath(Directory).click()

time.sleep(sec)

Maintenance = "/html/body/div[1]/div[2]/ul/li[10]/a/b"
driver.find_element_by_xpath(Maintenance).click()

time.sleep(sec)

Buzz = "/html/body/div[1]/div[2]/ul/li[11]/a/b"
driver.find_element_by_xpath(Buzz).click()

time.sleep(sec)

Marketplace = "/html/body/div[1]/div[1]/div[8]/input"
driver.find_element_by_xpath(Marketplace).click()

time.sleep(sec)

# Notificaion_bell_icon = "/html/body/div[1]/div[1]/div[1]/span/svg/path"
# driver.find_element_by_xpath(Notificaion_bell_icon).click()
#
# time.sleep(2)

Profile = "/html/body/div[1]/div[1]/a[2]"
driver.find_element_by_xpath(Profile).click()

time.sleep(sec)

about = "#aboutDisplayLink"
driver.find_element_by_css_selector(about).click()

time.sleep(sec)

cancel_about = "#displayAbout > div > a"
driver.find_element_by_css_selector(cancel_about).click()

time.sleep(sec)

Support = "#welcome-menu > ul > li:nth-child(2) > a"
driver.find_element_by_css_selector(Support).click()

time.sleep(sec)


