import time
from selenium import webdriver


driver=webdriver.Chrome()

driver.get("http://127.0.0.1:8001/login/")
driver.maximize_window()
driver.implicitly_wait(5)

total = 0
pass_case = 0
############登录正向用例##############
print("用例1：登录正向用例")
username,password,randcode ="admin","123456","123"
driver.find_element_by_id("LAY-user-login-username").send_keys(username)
driver.find_element_by_id("LAY-user-login-password").send_keys(password)
driver.find_element_by_id("LAY-user-login-vercode").send_keys(randcode)
driver.find_element_by_id("loginButton").click()

total+=1
#增加断言方式一：通过标题来断言
"""
time.sleep(3)
page_title = driver.title
if page_title == "自动化测试web项目":
    print("测试通过")
else:
    print("测试失败")
"""

#增加断言方式二：通过页面元素来断言

assertObject = driver.find_element_by_css_selector("body > div > div.layui-header > div")
if assertObject and assertObject.text == "接口自动化测试":
    pass_case+=1
    print("测试通过")
else:
    print("测试失败")

driver.quit()

############登录反向用例_用户名错误##############
print("用例2：用户名错误")
driver=webdriver.Chrome(executable_path=driver_path)

driver.get("http://127.0.0.1:8001/login/")
driver.maximize_window()
driver.implicitly_wait(5)


username,password,randcode ="admin","12345","123"
driver.find_element_by_id("LAY-user-login-username").send_keys(username)
driver.find_element_by_id("LAY-user-login-password").send_keys(password)
driver.find_element_by_id("LAY-user-login-vercode").send_keys(randcode)
driver.find_element_by_id("loginButton").click()
total+=1

#增加断言
rspmsg = driver.find_element_by_css_selector("#layui-layer2 > div.layui-layer-content.layui-layer-padding")
if rspmsg and rspmsg.text == "用户名或密码错误":
    pass_case += 1
    print("测试通过")
else:
    print("测试失败")

driver.close()

############登录反向用例_密码错误##############
print("用例3：密码错误")
driver = webdriver.Chrome(executable_path=driver_path)

driver.get("http://127.0.0.1:8001/login/")
driver.maximize_window()
driver.implicitly_wait(5)

username, password, randcode = "admin1", "123456", "123"
driver.find_element_by_id("LAY-user-login-username").send_keys(username)
driver.find_element_by_id("LAY-user-login-password").send_keys(password)
driver.find_element_by_id("LAY-user-login-vercode").send_keys(randcode)
driver.find_element_by_id("loginButton").click()
total+=1

# 增加断言
rspmsg = driver.find_element_by_css_selector("#layui-layer2 > div.layui-layer-content.layui-layer-padding")
if rspmsg and rspmsg.text == "用户名或密码错误":
    pass_case += 1
    print("测试通过")
else:
    print("测试失败")

driver.close()

############登录反向用例_用户名为空##############
print("用例4：用户名为空")
driver = webdriver.Chrome(executable_path=driver_path)

driver.get("http://127.0.0.1:8001/login/")
driver.maximize_window()
driver.implicitly_wait(5)

username, password, randcode = "admin", "123456", "123"
# driver.find_element_by_id("LAY-user-login-username").send_keys(username)
driver.find_element_by_id("LAY-user-login-password").send_keys(password)
driver.find_element_by_id("LAY-user-login-vercode").send_keys(randcode)
driver.find_element_by_id("loginButton").click()
total+=1

# 增加断言
rspmsg = driver.find_element_by_id("layui-layer1")
if rspmsg and rspmsg.text == "请输入用户名和密码":
    pass_case += 1
    print("测试通过")
else:
    print("测试失败")

driver.quit()
print("执行用例数为：%d,执行通过：%d,执行失败：%d"%(total,pass_case,total-pass_case))