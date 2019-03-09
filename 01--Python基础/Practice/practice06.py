'''
---管理用于登陆系统的用户信息---
'''
user_pass = {}

def create_user(username, password):
    if username in user_pass.keys():
        print("这个用户已经被注册了")
    else:
        user_pass[username] = password
        print("注册成功")
create_user("高静", 123456)
print(user_pass)

def login_user(username, password):
    if username not in user_pass.keys():
        print("你不是会员")
    elif password != user_pass[username]:
        print("密码错误")
    else:
        print("登陆成功")
login_user("高静", 123456)