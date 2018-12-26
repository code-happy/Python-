# -*- coding:utf-8 -*-
# getuu = input('请输入你的生日')
#
# with open('D:/pyIDE/filename/pi_digest.txt') as item:
#     lines = item.readlines()
#
#
# if getuu in lines:
#     print('有了')
# else:
#     print('哎呀，抱歉，没有欸')
birthday = input('请输入你的名字')
with open('D:/pyIDE/filename/pi_digest.txt') as item:
    lines = item.readlines()

pi_string = ''
for line in lines:
    pi_string += line.rstrip()
if birthday in pi_string:
    print('233,有了')
else:
    print('emmm...，没有找到')


