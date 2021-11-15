
import 工商银行完整版 as Bank
import unittest
from ddt import ddt
from ddt import data
from ddt import unpack
import xlrd, xlwt
from xlutils.copy import copy


da = xlrd.open_workbook('D:\\自动化测试python\\python\\python任务\\day14【参数化测试】\\H.xls')
table = da.sheets()[1]
table2 = da.sheets()[0]
rb = xlrd.open_workbook('D:\\自动化测试python\\python\\python任务\\day14【参数化测试】\\H.xls')
wb = copy(rb)
ws = wb.get_sheet(1)

li = []
l = []
for i in range(1, table.nrows):
    li = table.row_values(i, start_colx=0, end_colx=3)
    l.append(li)
i = 0
for j in range(4):
    Bank.bank["a"+str(j)] = {"account": "a"+str(j), "money":  0}
@ddt
class TestBank(unittest.TestCase):

    @data(*l)
    @unpack
    def test_saveMoney(self, a, b, h):

        result = Bank.bank_saveMoney(a, b)
        global i
        i += 1
        if int(result) != int(h):  # 将测试结果回写到excel表格中。
            ws.write(i, 3, "不通过")
            wb.save('D:\\自动化测试python\\python\\python任务\\day14【参数化测试】\\H.xls')
        else:
            ws.write(i, 3, '通过')
            wb.save('D:\\自动化测试python\\python\\python任务\\day14【参数化测试】\\H.xls')
        self.assertEqual(result, h)


if __name__ == '__main__':
    unittest.main()
