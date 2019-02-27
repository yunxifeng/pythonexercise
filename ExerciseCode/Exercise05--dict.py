# clear() 清除整个字典  返回None
dict1 = {'a':1,'b':2,'c':3}
dict1.clear()
print(dict1)

# copy()  复制字典
dict1 = {'a':1,'b':2,'c':3}
dict2 = dict1.copy()
print(dict2)

# fromkeys() 按照指定的序列为键创建字典,值都是一样的
list1 = ['a','b','c']
dict1 = {}.fromkeys(list1)
dict2 = {}.fromkeys(list1,3)
print(dict1,dict2)

# get() 根据键获取指定的值   找不到的键如果设默认值则返回默认值,如果没设默认值,则返回None
dict1 = {'a':1,'b':2,'c':3}
print(dict1.get('b'))
print(dict1.get('d'))
print(dict1.get('d',4))

# items() 将字典变成类似于元组的形式方便遍历
dict1 = {'a': 1, 'b': 2, 'c': 3}
for k, v in dict1.items():
    print(k, v)
for i in dict1.items():
    print(i)
print(dict1.items())

# pop()  弹出字典中指定元素  返回键所对应的值,如果键不存在,则返回默认值,如果键找不到,没设默认值,就会报错
dict1 = {'a':1,'b':2,'c':3}
print(dict1.pop('a'))
print(dict1)
print(dict1.pop('d',4))
print(dict1.pop('d'))

# popitem()  弹出字典的键值对  返回弹出的键和值
dict1 = {'d':4,'a':1,'b':2,'c':3}
print(dict1.popitem())

# setdefault()  在字典里添加一个元素
dict1 = {'d':4,'a':1,'b':2,'c':3}
print(dict1.setdefault('e',5))
print(dict1)

# update() 修改字典中的值
dict1 = {'d':4,'a':1,'b':2,'c':3}
dict1.update({'a':3,'b':4,'e':6})
print(dict1)
# dict1['d'] = 34
