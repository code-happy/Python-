# -*- coding:utf-8 -*-
"""
json的用法：就是调用json.dump()和json.load()方法，
dump()方法是把获取的数据放进去，load()方法是把获取的数据拿出来
调用这两个方法，都需要传递两个参数，一个是需要传的那个，另一个是传到哪里的参数
"""
import json
username = input("What is your name? ")
filename = 'username.json'
with open(filename, 'w') as item:
    '''
    这里调用的dump方法就传递了两个参数，一个是用户输入的参数username，
    另一个item就是filename的别名，也就是把这个username参数传递到username.json文件中，做一个参数储存
    还有就是load()方法了，load方法用来把json中的数据拿出来，但是这个函数的参数可以只传一个，
    那就是 username = json.load(item)，这种，把整个文件中的数据全部拿出来
    '''
    json.dump(username, item)
    print("We'll remember you when you come back, " + username + "!")