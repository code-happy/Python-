# -*- coding:utf-8 -*-
"""编写一个 while 循环，询问用户为何喜欢编程。每当用户输 入一个原因后，都将其添加到一个存储所有原因的文件 """
reason = input("请输入你为什么喜欢编程")
count = 1
while count <= 1:
    with open('reason_book.txt','a',) as list:
        list.write('%s'%reason + '\n')
        # print('%s,你好'%name)
        if count == 1:
            break
else:
    print('你的输入有误，打扰了')