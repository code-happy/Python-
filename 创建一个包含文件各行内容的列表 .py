# -*- coding:utf-8 -*-
with open('D:/pyIDE/filename/pi_digest.txt') as item:
    lines = item.readlines()
    #创建一个包含文件各行内容的列表
"""
首先用lines这个变量来一行一行的打印出这个文件
然后用遍历的形式来访问这一行的数据
创建一个包含文件各行内容的列表 
"""
for line in lines:
    print(line.rstrip())