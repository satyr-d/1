# class Air:
#     __brand = ""
#     __price = 0
#
#     def set_brand(self, brand):
#         self.__brand = brand
#
#     def set_price(self, price):
#         self.__price = price
#
#     def get_brand(self):
#         return self.__brand
#
#     def get_price(self):
#         return self.__price
#
#     def open(self):
#         print("空调开机了...")
#
#     def close(self, num):
#         print("空调将在", num, "分钟后自动关闭...")
#
#
# air = Air()
# air.set_price(1000)
# air.set_brand("美的")
# print(air.get_brand(), air.get_price())
# air.open()
# air.close(5)
#
#
# class Student:
#     __username = None
#     __age = None
#
#     def setUsername(self, username):
#         self.__username = username
#
#     def getUsername(self):
#         return self.__username
#
#     def setAge(self, age):
#         if age > 120 or age < 0:
#             print("您年龄输入非法！")
#         else:
#             self.__age = age
#
#     def getAge(self):
#         return self.__age
#
#     def showMe(self):
#         print("大家好，我叫", self.__username, "，今年", self.__age, "岁了！")
#
#     def compare(self, student):  # self代表我自己    student代表另一个人
#         if self.__age > student.getAge():
#             print("我比同桌大", (self.__age - student.getAge()), "岁！")
#         elif self.__age < student.getAge():
#             print("我比同桌小", (student.getAge() - self.__age), "岁！")
#         else:
#             print("我俩一样大！")
#
#
# s = Student()
# s.setUsername("旺财")
# s.setAge(55)
#
# s1 = Student()
# s1.setUsername("李四")
# s1.setAge(56)
#
# s.showMe()
# s.compare(s1)  # 旺财要和李四比较
# s1.compare(s)
#
#
# class People:
#     __name = None
#     __gender = ''
#     __age = None
#     __cost = 0   # 剩余话费
#     __brand = ''   # 品牌
#     __battery = 0  # 电池容量
#     __size = 0    # 屏幕大小
#     __standby = 0   # 最大待机时长
#     __integral = 0  # 积分
#
#     def setName(self, name):
#         self.__name = name
#
#     def getName(self):
#         return self.__name
#
#     def setGender(self, gender):
#         self.__gender = gender
#
#     def getGender(self):
#         return self.__gender
#
#     def setAge(self, age):
#         if age <= 0 or age >= 120:
#             print('年龄非法！')
#         else:
#             self.__age = int(age)
#
#     def getAge(self):
#         return self.__age
#
#     def setCost(self, cost):
#         self.__cost = float(cost)
#
#     def getCost(self):
#         return self.__cost
#
#     def setBrand(self, brand):
#         self.__brand = brand
#
#     def getBrand(self):
#         return self.__brand
#
#     def setBattery(self, battery):
#         if battery < 0:
#             print('电池容量不能为负！')
#         else:
#             self.__battery = float(battery)
#
#     def getBattery(self):
#         return self.__battery
#
#     def setSize(self, size):
#         if size <= 0:
#             print('屏幕大小输入非法！')
#         else:
#             self.__size = int(size)
#
#     def getSize(self):
#         return self.__size
#
#     def setStandby(self,standby):
#         self.__standby = int(standby)
#
#     def getStandby(self):
#         return self.__standby
#
#     def setIntegral(self, integral):
#         if integral < 0:
#             print('积分不能为负！')
#         else:
#             self.__integral = int(integral)
#
#     def getIntegral(self):
#         return self.__integral
#
#     def show(self):
#         print('姓名', self.__name, '\n性别', self.__gender, '\n年龄', self.__age,'\n所拥有的手机剩余话费',
#               self.__cost, '元！\n手机品牌', self.__brand,'\n手机电池容量', self.__battery, '%\n屏幕大小',
#               self.__size, '寸\n最大待机时长',self.__standby, '分钟\n所拥有积分：', self.__integral)
#
#
# p = People()
# p.setName(input('输入姓名'))
# p.setGender(input('输入性别'))
# p.setAge(int(input('输入年龄')))
# p.setCost(float(input('输入手机剩余话费')))
# p.setBrand(input('输入手机品牌'))
# p.setBattery(float(input('输入电池容量')))
# p.setSize(int(input('输入手机屏幕大小')))
# p.setStandby(int(input('输入手机最大待机时长')))
# p.setIntegral(int(input('输入拥有积分')))
# p.show()
# cc = p.getCost()
# dd = p.getIntegral()
#
# while True:
#     a = int(input('需要打电话还是发短信：（1或2）'))
#     if a == 1:
#         a_1 = input('输入短信内容：')
#         print('短信内容为：\n', a_1)
#     elif a == 2:
#         a_1 = int(input('输入电话号码：'))
#         a_2 = int(input('输入打多长时间：'))
#         if a_1 == None: print('不能为空！')
#         elif a_1 <= 1: print('电话费不够了！')
#         else:
#             print('电话已拨通！')
#         if a_2 >= 0 and a_2 <= 10:
#             if dd >= a_2 * 15:
#                 dd -= a_2 * 15
#             else:
#                 cc -= a_2 * 1
#         elif a_2 > 10 and a_2 <=20:
#             if dd >= a_2 * 39:
#                 dd -= a_2 * 39
#             else:
#                 cc -= a_2 * 0.8
#         else:
#             if dd >= a_2 * 48:
#                 dd -= a_2 * 48
#             else:
#                 cc -= a_2 * 0.65
#
#         print('剩余话费为：', cc)
#         print('剩余积分为：', dd)
#         break


