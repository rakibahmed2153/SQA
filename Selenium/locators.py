from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\\Users\\s\\PycharmProjects\\pythontest\\chromedriver.exe")
driver.get("https://rahulshettyacademy.com/angularpractice/")


dropdown = Select(driver.find_element_by_id("exampleFormControlSelect1"))
dropdown.select_by_visible_text("Female")
driver.find_element_by_xpath("//input[@type='submit']").click()
message = driver.find_element_by_class_name("alert-success").text

assert "Sucess" in message








driver.find_element_by_name("firstName").send_keys("Moin")
driver.find_element_by_name("lastName").send_keys("Ahmed")
driver.find_element_by_css_selector("input[name='name']")
driver.find_element_by_name("email").send_keys("ahmed+12@newroztech.com")
driver.find_element_by_name("password").send_keys("Password100@")
driver.find_element_by_name("confirm-password").send_keys("Password100@")
driver.find_element_by_xpath("//button[@type='submit']").click()

