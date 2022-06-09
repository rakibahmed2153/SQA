from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Driver Path and browser set for run website on it
PATH = "/home/rakib/Downloads/chromedriver_linux64/chromedriver"
driver =  webdriver.Chrome(PATH)
# Website add
driver.get("https://techwithtim.net/")


try:
    # Wait until the page load and text find
    element = WebDriverWait(driver, 10).until(
       EC.presence_of_element_located((By.LINK_TEXT, "Python Programming"))
    )
    element.click()
    
    # Wait until the page load and text find
    element = WebDriverWait(driver, 10).until(
       EC.presence_of_element_located((By.LINK_TEXT, "Beginner Python Tutorials"))
    )
    element.click()

    # Wait until the page load and find the button
    element = WebDriverWait(driver, 10).until(
       EC.presence_of_element_located((By.ID, "sow-button-19310003"))
    )
    element.click()

    # Back to previous page
    driver.back()

    # GO Forward
    # driver.forward()
    
except:
    driver.quit()   


