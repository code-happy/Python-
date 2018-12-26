# -*- coding:utf-8 -*-
import json
numbers = [1,2,3,5,7,9,6]

file_name = 'number.json'
# file_name = 'number.txt'
with open(file_name,'w') as item:
    json.dump(numbers,item)