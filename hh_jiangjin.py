# -*- coding:utf-8 -*-
'''

利润 (I) ：
低于或等于 10 万元时，奖金可提 10%；
高于 10万元，低于 20 万元时，低于 10 万元的部分按 10%提成，高于 10
万元的部分，可提成 7.5%；
20 万到 40 万之间时，高于 20 万元的部分，可提成 5%；
40 万到 60 万之间时，高于 40 万元的部分，可提成 3%；
60 万到 100 万之间时，高于 60万元的部分，可提成 1.5%，
高于 100万元时，
超过 100万元的部分按 1%提成，
从键盘输入当月利润 I ，求应发放奖金总数
'''
class TiCheng:

    def jisuan(self,I):
        if I <= 100000:
            a = I*0.1
            print(a)
        elif I > 100000 and I <= 200000:
            b = (I-100000)*0.075 + 100000*0.1
            print(b)
        elif I > 200000 and I <= 400000:
            c = (I - 200000)*0.05 + 100000*0.075 + 100000*0.1
            print(c)
        elif I > 400000 and I <= 600000:
            d = (I-400000)*0.03 + 200000*0.05 + 100000*0.075 + 100000*0.1
            print(d)
        elif I > 600000 and I <= 1000000:
            e = (I-600000)*0.015 + 200000*0.03 + 200000*0.05 + 100000*0.075 + 100000*0.1
            print(e)
        else:
            f = (I-1000000)*0.01 + 400000*0.015 +200000*0.03 + 200000*0.05 + 100000*0.075 + 100000*0.1
            print(f)

shiji = TiCheng() 
shiji.jisuan(200000)




