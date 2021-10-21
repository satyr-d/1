#优化代码：只有一个input 进行判断 1or2 生成人名or几遍    q or Q退出  输入其他的直接锁死time.sleep(10)睡10秒
import random
import time

list=["法外狂徒","小李子","汤老师","郭达","强森","抖森","小罗伯特","汉弗莱","兰尼斯特","千纸鹤"]
#角标
while True:
    index=input("请输入1或2随机生成\n")
    #生成人名
    if index == 'q' or index == 'Q':
        print("退出系统")
        break
    else:
        try:
            index = int(index)
        except :
            print("还有3秒退出")
            time.sleep(1)
            print("还有2秒退出")
            time.sleep(1)
            print("还有1秒退出")
            time.sleep(1)
            print("退出系统")
            break
        if index == 1 or index == 2:
            dint=random.randint(0,len(list)-1)
            num=random.randint(0,10)
            print(list[dint],"处罚了",num,"遍")
        else:
            print("还有3秒退出")
            time.sleep(1)
            print("还有2秒退出")
            time.sleep(1)
            print("还有1秒退出")
            time.sleep(1)
            print("退出系统")
            break