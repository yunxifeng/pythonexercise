# 01--简单图形打印
'''
* * * * *
* * * * *
* * * * *
* * * * *
'''
for i in range(4):
    print("* " * 5)

print("-" * 20)

# 02--利用双层for循环更改上面的案例
# 打印一行*号
for i in range(4):
    for j in range(5):
#print默认自动换行
#可以通过end参数控制
        print("* " , end="")
#此处print()控制换行
    print()

print("- " * 20)

# 03--利用单层for循环更改上面的案例
for i in range(4):
    print("* " * 5)

print("- " * 20)

# 04--简单图形打印
'''
* * * * *
*       *
*       *
* * * * *
思路:1.用for循环控制打印行
     2.判断:第一行和最后一行整行打印,第一列和最后一列整行打印,否则打印空格
'''
for i in range(4):
    if i == 0 or i ==3:
        print("* " * 5)
    else:
        print("*       *")

print("- " * 20)

# 05--更改上面的案例
for i in range(4):
    if i == 0 or i ==3:
        print("* " * 5)
    else:
        for j in range(5):
            if j ==0 or j ==4:
                print("* ", end="")
            else:
                print("  ",end="")
        print()

print("- " * 20)

# 06--简单图形打印
#打印三角形
'''
*
* *
* * *
* * * *
* * * * *
'''
#一行一行地打印,首先考虑for循环
#观察规律:首先要打5行,用到一个for循环,然后每行打印"行数"个,很明显是有规律的,可以再嵌套一个for循环
for i in range(5):
    for j in range(i+1):
        print("* ",end="")
    print()

print("- " * 20)

# 07--简单图形打印
#打印空心三角形
'''
*
* *
*   *
*     *
* * * * *     
'''
# 方法一:自己写的
for i in range(5):
    if i==0 or i==1 or i==4:
        print("* " * (i+1))
    else:
        for j in range(i+1):
            if j==0 or j==i:
                print("* ",end="")
            else:
                print("  ",end="")
        if i==2 or i==3:
            print()
#方法二:老师写的



print("- " * 20)

# 08--简单图形打印
#打印倒立三角形
'''
* * * * *
* * * *
* * *
* *
*
'''
for i in range(5):
    print("* " * (5-i))
#或者
for i in range(5):
    for j in range(5-i):
        print("* ", end="")
    print()
#或者
#使用参数控制range结果
#表示从5到0,每次减1
for i in range(5, 0, -1):
    for j in range(i, 0, -1):
        print("* ", end="")
    print()

# 09--简单图形打印
#打印空心倒立三角形
'''
* * * * *
*     *
*   *
* *
*
'''
for i in range(5):
    for j in range(5-i):
        if i==0:
            print("* ",end="")
            continue
        if j==0 or j==4-i:
            print("* ",end="")
        else:
            print("  ",end="")
    print()

print("- " * 20)

# 10--简单图形打印
#打印正三角形
'''
    *
   * *
  * * *
 * * * *
* * * * *
'''
for i in range(5):
    for j in range(5-i):
        print(" ",end="")
    for k in range(i+1):
        print("* ",end="")
    print()

print("- " * 20)

# 11--简单图形打印
#打印空正三角形
'''
    * 
   * * 
  *   * 
 *     * 
* * * * * 
'''
for i in range(1,6):
    for k in range(1,6-i):
        print(end=" ")
    for j in range(6-i,6):
        #逻辑混乱,不推荐
        if i==5 or j==6-i or j==5:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()