#任务：开始金币有5个金币，每猜一次减一个为0就退出（or充钱）猜错3次也退出

import random
#              20，10
randint=random.randint(10, 20)#随机生成数字的范围：int   []
print(randint)
i = 3
coin = 5
while True:
    num = int(input("请输入您猜的数字"))
    if num == randint:
        print("恭喜你猜对了")
        randint = random.randint(10, 20)
        print(randint)
    else:
        print("猜错了")
        i -= 1
    coin -= 1
    if coin <= 0:
        print("金币已用完是否充钱？充钱输入1,不充输入0")
        j = int(input())
        if j == 1:
            coin = 5
            randint = random.randint(10, 20)
            print(randint)
        else:
            break
    if i<= 0:
        print("猜错3次，游戏结束")
        break
