#第一题
def f1():
    names = [
    ["曹操","56","男","106","IBM", 500 ,"50"],
    ["大乔","19","女","230","微软", 501 ,"60"],
    ["小乔", "19", "女", "210", "Oracle", 600, "60"],
    ["许褚", "45", "男", "230", "Tencent", 700 , "10"]
    ]
    print(names)
    aSalary = 0
    aAge = 0
    man = 0
    woman = 0
    for i in range(len(names)):
        aSalary += int(names[i][5])
    for i in range(len(names)):
        aAge += int(names[i][1])
    aSalary /= len(names)
    aAge /= len(names)
    print("平均薪资：",aSalary," 平均年龄：",aAge)
    names.append(["刘备","45","男","220","alibaba","500","30"])
    print(names)
    for i in range(len(names)):
        if names[i][2] == "男":
            man += 1
        elif names[i][2] == "女":
            woman += 1
    print("男：",man,"人 ","女：",woman,"人")

    for i in range(10, 100, 10):
        sum = 0
        for j in range(len(names)):
            if int(names[j][6]) == i:
                sum += 1
        if sum > 0:
            print(i,"部门人数：",sum)
#第二题
def f2():
    list = [
    ["罗恩","23","35","44"],
    ["哈利","60","70","68","88","90"],
    ["赫敏", "97", "99", "89", "91", "95", "90"],
    ["马尔福", "100", "85", "90"]
    ]
    for i in range(len(list)):
        sum = 0
        for j in range(len(list[i]) - 1):
            sum += int(list[i][j + 1])
        print(list[i][0], "的总成绩：", sum)

#第三题执行结果：12345

#第四题
def f4():
    a = [5,2,4,7,9,1,3,5,4,0,6,1,3]
    tem = 0

    for i in range(len(a)-1):
        n = len(a) - 1
        for j in range(n):
            if a[j] > a[j + 1]:
                tem = a[j]
                a[j] = a[j + 1]
                a[j + 1] = tem
        n -= 1
    print(a)
f4()

