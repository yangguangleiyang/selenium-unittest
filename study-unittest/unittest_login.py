import unittest
from selenium import webdriver
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By


class LoginTestCase(unittest.TestCase):
    def do_input(self,username=None,password=None,randcode=None):
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
    def test_1_normal(self):

        self.do_input("admin","123456","123")

        # 断言：通过标题来断言
        time.sleep(3)
        page_title = self.driver.title
        self.assertEqual(page_title,"自动化测试web项目")

    def test_2_bad_username(self):
        self.do_input("admin1","123456","123")
        time.sleep(2)
        rspmsg = self.driver.find_element_by_css_selector("#layui-layer2 > div.layui-layer-content.layui-layer-padding").text
        self.assertEqual(rspmsg,"用户名或密码错误")

    def test_3_bad_password(self):
        self.do_input("admin","123","123")
        # element_text = ""
        # try:
        #     element = WebDriverWait(self.driver,10).until(
        #         expected_conditions.presence_of_element_located(By.CSS_SELECTOR,'#layui-layer2 > div.layui-layer-content.layui-layer-padding')
        #     ).text
        #     element_text = element.text
        # except Exception as e:
        #     print(e)
        #
        # self.assertEqual(element_text,"用户名或密码错误")

        time.sleep(2)
        rspmsg = self.driver.find_element_by_css_selector("#layui-layer2 > div.layui-layer-content.layui-layer-padding").text
        self.assertEqual(rspmsg,"用户名或密码错误")

    def test_4_None_username(self):
        self.do_input(password="123456",randcode="123")
        time.sleep(2)
        rspmsg = self.driver.find_element_by_id("layui-layer1").text
        self.assertEqual(rspmsg,"请输入用户名和密码")


if __name__ == '__main__':
    unittest.main()