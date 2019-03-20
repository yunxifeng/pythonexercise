import math
import random

# 比较输入的数与随机数的大小,若大于,则分别输出三位数的个十百位;若等于,则提示中奖,记100分;
# 若小于,则将120个字符写入文本文件(每一条字符串长度为12,单独占一行,前四个是字母,后八个是数字)
# ASCII码转换字符: 内置函数:chr()
# 字符转换ASCII码: 内置函数:ord()


def line():
    str_num = ""
    for i in range(4):
        str_s = chr(random.randrange(97, 123))
        str_num += str_s
    for i in range(8):
        str_num += str(random.randrange(0, 10))
    return str_num


def game():
    score = 0 # 初始分数
    total = 0 # 有效输入累计次数
    win = 0 # 中奖次数
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
                    str_line = line()
                    with open(r'str_num.txt', 'a') as f:
                        f.write(str_line+'\n')
        else:
            print("请按规定输入")


# 程序入口, 也叫调试代码
if __name__ == "__main__":
    game()