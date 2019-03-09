'''
游戏编程
1.场景范围: 0<=x<=10, 0<=y<=10
2.游戏生成一只乌龟和十条鱼
3.移动方向均随机
4.乌龟的最大移动能力是2,鱼的最大移动能力是1
5.当移动到场景边缘,自动反方向移动
6.乌龟初始化体力是100点(上限)
7.乌龟每移动一次,体力消耗1点
8.当乌龟和鱼重叠,乌龟吃掉鱼,乌龟体力增加20
9.鱼不计算体力
10.当乌龟体力值为0或者鱼的数量为0时,游戏结束
'''


import random as r


class Turtle(object):
    def __init__(self):
        # 乌龟体力
        self.power = 100
        # 初始化乌龟的位置
        self.x = r.randint(0, 10)
        self.y = r.randint(0, 10)

    # 移动
    def move(self):
        new_x = self.x + r.choice([1, -1, 2, -2])
        new_y = self.y + r.choice([1, -1, 2, -2])

        # 判断是否超出边界
        if new_x < 0:
            self.x = 0 - new_x
        elif new_x > 10:
            self.x = 20 - new_x
        else:
            self.x = new_x

        if new_y < 0:
            self.y = 0 - new_y
        elif new_y > 10:
            self.y = 20 - new_y
        else:
            self.y = new_y
        # 体力
        self.power -= 1
        return self.x, self.y

    def eat(self):
        self.power += 20
        if self.power > 100:
            self.power = 100


class Fish(object):
    def __init__(self):
        self.x = r.randint(0, 10)
        self.y = r.randint(0, 10)

    # 移动
    def remove(self):
        new_x = self.x + r.choice([1, -1])
        new_y = self.y + r.choice([1, -1])
        # 判断是否超出边界
        if new_x < 0:
            self.x = 0 - new_x
        elif new_x > 10:
            self.x = 20 - new_x
        else:
            self.x = new_x

        if new_y < 0:
            self.y = 0 - new_y
        elif new_y > 10:
            self.y = 20 - new_y
        else:
            self.y = new_y

        return self.x, self.y


turtle = Turtle()
fish = []
for i in range(10):
    new_fish = Fish()
    fish.append(new_fish)

while True:
    if not len(fish):
        print("鱼被吃完了,游戏结束")
        break
    if not turtle.power:
        print("乌龟没有体力了,游戏结束")
        break
    # 判断位置是否相同
    position = turtle.move()
    # 在迭代器中删除列表元素是很危险的,经常会出现一些意想不到的问题,因为迭代器是直接引用原列表的数据进行操作
    # 所以这里把列表拷贝一份传给迭代器,然后对原列表进行操作
    for each_fish in fish[:]:
        if each_fish.remove() == position:
            turtle.eat()
            fish.remove(each_fish)
            print("有一条鱼被吃掉了")