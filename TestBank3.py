import 工商银行完整版 as Bank
import unittest
from ddt import ddt
from ddt import data
from ddt import unpack
import xlrd, xlwt
from xlutils.copy import copy
import random

da = xlrd.open_workbook('D:\\自动化测试python\\python\\python任务\\day14【参数化测试】\\H.xls')
table = da.sheets()[2]
table2 = da.sheets()[0]
rb = xlrd.open_workbook('D:\\自动化测试python\\python\\python任务\\day14【参数化测试】\\H.xls')
wb = copy(rb)
ws = wb.get_sheet(2)

li = []
l = []
for i in range(1, table.nrows):
    li = table.row_values(i, start_colx=0, end_colx=5)
    l.append(li)

i = 0

for j in range(5):
    Bank.bank["b"+str(j)] = {"account": "b"+str(j), "money":  random.randint(1, 500), "password": "b"+str(j)}
for j in range(5):
    Bank.bank["c"+str(j)] = {"account": "c"+str(j), "money":  random.randint(1, 500), "password": "c"+str(j)}
@ddt
class TestBank(unittest.TestCase):

    @data(*l)
    @unpack
    def test_transformMoney(self, a, b, c, d, h):

        result = Bank.bank_transformMoney(a, b, c, d)
        global i
        i += 1
        if result != h:  # 将测试结果回写到excel表格中。
            ws.write(i, 5, "不通过")
            wb.save('D:\\自动化测试python\\python\\python任务\\day14【参数化测试】\\H.xls')
        else:
            ws.write(i, 5, '通过')
            wb.save('D:\\自动化测试python\\python\\python任务\\day14【参数化测试】\\H.xls')
        self.assertEqual(result, h)


if __name__ == '__main__':
    unittest.main()