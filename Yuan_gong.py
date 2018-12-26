# -*- coding:utf-8 -*-
'''
其方法__init__()接受名、姓和年薪，并 将它们都存储在属性中。
编写一个名为 give_raise()的方法，它默认将年薪增加 5000 美元，但也能够接受其他的年薪增加量。
为 Employee 编写一个测试用例，其中包含两个测试方法：test_give_default_ raise()和 test_give_custom_raise()。
使用方法 setUp()，以免在每个测试方法中都创 建新的雇员实例。运行这个测试用例，确认两个测试都通过了。
'''
import unittest
from yuangong import give_raise

class Empolyee(unittest.TestCase):

    def setUp(self):
        '''以免在每个测试方法中都创 建新的雇员实例。运行这个测试用例，确认两个测试都通过了'''

'''这个函数就是用来算工资的，默认年薪为十万，每年的工资增加是5000美元，也可以接受增加是其他的数字'''
    def test_give_default_raise(self):
        pay_rise = 5000
        default_raise = pay_rise *
        pay += 5000
    def test_give_custom_raise(self):
        pass