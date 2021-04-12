from selenium import webdriver
import time

from selenium.webdriver.common.action_chains import ActionChains

driver_path=r"C:\chromedriver_win32\chromedriver.exe"

driver=webdriver.Chrome(executable_path=driver_path)

#滑动拖拽  携程网注册页面
# driver.get("https://passport.ctrip.com/user/reg/home")
# driver.maximize_window()
#
# driver.find_element_by_css_selector("#agr_pop > div.pop_footer > a.reg_btn.reg_agree").click()
# time.sleep(3)
#
# source = driver.find_element_by_css_selector("#slideCode > div.cpt-drop-box > div.cpt-drop-btn > div > i.cpt-logo.cpt-img-double-right")
# box = driver.find_element_by_css_selector("#slideCode > div.cpt-drop-box > div.cpt-bg-bar")
#
# ActionChains(driver).drag_and_drop_by_offset(source,box.size['width'],0).perform()


#多窗口切换

driver.get("http://www.baidu.com")
driver.maximize_window()
driver.implicitly_wait(5)

print(driver.current_window_handle)      #查看当前窗口句柄
driver.find_element_by_link_text("新闻").click()

print(driver.current_window_handle)     #继续查看当前窗口句柄

handles = driver.window_handles #查看一共开了多少窗口
print(handles)
driver.switch_to.window(handles[1])
driver.find_element_by_link_text("军事").click()

