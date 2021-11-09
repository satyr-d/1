from threading import Thread
import time

num = 0
money = 0


class Cooker(Thread):
    name = ""
    c_num = 0
    c_money = 0

    def run(self) -> None:
        global num,end,money
        while (end - start) < 180:
            end = time.perf_counter()

            if num >= 500:
                print("篮子满了")
                time.sleep(3)
            else:
                num += 1
                self.c_num += 1
                self.c_money = self.c_num * 2.5
                money -= self.c_money

                print(self.name,"赚了",self.c_money,"做了",self.c_num,"个蛋挞")



class Customer(Thread):
    c_money = 5000
    c_num = 0
    name = ""
    def run(self):
        global num, money, end
        while (end - start) < 180:
            end = time.perf_counter()

            if num <= 0:
                print("篮子空了")
                time.sleep(4)
            elif self.c_money > 0:
                num -= 1
                self.c_num += 1
                self.c_money -= self.c_num * 3
                money += self.c_num * 3

                print(self.name,"买了",self.c_num,"个蛋挞，剩",self.c_money,"块钱")



C1 = Cooker()
C2 = Cooker()
C3 = Cooker()
p1 = Customer()
p2 = Customer()
p3 = Customer()
p4 = Customer()
p5 = Customer()
p6 = Customer()
C1.name = "厨师1"
C2.name = "厨师2"
C3.name = "厨师3"
p1.name = "顾客1"
p2.name = "顾客2"
p3.name = "顾客3"
p4.name = "顾客4"
p5.name = "顾客5"
p6.name = "顾客6"
start = time.perf_counter()
end = 0
C1.start()

C2.start()

C3.start()

p1.start()

p2.start()

p3.start()

p4.start()

p5.start()

p6.start()


