from selenium import webdriver
import time

# driver_path=r"C:\chromedriver_win32\chromedriver.exe"

driver=webdriver.Chrome()

driver.get("https://www.baidu.com/")

# driver.maximize_window()
#
# title=driver.title   #拿到页面的title
# print(title)
#
# url=driver.current_url   #拿到当前页面的url
# print(url)
#
# driver.back()         #页面后退
# time.sleep(3)
#
# driver.forward()       #页面前进
# time.sleep(3)
#
# driver.refresh()        #页面刷新
