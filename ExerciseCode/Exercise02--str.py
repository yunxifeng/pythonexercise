
# str连接操作
s1 = "I love"
s2 = "Python"
s3 = s1 + s2
print(s3)
print(s1 + " " + s2)
print("I love " + "Python")
# 字符串的乘法
s = "I love Python"
ss = s * 10
print(ss)
# 字符串可以当做列表来用
s = "I love Python"
print(s[0])
print(s[-1])
## 切片操作,左包含
ss = "I love Python"
print(ss[2:5])
print(id(ss))
print(id(ss[:]))
print(id(ss[:20]))
# TypeError: 'str' object does not support item assignment
# ss[1] = "A"
# 我们可以把str当做list使用,但是不能对str的下标元素进行赋值操作
# 所以下面的问题,我们用list解决

## 疑问与解决
## 切片操作: 首先,上述字符串ss占用一块内存空间,当我们对ss进行部分切片操作时,会产生一块新的内存空间,故原ss的id与切片操作后的ss的id是不一样的
## 但是,当我们对ss进行整片切片操作时,发现切片前后的ss的id是一样的,这可能意味着切片前后的ss都指向同一块内存空间,可以理解为"偷懒",两个变量指向同一块内存
## 这样会造成干扰,但是否是这样,我们需要通过实验来验证

## 解决上述疑问,证明部分切片和完整切片的区别
l = [1,2,3,4,5,6,7,8,9,100]
# 情形一
l1 = l[:6]
print(id(l))
print(id(l1))
# 情形二
l2 = l[:]
print(id(l))
print(id(l2))

# 结论: 对于str来说,切片前后均指向同一块内存,对于list来说,切片前后指向两块不同的内存空间,是两个完全不同的变量
# 这可能跟str的一些特性有关

# str.capitalize(): 将字符串的第一个字母变成大写,其他字母变小写。对于 8 位字节编码需要根据本地环境,返回字符串.
# 注:英文释义:capitalize:用大写字母写或印刷
# 特殊:当字符串[0]为空格和汉字等情况,则只会将后续字母全部小写
s = " I LOve Python"
print(s.capitalize())
# str.title(): 将每个单词的首字母大写,返回字符串
print(s.title())
# str.upper(): 将所有字母变为大写,返回字符串
print(s.upper())
# str.lower(): 将所有字母变为小写,返回字符串
print(s.lower())
# str.swapcase(): 大小写互换,返回字符串.注:英文释义:swap:交换
print(s.swapcase())

# len(str):计算字符串的长度,不属于字符串的内建函数
# len()统计长度是按照字符个数统计,一个汉字的长度为1
s1 = "I love Python"
s2 = "I love Python非常"
print(len(s1))
print(len(s2))

# str.find("*", m, n): 查找指定字符串,找不到返回-1,第一次找到返回第一次索引值
# 参数: - "*" : 需要查询的字符串, - "m" : 起始下标, - "n" : 结束下标, 注: [m, n)
# 注: 此处的m,n仅为了方便表达
s = "galgasflasgb"
print(s.find("g", 1, 3))
# str.index("*", m, n): 与find用法相同,区别: 找不到会提交Value异常,报错
# ValueError: substring not found
print(s.index("g", 1, 3))

# str.count("*"):计算字符串"*"出现次数,返回整型
print(s.count("g"))

