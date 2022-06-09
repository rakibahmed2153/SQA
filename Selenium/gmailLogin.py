from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By

# Driver Path and browser set for run website on it
PATH = "/home/rakib/Downloads/chromedriver_linux64/chromedriver"
driver =  webdriver.Chrome(PATH)

'''
Add user name and password to login
and url of the gmail account login
'''
username = ''
password = ''

url='https://accounts.google.com/AccountChooser/identifier?service=mail&continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&flowName=GlifWebSignIn&flowEntry=AccountChooser'
driver.get(url)


# with for 10 sec then go other process
driver.implicitly_wait(10)
driver.maximize_window()

# Find the username input field
usernameInput = driver.find_element(By.ID, "identifierId")
# Clear the input box
usernameInput.clear()
# send the username in the input box
usernameInput.send_keys(username)
sleep(3)

# Next Button Click
driver.find_element(By.ID, "identifierNext").click()
sleep(3)

# Find the password input field
passInput = driver.find_element(By.ID, "password")
# Clear the input box
passInput.clear()
# send the password in the input box
passInput.send_keys(password)

# Next Button Click
driver.find_element(By.ID, "passwordNext").click()
sleep(3)

print("Login Successful")
