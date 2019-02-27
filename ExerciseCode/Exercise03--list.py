# append()  向列表末尾添加新元素    返回值None
list1 = [1,2,3,4,5]
print(id(list1))
list1.append(6)
print(id(list1))
print(list1)

# copy()  复制列表
list1 = [1,2,3,4,5]
list2 = list1.copy()
print(list2)
print(id(list1))
print(id(list2))

# count() 计算某个元素在列表中出现的次数
list1 = [1,1,2,5,1,3]
print(list1.count(1))

# extend() 将一个列表继承另一个列表
list1 = [1,2,3,4,5]
list2 = [6,7,8,9,10]
print(id(list1))
list3 = list1.extend(list2)
print(id(list1))
print(list1)
print(list2)
print(list3)
print(list1+list2)

# index()  获取值在列表中的索引
list1 = [1,3,2,3,4,5,3]
print(list1.index(3))
print(list1.index(3,2,5))

# insert() 在指定位置前插入元素   2个参数
list1 = [1,2,3,4,5]
list1.insert(2,9)
print(list1)

# pop()  根据索引弹出列表内一个元素,不给索引默认弹出最后一个  返回弹出的那个值
list1 = [1,2,3,4,5]
#list1.pop(2)
#print(list1)
print(list1.pop())
print(list1)
print(list1.pop())
print(list1)
list1.pop()
print(list1)
list1.pop()
print(list1)
list1.pop()
print(list1)
list1.pop()

# remove()  移除列表中指定的值   返回None
list1 = ['a','b','c','d']
print(list1.remove('b'))
print(list1)

# reverse()  列表反转
list1 = [1,2,3,4]
print(id(list1))
list1.reverse()
print(id(list1))
print(list1)

# sort()  排序  默认从小到大
list1 = [5,2,4,6,1,9]
list1.sort()
print(list1)
# 从大到小
list1.sort(reverse=True)
print(list1)

