class Vehicle:  # 定义交通工具类
    def __init__(self, name, speed, load, power):
        self.name = name
        self.speed = speed
        self.load = load
        self.power = power

    def run(self):
        print('开动啦...')


class Subway(Vehicle):  # 地铁
    def __init__(self, name, speed, load, power, line):
        Vehicle.__init__(self, name, speed, load, power)  # 调用父类的构造函数（初始化）
        self.line = line

    def run(self):
        print('地铁%s号线欢迎您' % self.line)
        Vehicle.run(self)  # 调用父类的方法run()


line13 = Subway('中国地铁', '180m/s', '1000人/箱', '电', 13)
line13.run()
