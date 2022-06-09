from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

# Driver Path and browser set for run website on it
PATH = "/home/rakib/Downloads/chromedriver_linux64/chromedriver"
driver =  webdriver.Chrome(PATH)
# Website add
driver.get("https://orteil.dashnet.org/cookieclicker/")

# with for 10 sec then go other process
driver.implicitly_wait(10)
# print('print =====', driver.find_element('id', 'languageSelectHeader'))
# if(driver.find_element('id', 'languageSelectHeader')):
eng = driver.find_element('id', 'languageSelectHeader')
eng.click()


# Find element by id
cookie = driver.find_element("id", "bigCookie")
cookie_count = driver.find_element("id", "cookies") 

# find items to update
items = [driver.find_element("id", "productPrice" + str(i)) for i in range(1,-1,-1)]

# Set the action in Queue
actions = ActionChains(driver)
actions.click(cookie)

for i in range(5000):

    # perform the action
    actions.perform()