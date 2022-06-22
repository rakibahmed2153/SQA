from selenium import webdriver

# Driver Path and browser set for run website on it
PATH = "/home/rakib/Downloads/chromedriver_linux64/chromedriver"
driver =  webdriver.Chrome(PATH)
# Website add
driver.get("https://www.rahulshettyacademy.com/AutomationPractice/")


driver.find_element("id", "name").send_keys("Option3")
driver.find_element("id", "alertbtn").click()

# alert 
alert = driver.switch_to.alert
print(alert.text)
alert.accept()

