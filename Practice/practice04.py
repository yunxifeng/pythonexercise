'''
---求100-999之间的水鲜花数---
水仙花数: 如果一个三位数等于其他数字的立方和,则称这个数为水仙花数
'''
for i in range(100, 1000):
    temp = list(str(i))
    a = int(temp[0])
    b = int(temp[1])
    c = int(temp[2])
    if i == a ** 3 + b ** 3 + c ** 3:
        print(str(i)+"是水仙花数")