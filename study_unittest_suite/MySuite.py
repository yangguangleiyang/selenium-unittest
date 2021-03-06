import unittest

from study_unittest_suite import MyTestCase3_model
from study_unittest_suite.MyTestCase1 import TestMyCase1
from study_unittest_suite.MyTestCase2 import TestMyCase2

suite = unittest.TestSuite()

#简单的方法执行测试用例
# cases = [
#     TestMyCsae1("test_1"),
#     TestMyCsae1("test_2"),
#     TestMyCsae2("test_3"),
#     TestMyCsae2("test_4")
# ]
# suite.addTests(cases)

#使用加载器执行测试用例     通过用例
# suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestMyCsae1))
# suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestMyCsae2))

#换一种方法   通过名字
# suite.addTests(unittest.TestLoader().loadTestsFromNames(["MyTestCase1.TestMyCase1","MyTestCase2.TestMyCase2"]))


#再换一种方法   通过模块执行整个模块的用例
# suite.addTests(unittest.TestLoader().loadTestsFromModule(MyTestCase3_model))

#执行当前目录下的所有用例
module_path = "./"
discover = unittest.defaultTestLoader.discover(start_dir=module_path,pattern="MyTestCase*.py")


runner = unittest.TextTestRunner()

runner.run(discover)


#HTMLTestRunner  来生成测试报告
#下载HTMLTestRunner.py文件
#他是python2语法写出来一个库 需要转换成python3