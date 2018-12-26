# -*- coding:utf-8 -*-
# import json
# file_name = 'number.json'
# with open(file_name) as f_obj:
#
#     numbers = json.load(f_obj)
# print(numbers)
# import json
file_name = 'number.json'
with open(file_name) as item:
    # for it in item:
    #     print(it)

    numbers = json.load(item)
    print(numbers)