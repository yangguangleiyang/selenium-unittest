import unittest
from selenium import webdriver
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from ddt import ddt,data,file_data

@ddt
class LoginTestCase(unittest.TestCase):
    def do_input(self,username=None,password=None,randcode=1234):
        if username:
            self.driver.find_element_by_id("LAY-user-login-username").send_keys(username)
        if password:
            self.driver.find_element_by_id("LAY-user-login-password").send_keys(password)
        if randcode:
            self.driver.find_element_by_id("LAY-user-login-vercode").send_keys(randcode)
        self.driver.find_element_by_id("loginButton").click()

    def setUp(self):
        self.driver = webdriver.Chrome()

        self.driver.get("http://127.0.0.1:8001/login/")
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)

    def tearDown(self):
        self.driver.close()


    @file_data("test_data/test_login_normal.yaml")
    def test_1_normal(self,username,password):
        #用户登录的正例测试
        print(f"username:{username},password:{password}")


        self.do_input(username,password)

        # 断言：通过标题来断言
        time.sleep(3)
        page_title = self.driver.title
        self.assertEqual(page_title,"自动化测试web项目")


    @file_data("test_data/test_login_bad.yaml")
    def test_2_bad_username(self,username,password):
        #用户登录的反例测试

        self.do_input(username,password)

        #断言
        time.sleep(2)
        rspmsg = self.driver.find_element_by_css_selector("#layui-layer2 > div.layui-layer-content.layui-layer-padding").text
        self.assertEqual(rspmsg,"用户名或密码错误")

    @file_data("test_data/test_login_no.yaml")
    def test_4_no(self,username,password):
        self.do_input(username,password)

        time.sleep(2)
        rspmsg = self.driver.find_element_by_id("layui-layer1").text
        self.assertEqual(rspmsg,"请输入用户名和密码")


if __name__ == '__main__':
    unittest.main()