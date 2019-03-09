'''
定义一个门票系统
1.门票的原价是100
2.周末的时候涨价20%
3.小孩子半票
4.计算2个成人和一个小孩的平日票价
'''


class Ticket():
    def __init__(self, weekend = False, child = False):
        self.exp = 100
        if weekend:
            self.inc = 1.2
        else:
            self.inc = 1

        if child:
            self.discount = 0.5
        else:
            self.discount = 1

    def cal_price(self, num):
        return self.exp * self.inc * self.discount * num


adult = Ticket()
child = Ticket(child=True)
print("两个成年人和一个小孩的票价是{0}".format(adult.cal_price(2) + child.cal_price(1)))