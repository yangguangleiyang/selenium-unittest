import unittest
from ddt import ddt, data, unpack,file_data
import json



@ddt
class TestMyCase(unittest.TestCase):

    # @file_data("phone.yaml")
    # def test_1(self,phone):
    #     print("测试手机号",phone)


    @file_data("user_data_yaml.yaml")
    def test_2(self,username,password):
        print(username,password)


if __name__ == '__main__':
    unittest.main()