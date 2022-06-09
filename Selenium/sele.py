from selenium import webdriver

PATH = "/home/rakib/Downloads/chromedriver_linux64/chromedriver"

drive = webdriver.Chrome(PATH)
# Access the website
drive.get('https://github.com/')
# Title of the Web Site
print(drive.title)
# Quit the browser
drive.quit()
# Exit only the tab of the browser
# drive.exit()
