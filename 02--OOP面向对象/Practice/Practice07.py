'''
定义一个点(Point)和直线(Line)类,使用getLen()方法获取两点构成直线的长度
'''


import math


class Point(object):
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y


class Line(object):
    def __init__(self, p1, p2):
        self.x = p1.get_x() - p2.get_y()
        self.y = p1.get_y() - p2.get_y()

    def get_len(self):
        line_length = math.sqrt(self.x ** 2 + self.y ** 2)
        return line_length


p1 = Point(2, 3)
p2 = Point(4, 5)
l = Line(p1, p2)
print(l.get_len())