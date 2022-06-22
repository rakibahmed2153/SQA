from selenium import webdriver

import time


# Driver Path and browser set for run website on it
PATH = "/home/rakib/Downloads/chromedriver_linux64/chromedriver"
driver =  webdriver.Chrome(PATH)

url= "https://rahulshettyacademy.com/angularpractice/"
driver.get(url)

driver.find_element_by_css_selector("body > app-root > app-navbar > div > nav > ul > li:nth-child(2) > a").click()

# products = driver.find_elements_by_xpath("//div[@class='card h-100']")
driver.find_element_by_xpath("/html/body/app-root/app-shop/nav/div/div/ul/li/a").click()
driver.find_element_by_xpath("/html/body/app-root/app-shop/div/div/div/table/tbody/tr[2]/td[5]/button").click()
driver.find_element_by_id("country").send_keys("ind")
# driver.find_element_by_id("//div[@class='checkbox checkbox-primary']").click()

driver.get_screenshot_as_file("screen.png")
