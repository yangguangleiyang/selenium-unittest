import unittest
from ddt import ddt, data, unpack
import json

def read_phone():
    # li = []
    # with open("phone.txt","r",encoding="utf-8") as f:
    #     for line in f.readlines():
    #         li.append(line.strip("\n"))
    # return li

    #也可以选取json格式进行读取数据
    return json.load(open("phone_json.json","r"))


def read_userdata():
    li = []
    with open("user_data.txt","r",encoding="utf-8") as f:
        for line in f.readlines():
            li.append(line.strip("\n").split(","))
    return li
@ddt
class TestMyCase(unittest.TestCase):

    @data(*read_phone())
    def test_1(self,phone):
        print("测试手机号",phone)


    @data(*read_userdata())
    @unpack
    def test_2(self,username,password):
        print(username,password)


if __name__ == '__main__':
    unittest.main()