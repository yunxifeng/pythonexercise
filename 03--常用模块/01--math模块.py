import math
print(math)
# 1.math.celi()向上取整
print(math.ceil(5.1))
print(math.ceil(-5.1))
# 2.math.floor()向下取整
print(math.floor(5.1))
print(math.floor(-5.1))
# 查看系统关键字
import keyword
print(keyword.kwlist)
# 3.内置模块round()四舍五入
print(round(5.4))
# 4.math.sqrt()开平方,返回float类型
print(math.sqrt(4))
# 5.math.sin()/cos()/tan()三角函数,返回float类型
print(math.sin(0))
# 6.math.pow()计算一个数的n次方,返回float类型-->类似x ** n,返回int类型
print(math.pow(2, 32))
print(2 ** 32)
# 7.math.fabs()取绝对值,返回float类型-->类似内置函数abs(),返回类型由数据自身决定
print(math.fabs(-4))
print(abs(-4))
# 8.math.fsum(序列)求和,返回float类型-->类似内置函数sum(),返回类型由序列之和自身决定
print(math.fsum([1, 2, 3, 4]))
print(sum([1, 2, 3, 4.5]))
print(math.fsum({1, 2, 3, 3}))
print(math.fsum((1, 2, 3, 4)))
# 9.math.modf()拆分float类型数据为整数部分和小数部分组成元组,均是float类型,且小数部分在前
print(math.modf(-4.5))
# 10.math.copysign()将第二个数的符号赋给第一个数,返回第一个数的float类型
print(math.copysign(2, -3))
# 11.e,π
print(math.e)
print(math.pi)
