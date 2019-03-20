# 将lianxi01.py中的函数封装成类
import random
import math


class GameNum():
    def line(self):
        str_num = ""
        for i in range(4):
            str_s = chr(random.randrange(97, 123))
            str_num += str_s
        for i in range(8):
            str_num += str(random.randrange(0, 10))
        return str_num

    def game(self, score, total, win):
        while True:
            random_num = random.randrange(100, 1000)
            num = input("请输入一个三位数, 输入-1退出游戏:")
            if num == "-1":
                print("游戏结束")
                break
            if num.isdigit() and 100 <= int(num) <= 999:
                total += 1
                print("有效输入累计次数:{0}".format(total))
                num = int(num)
                if num > random_num:
                    # 方法一
                    # bai = random_num % 100
                    # shi = random_num % 100 // 10
                    # ge = random_num % 100 % 10
                    # print("个位是{0},十位是{1},百位是{2}".format(ge, shi, bai))
                    # 方法二
                    bai = math.floor(random_num / 100)
                    shi = math.floor(random_num % 100 / 10)
                    ge = random_num % 100 % 10
                    print("你输入的数字过大,该随机数{0}的个位是{1},十位是{2},百位是{3}".format(random_num, ge, shi, bai))
                if num == random_num:
                    win += 1
                    score += 100
                    print("牛逼啊,目前得分{0}".format(score))
                    print("中奖概率为:{:.2f}%".format((win / total) * 100))
                if num < random_num:
                    print(random_num)
                    for i in range(10):
                        # 当实例化后,通过对象调用时
                        str_line = self.line()
                        # 当通过类直接调用时
                        # str_line = GameNum.line(0)
                        with open(r'str_num.txt', 'a') as f:
                            f.write(str_line + '\n')
            else:
                print("请按规定输入")

# 程序入口, 也叫调试代码
if __name__ == "__main__":
    score = 0
    total = 0
    win = 0
    # 实例化类,对象调用, 对象会自动作为参数传入函数
    game_num =GameNum()
    game_num.game(score, total, win)

    # 直接通过类调用,类不会将自身作为参数传入参数
    # 此处的'0'代表GameNum这个类自身
    # GameNum.game(0, score, total, win)


