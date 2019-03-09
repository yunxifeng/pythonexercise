'''
定义一个set的操作类
1.添加集合元素: add_setinfo()
2.集合的交集: get_intersection()
3.集合的并集: get_union()
4.集合的差集: get_difference()
'''

class SetInfo():
    def __init__(self, my_set):
        self.sett = my_set

    def add_setinfo(self, set_value):
        self.sett.add(set_value)
        return self.sett

    def get_intersection(self, interinfo):
        if type(interinfo) == set:
            # 或者 if isinstance(interinfo, set):
            return self.sett & interinfo
        else:
            return "请输入集合"

    def get_union(self, unioninfo):
        if type(unioninfo) == set:
            return self.sett | unioninfo
        else:
            return "请输入集合"

    def get_difference(self, diffinfo):
        if type(diffinfo) == set:
            return self.sett - diffinfo
        else:
            return "请输入集合"
