'''
---猜数字---
三次机会
'''
import random

secret = random.randint(1, 100)#生成一个1-100的随机数
times = 3#三次机会

while times:
    num = input("请输入:")
    if num.isdigit():
        tmp = int(num)
        if tmp == secret:
            print("猜对了!!!")
            break
        elif tmp < secret:
            print("太小了!!!")
            times -= 1
        else:
            print("太大了!!!")
            times -= 1
    else:
        print("请输入数字!!!")
print("游戏结束")