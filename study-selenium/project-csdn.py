from selenium import webdriver

driver_path=r"C:\chromedriver_win32\chromedriver.exe"

driver=webdriver.Chrome(executable_path=driver_path)

driver.get("https://www.csdn.net/")
driver.implicitly_wait(5)

driver.find_element_by_link_text(r"登录/注册").click()
driver.find_element_by_link_text("账号密码登录").click()
driver.find_element_by_id("all").send_keys("13718627413")
driver.find_element_by_id("password-number").send_keys("123456")
driver.find_element_by_class_name("btn-primary").click()
