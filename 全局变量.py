# -*- coding:utf-8 -*-
num = 100
nums = [11,22]
def test1():
    global num
    num += 100
def text2():
    nums.append(33)
print(num)
print(nums)
#这里就是打印一个变量

test1()
text2()
#这里是打印函数输出的结果
print(num)
print(nums)