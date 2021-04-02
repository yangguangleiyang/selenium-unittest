# print("hello world1")

from selenium import webdriver

driver_path=r"C:\chromedriver_win32\chromedriver.exe"

driver=webdriver.Chrome(executable_path=driver_path)

driver.get("http://baidu.com")