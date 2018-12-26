# -*- coding:utf-8 -*-
"""访客名单：编写一个 while 循环，提示用户输入其名字。
用户输入其名字后， 在屏幕上打印一句问候语，并将一条访问记录添加到文件 guest_book.txt 中。确保这个 文件中的每条记录都独占一行 """
name = input("请输入你的名字")
count = 1
while len(name) >= 2 and count <= 1:
    with open('guest_book.txt','a',) as list:
        list.write('%s'%name + '\n')
        print('%s,你好'%name)
        if count == 1:
            break
else:
    print('你的输入有误，打扰了')