'''
定义一个学生类
1.姓名,年龄,成绩(语文,数学,英语,均为integer类型)
2.获取学生的姓名: get_name()返回类型:str
3.获取学生的年龄: get_age()返回类型:int
4.返回3门科目中最高的分数,get_course()返回类型:int
'''
class Student():
    def __init__(self, name, age, source):
        self.name = name
        self.age = age
        self.source = source

    def get_name(self):
        print(self.name)
        return

    def get_age(self):
        print(int(self.age))
        return

    def get_course(self):
        print(max(self.source))
        return


s = Student("jojo", 12, [80, 90, 98])
s.get_name()
s.get_age()
s.get_course()

