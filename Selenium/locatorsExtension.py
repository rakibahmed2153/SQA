from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\\Users\\s\\PycharmProjects\\pythontest\\chromedriver.exe")

driver.get("https://login.salesforce.com/?locale=eu")
driver.find_element_by_css_selector("#username").send_keys("Moin")
driver.find_element_by_css_selector(".password").send_keys("Password100@")
driver.find_element_by_css_selector(".password").clear()
driver.find_element_by_partial_link_text("Forgot Your Password?").click()