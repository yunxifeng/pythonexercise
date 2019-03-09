'''
定义一个dict类: DictClass,完成如下功能
1.删除某个key: del_dict(key)
2.判断某个键是否在dict里,如果在,返回对应的值,不在则返回not found: get_dict()
3.返回键组成的list: get_key()
4.合并dict,并且返回合并后字典的values组成的list: update_dict()
'''


class DictClass():
    def __init__(self, dict1):
        self.dict1 = dict1

    def del_dict(self, key):
        if key not in self.dict1.keys():
            return "key不在字典里"
        else:
            del self.dict1[key]
            return "删除成功"

    def get_dict(self, key):
        if key in self.dict1.keys():
            return self.dict1[key]
        else:
            return "Not found"

    def get_key(self):
        l1 = []
        for i in self.dict1.keys():
            l1.append(i)
        return l1

    def update_dict(self, dict2):
        # 法一
        # self.dict1.update(dict2)
        # 法二
        # self.dict1 = dict(self.dict1, **dict2)
        # 法三
        d3 = {}
        for k,v in self.dict1.items():
            d3[k] = v
        for k,v in dict2.items():
            d3[k] = v
        l2 = []
        for i in d3.values():
            l2.append(i)
        return l2


d = DictClass({"one": 1, "two": 2, "three": 3})