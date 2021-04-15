from selenium import  webdriver
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys

driver_path = r"C:\chromedriver_win32\chromedriver.exe"
driver=webdriver.Chrome(executable_path=driver_path)

driver.get("https://ad-test.kuaidaoapp.com/advertise/#/?_k=9msnat")
driver.maximize_window()
driver.implicitly_wait(10)
time_sleep = 2


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
# driver.find_element_by_css_selector("#app > div > div > div.nav-wrap.ant-layout-sider.ant-layout-sider-has-trigger > div.ant-layout-sider-children > ul > li:nth-child(8) > div > span > span").click()
# driver.find_element_by_xpath('//*[@id="7$Menu"]/li[1]/span').click()
# driver.find_element_by_css_selector("#app > div > div > div.ant-layout > div.ant-layout-content > div > div > div > div.ant-tabs-bar > div > div > div > div > div:nth-child(4)").click()
#
# #上传文件
# test_project = "测试蛋糕"
# driver.find_element_by_css_selector("#app > div > div > div.ant-layout > div.ant-layout-content > div > div > div > div.ant-tabs-content.ant-tabs-content-animated > div.ant-tabs-tabpane.ant-tabs-tabpane-active > div > div._1x9fBCtMtv3XPSME9k73dx > span > div > span > input[type=file]").send_keys(r'C:\Users\admin\Desktop\jihuashouzimubiao.xlsx')
# driver.find_element_by_css_selector("body > div:nth-child(8) > div > div.ant-modal-wrap > div > div.ant-modal-content > div > div > div.ant-confirm-btns > button:nth-child(1)").click()
#
# #再次点击计划首字母表页面，切换回来
# time.sleep(5)
# driver.refresh()
# driver.find_element_by_css_selector("#app > div > div > div.ant-layout > div.ant-layout-content > div > div > div > div.ant-tabs-bar > div > div > div > div > div:nth-child(4)").click()
# time.sleep(2)
#
#
# #断言
# all_text = driver.find_element_by_css_selector("#app > div > div > div.ant-layout > div.ant-layout-content > div > div > div > div.ant-tabs-content.ant-tabs-content-animated > div.ant-tabs-tabpane.ant-tabs-tabpane-active > div > div.ant-table-wrapper > div > div > div > div > div > table > tbody").text
#
# if test_project in all_text:
#     print("计划首字母表上传成功")
# else:
#     print("计划首字母表上传失败")

#########################新建站点############
# driver.find_element_by_xpath('//*[@id="app"]/div/div/div[1]/div[1]/ul/li[1]/div/span/span').click()
# time.sleep(2)
# driver.find_element_by_xpath('//*[@id="0$Menu"]/li[1]/span').click()
# #点击新增站点按钮
# driver.find_element_by_css_selector("#app > div > div > div.ant-layout > div.ant-layout-content > div > div > div > div.siteInfo-table > div.siteInfo-addSite > div > button:nth-child(1)").click()
#
# #弹出框
# driver.find_element_by_css_selector(".ant-form > .ant-row .ant-select-selection__placeholder").click()
# driver.find_element_by_css_selector(".ant-select-dropdown-menu-item-active").click()


##########新建落地页###########
project = "CSSJ"

driver.find_element_by_xpath('//*[@id="app"]/div/div/div[1]/div[1]/ul/li[2]/div/span/span').click()
driver.find_element_by_xpath('//*[@id="1$Menu"]/li[1]/span').click()
#点击上传落地页
driver.find_element_by_css_selector("#app > div > div > div.ant-layout > div.ant-layout-content > div > div > div > div > div:nth-child(2) > div:nth-child(1) > button").click()
time.sleep(time_sleep)

driver.find_element_by_css_selector(".ant-col-xs-18 #pageName").send_keys("落地页1")
driver.find_element_by_css_selector("body > div:nth-child(7) > div > div.ant-modal-wrap > div > div.ant-modal-content > div.ant-modal-body > form > div:nth-child(2) > div > div > div.ant-form-item-label.ant-col-xs-5.ant-col-sm-5").click()
time.sleep(time_sleep)

driver.find_element_by_css_selector(".ant-row-flex:nth-child(2) > .ant-col-24 .ant-select-selection__placeholder").click()
driver.find_element_by_id("domainId").send_keys("ce6.test.icloudidc.net")
driver.find_element_by_id("domainId").send_keys(Keys.ENTER)
driver.find_element_by_css_selector("body > div:nth-child(7) > div > div.ant-modal-wrap > div > div.ant-modal-content > div.ant-modal-body > form > div:nth-child(2) > div > div > div.ant-form-item-label.ant-col-xs-5.ant-col-sm-5").click()
time.sleep(time_sleep)
#输入项目缩写
driver.find_element_by_css_selector("body > div:nth-child(7) > div > div.ant-modal-wrap > div > div.ant-modal-content > div.ant-modal-body > form > div:nth-child(5) > div > div > div.ant-form-item-control-wrapper.ant-col-xs-18.ant-col-sm-18 > div > div > div > div > div.ant-select-selection__placeholder").click()
driver.find_element_by_css_selector(".ant-select-open #projectCode").send_keys(project)
driver.find_element_by_css_selector(".ant-select-open #projectCode").send_keys(Keys.ENTER)
time.sleep(time_sleep)

#输入页面编码
driver.find_element_by_css_selector(".ant-col-xs-18 #pageCode").click()
driver.find_element_by_css_selector(".ant-col-xs-18 #pageCode").send_keys("123")
time.sleep(time_sleep)

#添加压缩包
driver.find_element_by_css_selector("body > div:nth-child(7) > div > div.ant-modal-wrap > div > div.ant-modal-content > div.ant-modal-body > form > div:nth-child(7) > div > div > div.ant-form-item-control-wrapper.ant-col-xs-18.ant-col-sm-18 > div > div > span > div.ant-upload.ant-upload-drag > span > input[type=file]").send_keys(r"C:\Users\admin\Desktop\py-j31-001-18094.zip")
time.sleep(time_sleep)

#点击确定按钮
driver.find_element_by_css_selector("body > div:nth-child(7) > div > div.ant-modal-wrap > div > div.ant-modal-content > div.ant-modal-footer > button.ant-btn.ant-btn-primary.ant-btn-lg").click()
