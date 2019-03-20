import lianxi01_class
import lianxi02


print("请选择游戏\n1.数字游戏\n2.字母游戏")
game = input("请输入1或2: ")
if game == "1":
    game_num = lianxi01_class.GameNum()
    game_num.game(0, 0, 0)
elif game == "2":
    game_zimu = lianxi02.ZiMu()
    game_zimu.Ctl()
else:
    print("输入错误")