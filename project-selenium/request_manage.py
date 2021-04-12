import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver_path=r"C:\chromedriver_win32\chromedriver.exe"

driver=webdriver.Chrome(executable_path=driver_path)

driver.get("http://127.0.0.1:8001/login/")
driver.maximize_window()
driver.implicitly_wait(5)

total = 0
pass_case = 0
############登录##############

username,password,randcode ="admin","123456","123"
driver.find_element_by_id("LAY-user-login-username").send_keys(username)
driver.find_element_by_id("LAY-user-login-password").send_keys(password)
driver.find_element_by_id("LAY-user-login-vercode").send_keys(randcode)
driver.find_element_by_id("loginButton").click()

#点击左侧菜单栏
driver.find_element_by_css_selector("body > div > div.layui-side.layui-bg-cyan > div > ul > li > a").click()
time.sleep(2)
driver.find_element_by_link_text("需求申请").click()

#选择需求部门
driver.switch_to.frame(driver.find_element_by_id("mainframe"))
driver.find_element_by_css_selector("#addForm > div:nth-child(2) > div.layui-input-inline > div > div > input").click()
driver.find_element_by_css_selector("#addForm > div:nth-child(2) > div.layui-input-inline > div > dl > dd:nth-child(2)").click()
time.sleep(2)

#选择申请日期
driver.find_element_by_id("order_date").send_keys("2021-09-07")
driver.find_element_by_css_selector("#addForm > div:nth-child(3)").click()
time.sleep(2)

#选择需求名称
driver.find_element_by_id("order_name").send_keys("定制计划")
time.sleep(2)

#选择关联系统
driver.find_element_by_id("order_sys").send_keys("管理系统")
time.sleep(2)

#选择需求类型
driver.find_element_by_css_selector("#addForm > div:nth-child(6) > div > div:nth-child(6) > i").click()
time.sleep(2)

#选择需求描述
driver.find_element_by_id("order_desc").send_keys("黄花城一日游")
time.sleep(2)

#提交
driver.find_element_by_css_selector("#submitBtn").click()

#断言   等待页面元素出现才去获取，只等待10秒
rspmsg = ""
try:
    element = WebDriverWait(driver,10).until(
        expected_conditions.presence_of_element_located((By.ID,'layui-layer2'))
    )

    rspmsg = element.text

except Exception as e:
    print(e)

if rspmsg == "需求登录成功":
    print("测试通过")
else:
    print("测试通过")

















#增加断言方式二：通过页面元素来断言

# assertObject = driver.find_element_by_css_selector("body > div > div.layui-header > div")
# if assertObject and assertObject.text == "接口自动化测试":
#     pass_case+=1
#     print("测试通过")
# else:
#     print("测试失败")
#
# driver.close()