from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

PATH = "/home/rakib/Downloads/chromedriver_linux64/chromedriver"

drive = webdriver.Chrome(PATH)
# Access the website
drive.get('https://techwithtim.net/')
# Title of the Web Site
print(drive.title)

# Exit only the tab of the browser
# drive.exit()

#Sourse Code Of the site
# print(drive.page_source)

# Access a Search Box and grab all the search result
"""
 => First need to take the element ID, If ID not there the name In worst case take the class name and so on.
 => Need to take unique name or element to take the specific one.
"""
# locate the element
search = drive.find_element("name", "s")
# Clear the input box
drive.clear()
# type valiable in the input box
search.send_keys("test")
# Click on the submit button to send
search.send_keys(Keys.RETURN)

# Wait until the main is located
try:
    
    main = WebDriverWait(drive, 100).until(
       EC.presence_of_element_located((By.ID, "main"))
    )
    print(main)
    articals = main.find_element("tag", "article")
    print(articals)
    for artical in articals:
        header = artical.find_element("class", "published")
        print(header.text)
except:
    drive.quit()    

# Quit the browser
drive.quit()