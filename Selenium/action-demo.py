from selenium import webdriver
from selenium.webdriver import ActionChains

driver = webdriver.Chrome(executable_path="C:\\Users\\s\\PycharmProjects\\pythontest\\chromedriver.exe")
action = ActionChains(driver)

driver.get("https://chercher.tech/practice/practice-pop-ups-selenium-webdriver")
double_click(driver.find_element_by_id("double-click")).perform()


