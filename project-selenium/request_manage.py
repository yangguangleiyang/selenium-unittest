import datetime
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

time_sleep = 2


#打开左侧菜单栏函数
def gotopage(pagename):
    driver.find_element_by_css_selector("body > div > div.layui-side.layui-bg-cyan > div > ul > li > a").click()
    time.sleep(time_sleep)
    driver.find_element_by_link_text(pagename).click()
    driver.switch_to.frame(driver.find_element_by_id("mainframe"))   #切换iframe


#提交表单
def doFormInput(params):
    #选择申请部门
    if "dept" in case_params:
        driver.find_element_by_css_selector("#addForm > div:nth-child(2) > div.layui-input-inline > div > div > input").click()
        # driver.find_element_by_css_selector("#addForm > div:nth-child(2) > div.layui-input-inline > div > dl > dd:nth-child(2)").click()
        elems = driver.find_elements_by_css_selector("#addForm > div:nth-child(2) > div.layui-input-inline > div > dl > dd")
        for ele in elems:
            if ele.text == params["dept"]:
                ele.click()
                break
        time.sleep(time_sleep)

    #选择申请日期
    if "date" in case_params:
        driver.find_element_by_id("order_date").send_keys(params["date"])
        driver.find_element_by_css_selector("#addForm > div:nth-child(3)").click()
        time.sleep(time_sleep)

    #选择需求名称
    if "name" in case_params:
        driver.find_element_by_id("order_name").send_keys(params["name"])
        time.sleep(time_sleep)

    #选择关联系统
    if "refers" in case_params:
        driver.find_element_by_id("order_sys").send_keys(params["refers"])
        time.sleep(time_sleep)

    #选择需求类型
    driver.find_element_by_css_selector("#addForm > div:nth-child(6) > div > div:nth-child(6) > i").click()
    time.sleep(time_sleep)

    #选择需求描述
    if "desc" in case_params:
        driver.find_element_by_id("order_desc").send_keys(params["desc"])
        time.sleep(time_sleep)

    #提交
    driver.find_element_by_css_selector("#submitBtn").click()



def assertSucces(assert_text):
    global total,pass_case
    total += 1
    rspmsg = ""
    try:
        element = WebDriverWait(driver, 10).until(
            expected_conditions.presence_of_element_located((By.ID, 'layui-layer2'))
        )

        rspmsg = element.text

    except Exception as e:
        print(e)

    if rspmsg == assert_text:
        print("测试通过")
        pass_case += 1
    else:
        print("测试失败")




driver_path=r"C:\chromedriver_win32\chromedriver.exe"
driver=webdriver.Chrome(executable_path=driver_path)

driver.get("http://127.0.0.1:8001/login/")
driver.maximize_window()
driver.implicitly_wait(5)    #隐式等待 就是如果这个元素一开始没有出现，会等待这个元素5秒，如果超过5秒还没出现，会报超时错误


############登录##############

username,password,randcode ="admin","123456","123"
driver.find_element_by_id("LAY-user-login-username").send_keys(username)
driver.find_element_by_id("LAY-user-login-password").send_keys(password)
driver.find_element_by_id("LAY-user-login-vercode").send_keys(randcode)
driver.find_element_by_id("loginButton").click()


total = 0
pass_case = 0
############################################
print("用例1，正例",end="...")
case_params = {
    "dept":"人力部门",
    "date":"2021-10-19",
    "name":"测试需求名称",
    "refers":"关联的应用系统",
    "desc":"需求描述内容",
    "type":"需求变更"
}

#打开菜单
gotopage("需求申请")

#录入表单
doFormInput(case_params)


#断言   等待页面元素出现才去获取，只等待10秒
assertSucces("需求登记成功.")

driver.refresh()


############################################
print("用例2，正例",end="...")
case_params = {
    "dept":"人力部门",
    "date":datetime.date.today().strftime("%Y-%M-%D"),
    "name":"测试需求名称",
    "refers":"关联的应用系统",
    "desc":"需求描述内容",
    "type":"需求变更"
}

#打开菜单
gotopage("需求申请")

#录入表单
doFormInput(case_params)

#断言   等待页面元素出现才去获取，只等待10秒
assertSucces("需求登记成功.")

driver.quit()




print("共执行用例：",total,"执行成功：",pass_case,"执行失败：",total-pass_case)













#增加断言方式二：通过页面元素来断言

# assertObject = driver.find_element_by_css_selector("body > div > div.layui-header > div")
# if assertObject and assertObject.text == "接口自动化测试":
#     pass_case+=1
#     print("测试通过")
# else:
#     print("测试失败")
#
# driver.close()