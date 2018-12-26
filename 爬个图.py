# -*- coding:utf-8 -*-
import requests
response = requests.get("http://www.meizitu.com/a/5561.html/01.jgp")
with open('01.jgp','wb') as fb:
    fb.write(response.content)
