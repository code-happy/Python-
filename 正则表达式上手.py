# -*- coding:utf-8 -*-
import requests
import re

response = requests.get("https://book.douban.com").text
patter = re.compile("",response,re.S)
results = re.findall (patter,response)
print(results)
for result in results:
    print(result)