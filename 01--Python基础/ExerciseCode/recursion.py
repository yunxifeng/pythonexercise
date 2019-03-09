# 类似于栈的先进后出模式
# 1.要有递推关系
# 2.要有临界值
def digui(num):
    print(num)
    # 临界值
    if num > 0:
        digui(num-1)
    else:
        print("*" * 20)
    print(num)
digui(3)

#汉诺塔问题
# 2^n-1
i = 0
def move(n,a,b,c):
    global i
    if n == 1:
        i += 1
        print("移动到", i, "次", a,"-->", c)
    else:
        move(n-1, a, c, b)
        move(1, a, b, c)
        move(n-1, b, a, c)


#
import os
def getdirpath(dirpath):
    total = 0
    # 获取所有文件
    allname = os.listdir(dirpath)
    for name in allname:
        fullpath = os.path.join(dirpath, name)
        if os.path.isfile(fullpath):
            total += os.path.getsize(fullpath)
        elif os.path.isdir(dirpath):
            total += getdirpath(fullpath)
    return total
