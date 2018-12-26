class Vehicle:

    def __init__(self, name, speed, load, power):
        self.name = name
        self.speed = speed
        self.load = load
        self.power = power

    def run(self):
        print("%s地铁今天开通了" % self.name)


class Subway(Vehicle):  # 地铁
    def __init__(self, name, speed, load, power, line):
        #重写，增加line
        super().__init__(name, speed, load, power)
        self.line = line

    def test(self):
        print('%s地铁%s号线欢迎您，以%s为动力，时速%s' % (self.name,self.line,self.power,self.speed))
        #指明调用的位置
        super(Subway, self).run()


line1 = Subway('长沙', '210km/s', '一', '电', 2)
line1.test()
