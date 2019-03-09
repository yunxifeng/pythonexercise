'''
定义一个list类ListInfo
1.添加元素(必须是数字或者字符串): add_key()
2.取值: get_key()
3.列表合并: update_list(list)
4.删除并返回最后一个元素: del_key()
'''


class ListInfo():
    def __init__(self, list_1):
        self.list_1 = list_1

    def add_key(self, value):
        if isinstance(value, (int, str)):
            self.list_1.append(value)
            return self.list_1
        else:
            return "不符合"

    def get_key(self, index):
        if abs(index) <= len(self.list_1):
            return self.list_1[index]
        else:
            return "超出list的长度"

    def update_list(self, list_2):
        self.list_1.extend(list_2)
        return self.list_1

    def del_key(self):
        if len(self.list_1) >= 0:
            return self.list_1.pop(-1)
        else:
            return "list为空"


l = ListInfo([1, 2, 3, 4, 5])