# class Student:
#     __snum = 0
#     __name = ""
#     __age = 0
#     __sex = ""
#     __high = 0
#     __weight = 0
#     __grade = 0
#     __address = ""
#     __phone = 0
#
#     def set_snum(self, num):
#         self.__snum = num
#     def set_name(self, name):
#         self.__name = name
#     def set_age(self, age):
#         self.__age = age
#     def set_sex(self, sex):
#         self.__sex = sex
#     def set_high(self, high):
#         self.__high = high
#     def set_weight(self, weight):
#         self.__weight = weight
#     def set_grade(self, grade):
#         self.__grade = grade
#     def set_address(self, address):
#         self.__address = address
#     def set_phone(self, phone):
#         self.__phone = phone
#     def get_snum(self):
#         return self.__snum
#     def get_name(self):
#         return self.__name
#     def get_age(self):
#         return self.__age
#     def get_sex(self):
#         return self.__sex
#     def get_high(self):
#         return self.__high
#     def get_weight(self):
#         return self.__weight
#     def get_grade(self):
#         return  self.__grade
#     def get_address(self):
#         return self.__address
#     def get_phone(self):
#         return self.__phone
#     def study(self, time):
#         print("学习了", time, "小时")
#     def play_game(self, name):
#         print("玩", name)
#     def program(self, line):
#         print("敲了", line, "行代码")
#     def sum(self, *args):
#         sum = 0
#         for i in args:
#             sum += i
#         return sum
#
# student = Student()
# student.study(5)
# student.program(10)
# print(student.sum(1, 2))
# student.play_game("dota2")


# class Car:
#     __type = ""
#     __num = 0
#     __color = ""
#     __weight = 0
#     __volume = 0
#
#     def set_num(self, num):
#         self.__num = num
#     def set_type(self, name):
#         self.__type = name
#     def set_color(self, age):
#         self.__color = age
#     def set_weight(self, weight):
#         self.__weight = weight
#     def set_volume(self, grade):
#         self.__volume = grade
#     def get_num(self):
#         return self.__num
#     def get_type(self):
#         return self.__type
#     def get_color(self):
#         return self.__color
#     def get_weight(self):
#         return self.__weight
#     def get_volume(self):
#         return  self.__volume
#     def run(self, r_tpye):
#         print(self.__type, "正在",r_tpye)
# ferrari = Car()
# bmw = Car()
# suzuki = Car()
# wuling = Car()
# tractor = Car()
# bmw.set_type("宝马")
# bmw.run("越野")


# class Laptop:
#     __type = ""
#     __time = 0
#     __memory = 0
#     __color = ""
#     __weight = 0
#     __volume = 0
#
#     def set_time(self, num):
#         self.__time = num
#     def set_type(self, name):
#         self.__type = name
#     def set_color(self, age):
#         self.__color = age
#     def set_weight(self, weight):
#         self.__weight = weight
#     def set_volume(self, grade):
#         self.__volume = grade
#     def set_memory(self, m):
#         self.__memory = m
#     def get_time(self):
#         return self.__time
#     def get_type(self):
#         return self.__type
#     def get_color(self):
#         return self.__color
#     def get_weight(self):
#         return self.__weight
#     def get_volume(self):
#         return  self.__volume
#     def get_memory(self):
#         return self.__memory
#     def play_game(self, name):
#         print("正在玩",name)
#     def work(self):
#         print("正在办公")
# laptop = Laptop()
# laptop.play_game("dota2")
# laptop.work()

class Monkey:
    __type = ""
    __sex = ""
    __color = ""
    __weight = 0

    def set_type(self, name):
        self.__type = name
    def set_color(self, age):
        self.__color = age
    def set_weight(self, weight):
        self.__weight = weight
    def set_sex(self, grade):
        self.__sex = grade
    def get_sex(self):
        return self.__sex
    def get_type(self):
        return self.__type
    def get_color(self):
        return self.__color
    def get_weight(self):
        return self.__weight

    def study(self, name):
        print("正在学习",name)
    def make_fire(self, m):
        print("正在用", m, "造火")

monkey = Monkey()
monkey.study("钓鱼")
monkey.make_fire("木棍")