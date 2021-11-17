f = open(file="D:\\自动化测试python\\python\\python任务\\day15【异常】\\baidu_x_system.log", mode="r")
l = f.readlines()
l1 = []
l2 = []

for i in l:
    if i.split()[0] not in l1:
        l1.append(i.split()[0])
for i in l:
    l2.append(i.split()[0])
for i in l1:
    count = 0
    for j in l2:
        if i == j:
            count += 1
    print(i, "出现次数：", count)
