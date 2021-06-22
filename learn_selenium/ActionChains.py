
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time

# driver =  webdriver.Chrome()
# driver.get("http://www.baidu.com")
# driver.maximize_window()

#鼠标悬浮
# sz = driver.find_element_by_id("s-usersetting-top")
# ActionChains(driver).move_to_element(sz).perform()
#
# time.sleep(3)
#
# driver.find_element_by_link_text("搜索设置").click()


#鼠标右键
# ipt = driver.find_element_by_id("kw")
# ActionChains(driver).context_click(ipt).perform()

#键盘删除键
# ipt = driver.find_element_by_id("kw")
# ipt.send_keys("selenium")
# ipt.send_keys(Keys.BACK_SPACE)    #删除一下

#iframe切换
driver=webdriver.Chrome()
driver.get("http://www.mail.qq.com")
driver.maximize_window()

driver.switch_to.frame(driver.find_element_by_id("login_frame"))
driver.find_element_by_id("u").send_keys("test")

