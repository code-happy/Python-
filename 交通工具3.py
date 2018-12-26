class Vehicle:

    def __init__(self, name, speed, load = 1, power = "电"):
        self.name = name
        self.speed = speed


    def run(self):
        print("%s地铁今天开通了" % self.name)


class Subway(Vehicle):  # 地铁

    def test(self):
        print('%s地铁一号线欢迎您，，时速%s' % (self.name,self.speed))
line1 = Subway('长沙', '210km/s')
line1.run()
line1.test()
