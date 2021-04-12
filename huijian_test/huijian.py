from selenium import  webdriver
import time


driver_path = r"C:\chromedriver_win32\chromedriver.exe"
driver=webdriver.Chrome(executable_path=driver_path)

driver.get("https://ad-test.kuaidaoapp.com/advertise/#/?_k=9msnat")
driver.maximize_window()
driver.implicitly_wait(5)

driver.find_element_by_id("username").send_keys("yxybyzyang")
driver.find_element_by_id("password").send_keys("123456")
driver.find_element_by_id("submit_id").click()

#断言
loginone = driver.find_element_by_css_selector("#click_bg > div > div.login-button").text
if loginone == "进入慧见":
    print("登录第一步测试通过")
else:
    print("登录第一步测试失败")

driver.find_element_by_css_selector("#click_bg > div > div.login-button").click()
#断言
logintwo = driver.find_element_by_css_selector("#app > div > div > div.nav-wrap.ant-layout-sider.ant-layout-sider-has-trigger > div.ant-layout-sider-children > ul > li:nth-child(1) > div > span > span").text
if logintwo == "投放管理":
    print("登录成功")
else:
    print("登录第二步失败")


#####################上传计划首字母表##########
driver.find_element_by_css_selector("#app > div > div > div.nav-wrap.ant-layout-sider.ant-layout-sider-has-trigger > div.ant-layout-sider-children > ul > li:nth-child(8) > div > span > span").click()
driver.find_element_by_xpath('//*[@id="7$Menu"]/li[1]/span').click()




#########################新建站点############
# driver.find_element_by_xpath('//*[@id="app"]/div/div/div[1]/div[1]/ul/li[1]/div/span/span').click()
# time.sleep(2)
# driver.find_element_by_xpath('//*[@id="0$Menu"]/li[1]/span').click()
#
# driver.find_element_by_css_selector("#app > div > div > div.ant-layout > div.ant-layout-content > div > div > div > div.siteInfo-table > div.siteInfo-addSite > div > button:nth-child(1)").click()
# all_handles = driver.window_handles
# print(all_handles)