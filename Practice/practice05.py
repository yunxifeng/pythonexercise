'''
---三色球问题---
有红黄蓝三种颜色的球,红球3个,黄球3个,蓝球6个
将12个球混合放在一个盒子中,从中任意摸出8个球
计算摸出球的各种颜色搭配
'''
i = 0
for red in range(0,4):
    for yellow in range(0,4):
        for blue in range(2,7):
            if red + yellow + blue == 8:
                i += 1
                print("RED:{}".format(red))
                print("YELLOW:{}".format(yellow))
                print("BLUE:{}".format(blue))
                print("-" * 20)
print("共有{}种情况".format(i))