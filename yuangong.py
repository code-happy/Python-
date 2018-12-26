# -*- coding:utf-8 -*-
'''
其方法__init__()接受名、姓和年薪，并 将它们都存储在属性中。
编写一个名为 give_raise()的方法，它默认将年薪增加 5000 美元，但也能够接受其他的年薪增加量。
为 Employee 编写一个测试用例，其中包含两个测试方法：test_give_default_ raise()和 test_give_custom_raise()。
使用方法 setUp()，以免在每个测试方法中都创 建新的雇员实例。运行这个测试用例，确认两个测试都通过了。
'''

work_year = int(input('请输入你的工作年限'))
pay_year = 10

'''确定雇员的工作年限'''
class Empolyee(object):

    '''这个函数就是用来算工资的，默认年薪为10，pay_year = 10
    pay_raise ==5000
    每年的工资增加是5000美元，也可以接受增加是其他的数字'''

    def __init__(self,name,pay):
        self.name = name
        self.pay = pay

    def give_raise(self,pay):
        pay == 5000
        pay_raise_year = pay + work_year * 10


laowang = Empolyee()
laowang.give_raise('laowang',pay=5000)