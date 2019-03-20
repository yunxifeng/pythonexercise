class ZiMu():
    # 打印字母"A"
    def A(self):
        for i in range(1, 5):
            for k in range(6-i):
                print(" ", end="")
            for j in range(1, i+1):
                if i == 1 or i == 3 or j == i or j == 1:
                    print("*", end=" ")
                else:
                    print(" ", end=" ")
            print()
    # 打印字母"B"
    def B(self):
        for i in range(1, 4):
            for j in range(1, 4):
                if i == 1 or i == 4 or j == 1:
                    if j < 3:
                        print("*", end=" ")
                elif j == 3:
                    if i ==2 or i ==3:
                        print("*", end=" ")
                else:
                    print(" ", end=" ")
            print()
        for i in range(1, 5):
            for j in range(1, 4):
                if i == 1 or i == 4 or j == 1:
                    if j < 3:
                        print("*", end=" ")
                elif j == 3:
                    if i ==2 or i ==3:
                        print("*", end=" ")
                else:
                    print(" ", end=" ")
            print()
    # 打印字母"C"
    def C(self):
        for i in range(1, 5):
            for j in range(1, 4):
                if i == 1 or i == 4:
                    if j == 1:
                        print(" ", end=" ")
                    else:
                        print("*", end=" ")
                elif j == 1:
                    if i == 2 or i == 3:
                        print("*", end=" ")
                else:
                    print(" ", end=" ")
            print()
    # 打印字母"D"
    def D(self):
        for i in range(1, 5):
            for j in range(1, 4):
                if i == 1 or i == 4 or j == 1:
                    if j < 3:
                        print("*", end=" ")
                elif j == 3:
                    if i ==2 or i ==3:
                        print("*", end=" ")
                else:
                    print(" ", end=" ")
            print()
    # 控制函数
    def Ctl(self):
        while True:
            Q = input("请输入A-D中的一个:")
            print("输入-1退出")
            if Q == "-1":
                break
            if Q == "A":
                self.A()
            elif Q == "B":
                self.B()
            elif Q == "C":
                self.C()
            elif Q == "D":
                self.D()
            else:
                print("输入错误!")



if __name__ == "__main__":
    zimu = ZiMu()
    zimu.A()