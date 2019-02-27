a = set()
print(a)
list1 = [1,2,3,4]
a = set(list1)
print(a)

# add()  向集合中添加元素
set1 = {5,1,2,3,4,'b','u'}
set1.add(6)
print(set1)

# clear()  清空集合
# copy()   复制集合
# pop()  随机弹出一个元素
a = {'a','b','f',4}
a.pop()
print(a)

# remove()  删除集合中的某个值,如果这个值不在集合中会报错
a = {'a','b','f',4}
a.remove(4)
print(a)
a.remove(4)

# discard()  删除集合中的某个值,如果这个值不在集合中什么也不做
a = {'a','b','f',4}
a.discard(4)
print(a)
a.discard(4)
print(a)

# difference()  差集
# difference_update()  区别就是第一个返回一个新的集合,第二个是把原来集合覆盖
set1 = {1,2,3,4,7}
set2 = {2,4,8,111,24}
set3 = set1.difference(set2)
print(set3)
print(set1)

set1 = {1,2,3,4,7}
set2 = {2,4,8,111,24}
set3 = set1.difference_update(set2)
print(set3)
print(set1)