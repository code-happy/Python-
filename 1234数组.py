# -*- coding:utf-8 -*-
import random
# number = [1,3,4,5,6]
# for i in number:
#     print(i)
list = [1, 2, 3, 4]
slice = random.sample(list, 2)  #从list中随机获取3个元素，作为一个片断返回
print(slice)
