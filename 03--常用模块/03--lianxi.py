import math
import random

# 比较输入的数与随机数的大小,若大于,则分别输出三位数的个十百位;若等于,则提示中奖,记100分;
# 若小于,则将120个字符写入文本文件(每一条字符串长度为12,单独占一行,前四个是字母,后八个是数字)
num = input("请输入一个三位数:")
random_num = random.randrange(100, 1000)
if num.isdigit() & 100 <= int(num) <= 999:
    num = int(num)
    if num > random_num:
        print(random_num)
    if num == random_num:
        print(random_num)
    if num < random_num:
        print(random_num)
else:
    print("请按规定输入")