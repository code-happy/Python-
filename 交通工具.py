# -*- coding:utf-8 -*-
class Vehicle(object):
    """交通工具"""
    def __init__(self,name,speed,load,power):
        self.name = name
        self.speed = speed
        self.load = load
        self.power = power
        print("%s地铁%s号线开通了-速度%s"%(self.name,self.line,self.speed))

    def __str__(self):
        return ('%s今天开通'%self.name)

class Subway(Vehicle):
    def __init__(self,name,speed,line):
        self.name = name
        self.speed = speed
        self.line = line
        super().__init__(self)


    def test(self):
        print("%s地铁%s号线开通了-速度%s"%(self.name,self.line,self.speed))
line1 = Subway("cs","210km",'d')
line1.test()
line1 = Subway("ff")
line1.run()