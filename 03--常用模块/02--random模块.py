import random
# 1.random.random()获取[0,1)之间的随机小数
print(random.randint(1, 2))
# 2.random.randint(m, n)获取[m, n]之间的随机整数
print(random.randint(1, 2))
# 3.random.randrange(m, n, [step])获取[m,n)之间的随机整数,可指定步长
for i in range(1, 5):
    print(random.randrange(1, 10, i))
# 4.random.choice(序列)随机获取序列中的值
print(random.choice(range(10)))
# 5.random.shuffle(序列)随机打乱序列,返回None
print(random.shuffle([1, 2, 3]))
# 6.random.uniform(m, n)随机获取[m,n)之间的数,包括小数
print(random.uniform(1,2))