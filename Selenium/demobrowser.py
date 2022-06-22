from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\\Users\\s\\PycharmProjects\\pythontest\\chromedriver.exe")
driver.maximize_window()

driver.get("http://hirehub-admin.newroztech.com/")

print(driver.title)
print(driver.current_url)
driver.close()

driver.get("http://hirehub.newroztech.com/")
driver.minimize_window()
driver.back()
driver.refresh()
driver.close()