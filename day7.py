import numpy as np
import xlrd

data = xlrd.open_workbook(r'D:\自动化测试python\python\python任务\day7\任务\2020年每个月的销售情况.xlsx')

s1 = 0
s2 = 0
for k in range(12):
    table = data.sheet_by_index(k)
    List1 = table.col_values(2, 1)
    List2 = table.col_values(4, 1)
    List3 = np.multiply(np.array(List1), np.array(List2))
    s1 += sum(List3.tolist())
print("总销售额：", s1)
for k in range(12):
    table = data.sheet_by_index(k)
    List1 = table.col_values(4, 1)
    s = sum(List1) / (table.nrows - 1)
    s2 += s
print("平均每日销售数量：", s2 / 12)

for k in range(12):
    table = data.sheet_by_index(k)
    s1 = set(table.col_values(1, 1))
    t1 = list(s1)
    for i in t1:
        num = 0
        flag = 0
        for j in table.col_values(1, 1):
            flag += 1
            if i == j:
                num += table.cell_value(flag, 4)
        print(i,"的",k + 1,'月销量占比：{:.2%}'.format(num/(sum(table.col_values(4, 1)))))

    print()
