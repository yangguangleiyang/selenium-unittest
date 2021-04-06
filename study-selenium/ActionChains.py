import time

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

driver_path=r"C:\chromedriver_win32\chromedriver.exe"

driver=webdriver.Chrome(executable_path=driver_path)

# driver.get("https://www.baidu.com/")
driver.get("https://mail.qq.com/")

driver.maximize_window()

#鼠标悬停
# sz = driver.find_element_by_id("s-usersetting-top")
# ActionChains(driver).move_to_element(sz).perform()  #perform是让ActioonChains执行起来
#
# time.sleep(2)
#
# driver.find_element_by_link_text("搜索设置").click()


#鼠标右键
# ipt = driver.find_element_by_id("kw")
# ActionChains(driver).context_click(ipt).perform()

#键盘删除操作
# ipt = driver.find_element_by_id("kw")
# ipt.send_keys("selenium")
# time.sleep(3)
#
# ipt.send_keys(Keys.BACKSPACE)   #删除一个字母
# time.sleep(3)
#
# ipt.send_keys(Keys.SPACE)        #输入一个空格


#进行iframe的切换
driver.switch_to.frame(driver.find_element_by_id("login_frame"))  #先切换到iframe元素下
driver.find_element_by_id("u").send_keys("test")
