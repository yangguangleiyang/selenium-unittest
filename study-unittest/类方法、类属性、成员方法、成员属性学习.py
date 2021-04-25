import unittest

#各个成员之间self对象是不一样的

class TestMyCase(unittest.TestCase):
    step = 1

    ipadder = "192.168.1.1"       # 类属性
    name = None
    @classmethod
    def setUpClass(cls):          #类方法
        print("-----setupclass")

    @classmethod
    def tearDownClass(cls):
        print("----setupclass")

    def setUp(self):
        print("----setup")

    def tearDown(self):
        print("----teardown")

    def test_1(self):                        #成员方法
        print("do test1",TestMyCase.ipadder)
        TestMyCase.name = "Sigper"

    @unittest.skip("test_2暂时不执行此用例")
    def test_2(self):
        print("do test2",TestMyCase.name)

    # @unittest.skipIf(2>1,"因为2>1,所以跳过")
    @unittest.skipIf(print("skip",step),"因为step等于1，所以跳过")     #skip装饰器在执行所有之前最先执行，包括setupclass
    def test_3(self):
        print("do test2",TestMyCase.name)

if __name__ == '__main__':
    unittest.main()