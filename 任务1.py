def a():
    sum = 0
    for i in range(1,11):
        print("请输入第",i,"个数字：")
        num = int(input())
        sum += num
    print(sum)
def a2():
    sum = 0
    max = 0
    for i in range(1,11):
        print("请输入第",i,"个数字：")
        num = int(input())
        sum += num
        if num > max:
            max = num
    avr = sum/10
    print("最大值:", max)
    print("10个数的和:",sum)
    print("平均数:",avr)
def a3():
    import random
    i = random.randint(50, 150)
    print(i)
def a4():
    a = float(input("请输入第一条边长："))
    b = float(input("请输入第二条边长："))
    c = float(input("请输入第三条边长："))
    if ((a + b) > c) & ((a + c) > b) & ((b + c) > a) & ((a - b) < c) & ((a - c) < b) & ((b - c) < a) & ((b - a) < c) & (
            (c - a) < b) & ((c - b) < a):
        if a == b == c:
            print("等边三角形")
        elif a == b or a == c or b == c :
            print("等腰三角形")
        elif a*a+b*b == c*c or c*c+b*b == a*a or a*a+c*c == b*b:
            print("直角三角形")
        else:
            print("普通三角形")
    else:
        print("不能形成三角形")
def a5():
    A = 56
    B = 78
    A = A+B
    B = A-B
    A = A-B
    print("A=",A,"B=",B)
def a6():
    user = "root"
    password = "admin"
    flag = 0
    while True:
        print("请输入用户名：")
        u = input()
        print("请输入密码：")
        p = input()
        if u == user and p == password:
            print("登陆成功")
            break
        else:
            print("密码错误")
            flag += 1
        if flag == 3:
            print("密码错误3次，已锁定")
            break
def a7():
    for i in range(1,8):
        for k in range(7 - i):
            print("", end=" ")
        for j in range(i):
            print("* ",end ="")
        print()
def a8():
    i = 1
    j = 0
    n = int(input("输入N"))
    while True:
        while True:
            j += 1
            print(j,"*",i,"=",i*j,end="\t")
            if j == i:
                j = 0
                break
        if i == n:
            break
        i += 1
        print()
def a9():
    l = list(range(1, 10))
    l.reverse()
    for i in l:
        for j in range(1, i+1):
            print(j,"*",i,"=",i*j,end="\t")
        print()
def a10():
    i = 1
    sum = 0
    while True:
        sum += 1
        if sum > 20:
            print(i,"天")
            break
        i += 1
def a11():
    # char = 1
    # Cy % ty = 1
    # Oax_li = 1
    # $123 = 1
    # fLul = 1
    # 3_3 = 1
    # BYTE = 1
    T_T = 1
    print(T_T)
def a12():
    import random
    randint = random.randint(10, 20)
    print(randint)
    i = 3
    coin = 5
    count = 0
    while True:
        num = int(input("请输入您猜的数字"))
        if num == randint:
            print("恭喜你猜对了")
            count += 1
            print("已猜",count,"次")
            randint = random.randint(10, 20)
            print(randint)
        else:
            count += 1
            print("猜错了")
            print("已猜", count, "次")
            i -= 1
        coin -= 1
        if coin <= 0:
            print("金币已用完是否充钱？充钱输入1,不充输入0")
            j = int(input())
            if j == 1:
                coin = int(input("请输入金币数:"))
                randint = random.randint(10, 20)
                print(randint)
            else:
                break
        if i <= 0:
            print("猜错3次，游戏结束")
            break
def a13():
    sum = 0
    for i in range(1,21):
        k = 1
        for j in range(i):
            k = (j+1) * k
        print(k)
        sum = k+sum
    print(sum)
a8()






