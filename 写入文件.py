# -*- coding:utf-8 -*-
filename = '学到的python知识.txt'

with open('学到的python知识.txt','w') as item:
    item.write('1，如何安装python'
               '2，输入和输出，input和print,注意input接收到的数据统一是字符串类型，如果需要改变，需要在input前面增加int(),输出print有格式化输出的要求，如果对应的数据是整数就用%d，字符串%s，浮点数就用%f，浮点数可以使用%*f的形式来确定保留几位数，其中的*就是保留的几位数'
               '3，python中常见的数据类型：int(),string(),float()'
                '4，列表，以中括号括起来，里面的数据类型可以整数，浮点数，字符串,数据可以改变，方法有增加，删除，改写，'
                '5，元组，以小括号括起来，里面的数据类型也可以是整数，浮点数，字符串，数据不能改变'
                '6，字典，以大括号括起来，里面的数据是以键值对的形式存在，有键就有值'
                '7，函数，以def作为关键字，函数名结束后以冒号结尾'
                '8，类，以class定义，类名要求满足驼峰命名法，符和新式类，'
                '9，继承，子类继承父类的属性和方法,除开父类的私有方法，子类可以通过间接访问的形式访问父类的方法，子类可以成为父类，子类的子类拥有父类和爷爷类的方法'
                '10，封装，封装是实现面向对象的基础，是指对外隐藏对象内部的属性和实现细节，只提供相应的接口和方法进行交互。')