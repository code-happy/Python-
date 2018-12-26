# -*- coding:utf-8 -*-
'''
喜欢的数字：
编写一个程序，提示用户输入他喜欢的数字，并使用 json.dump()将这个数字存储到文件中。
再编写一个程序，从文件中读取这个值，并打 印消息“I know your favorite number! It’s _____.”。
'''
import json
file_name = 'shizi.json'
number = input('请输入你喜欢的数字')
# number = int(input('请输入你喜欢的数字'))
with open(file_name,'a') as item:
    json.dump(number,item)

# with open(file_name,'a') as item:
    json.load(number)
    # butter = number
    print('我记得你个龟孙' + number + '!')