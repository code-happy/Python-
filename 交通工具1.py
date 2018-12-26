# -*- coding:utf-8 -*-
class Vehicle(object):
    """交通工具"""
    def __init__(self,name,load,speed,power):
        self.name = name
        self.load = load
        self.speed = speed
        self.power = power

    def run(self):
        print("%s地铁%s号线开通了-速度%s%d" %(self.name,self.load, self.speed,  self.power))

class Subway(Vehicle):
    def __init__(self,name,load,speed):
        self.name = name
        self.load = load
        self.speed = speed


    def test(self):
        print("%s地铁%s号线开通了-速度%s" % (self.name, self.load, self.speed))
line1 = Subway("长沙","1","210km/h")
line1.test()
