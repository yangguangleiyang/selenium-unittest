
from selenium import webdriver


driver_path=r"C:\chromedriver_win32\chromedriver.exe"

driver=webdriver.Chrome(executable_path=driver_path)

# driver.get("http://baidu.com")

#id定位
# driver.find_element_by_id("kw").send_keys("seleniium")

#link_text 超链接
# driver.find_element_by_link_text("新闻").click()
# driver.find_element_by_partial_link_text("新").click()  #适用于部分字体变，个别字体不变，前提是
#不能再有其他“新”字出现



#Xpath定位
# driver.implicitly_wait(5)   implicitly_wait(5)属于隐式等待，5秒钟内只要找到了元素就开始执行，5秒钟后未找到，就超时；
driver.get("https://passport.meituan.com/account/unitivelogin?")
driver.find_element_by_xpath('//*[@id="login-email"]').send_keys("13718627413")
driver.find_element_by_xpath('//*[@id="login-password"]').send_keys("123456")
driver.find_element_by_xpath('//*[@id="J-normal-form"]/div[5]/input[5]').click()

#tag_name  通过标签名来定位