# str.startswith("*"): 检测字符串是否以"*"开头,返回布尔值,注: 区分大小写
# str.endswith("*"): 检测字符串是否以"*"结尾,返回布尔值,注: 区分大小写
# 注意函数名单词拼写
s = " ajskblaksbf"
print(s.startswith("a"))
print(s.endswith("F"))
# str.isupper(): 检测所有字母是否是大写字母, 返回布尔值
s = " GGG喵HHH"
print(s.isupper())
# str.islower(): 检测所有字母是否是小写, 返回布尔值
print(s.islower())
# str.istitle(): 检测是否以指定标题显示(每个单词首字母大写)
ss = "I Love Python"
print(ss.istitle())
# str.isspace(): 检测是否是空字符串
s1 = ""
s2 = "  1233"
s3 = "      "
print(s3.isspace())
# str.isalpha(): 检测字符串是否是字母组成(不可以有空格,且汉字在英文字符包裹中也被当做字母处理),返回布尔值
s1 = "ilovepyt狗hon"
print(s1.isalpha())
# str.isalnum(): 检测字符串是否是由字母和数字组成(不可以有空格,且汉字在英文字符包裹中也被当做字母处理),返回布尔值
# 注: 纯字母或纯数字也可以
s = "i狗like123"
print(s.isalnum())


# 检测字符串是否由数字组成
# str.isdigit()
# str.isdecimal()
# str.isnumeric()
'''
isdigit()
True: Unicode数字，byte数字（单字节），全角数字（双字节），罗马数字
False: 汉字数字
Error: 无

isdecimal()
True: Unicode数字，全角数字（双字节）
False: 罗马数字，汉字数字
Error: byte数字（单字节）

isnumeric()
True: Unicode数字，全角数字（双字节），罗马数字，汉字数字
False: 无
Error: byte数字（单字节）

'''
s = '123'
print(s.isdigit())
print(s.isdecimal())
print(s.isnumeric())

print('='*20)

s = b'101100'
print(s.isdigit())
#print(s.isdecimal())
#print(s.isnumeric())

print('='*20)

# 百度digit，decimal， numeric的准确含义
s = '123.2'
print(s.isdigit())
print(s.isdecimal())
print(s.isnumeric())

print('='*20)

s = '三壹佰'
print(s.isdigit())
print(s.isdecimal())
print(s.isnumeric())

print('-'*20)

# 下面不是三个i的大写，是罗马数字的三
s = 'Ⅲ'
print(s.isdigit())
print(s.isdecimal())
print(s.isnumeric())


# str.split() 用指定字符切割字符串 , 返回由字符串组成的列表
s = '日照香炉生紫烟*疑是银河落九天*飞流直下三千尺'
list1 = s.split('*')
print(list1)
# str.splitlines()  以换行切割字符串
s = '''日照香炉生紫烟\n疑是银\n河落九天
    飞流直下三千尺'''
print(s.splitlines())

# str.join(list) 将列表按照指定字符串连接 返回的是字符串
list1 = ['日照香炉生紫烟', '疑是银河落九天', '飞流直下三千尺']
s = '*'.join(list1)
print(s)

# ljust()  指定字符串的长度,内容靠左边,不足的位置用指定字符填充,默认空格, 返回字符串
s = 'abc'
print(len(s))
print(s.ljust(5),'a')
# center()  指定字符串长度,内容居中,不足的位置用指定字符填充,默认空格, 返回字符串
print(s.center(5,'#'))
# rjust() 指定字符串的长度,内容靠右边,不足的位置用指定字符填充,默认空格, 返回字符串
print(s.rjust(5,'#'))

# strip() 去掉左右两边指定字符,默认是去掉空格
# lstrip()  去掉左侧指定字符,默认空格
# rstrip()  去掉右侧指定字符,默认空格

s = '   abc '
print('---'+s.strip()+'--')
print('---'+s+'--')
s = 'aaabcc'
print(s.lstrip('a'))
print(s.lstrip('b'))
print(s.rstrip('b'))
print(s.rstrip('c'))

# zfill() 指定字符串长度,内容靠右,不足的位置用0填充
s = 'abc'
print(s.zfill(5))

# maketrans()  生成用于字符串替换的映射表
# translate()  进行字符串替换
s = '今天晚上我吃的是小炒肉,可好吃了'
table = s.maketrans('小炒肉','大白菜')
print(table)
print(s.translate(table))
# 错误示例
s = '今天晚上我吃的是小炒肉,可好吃了'
table = s.maketrans('小炒肉','大白菜和粉条')
print(table)
print(s.translate(table))