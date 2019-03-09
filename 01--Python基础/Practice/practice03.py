password = "123456"
times = 3
while times:
    input_password = input("请输入密码:")
    if "*" in input_password:
        print("密码中不能包含*")
    else:
        if input_password == password:
            print("密码正确")
            break
        else:
            times -= 1
            print("密码错误,您还有"+str(times)+"次机会")
