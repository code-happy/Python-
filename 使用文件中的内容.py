# -*- coding:utf-8 -*-
with open('D:/pyIDE/filename/pi_digest.txt') as item:
    lines = item.readlines()

pi_string = ''
for line in lines:
    pi_string += line.rstrip()

print(pi_string)
print(len(pi_string))