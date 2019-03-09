# Python数据类型的内置结构--list
- help(list)
- list:
    - append() : 向列表末尾添加新元素,返回值None
    - copy():  浅复制,传值
    - count(*): 计算某个元素在列表中出现的次数
    - l1.extend(iterable): 将一个列表继承另一个可迭代的序列(l1后续追加iterable序列),返回值是None
    - l1.index(*,start,stop) : 获取值在列表中的索引,起止参数可选
    - insert(index, *) 在指定位置前插入元素 , 2个参数
    - pop(index):  根据索引弹出列表内一个元素,不给索引默认弹出最后一个  返回弹出的那个值
    - remove(*) : 移除列表中指定的值   返回None
    - l.reverse() : 列表反转
    - sort()  排序  默认从小到大(reverse=False), 从大到小则参数reverse=True
    