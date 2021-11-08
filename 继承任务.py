class OldPhone:
    __brand = ""

    def set_brand(self, brand):
        self.__brand = brand

    def get_brand(self):
        return self.__brand

    def call(self, name):
        print("正在给", name, "打电话...")


class NewPhone(OldPhone):
    def call(self, name):
        print("语音拨号中...")
        super().call(name)

    def introduce(self):
        print("品牌为：", self.get_brand(), "的手机很好用...")


phone = NewPhone()
phone.set_brand("苹果")
phone.introduce()
phone.call("张三")


class Cooker:
    __name = ""
    __age = 0
    def set_name(self, name):
        self.__name = name
    def get_name(self):
        return self.__name
    def set_age(self, age):
        self.__age = age
    def get_age(self):
        return self.__age
    def cook_rise(self):
        pass

class Cooker1(Cooker):
    def stir_fry(self):
        pass


class Cooker2(Cooker1):
    def cook_rise(self):
        print("蒸饭")
    def stir_fry(self):
        print("炒菜")

cooker = Cooker2()
cooker.set_age(20)
cooker.set_name("张三")
print(cooker.get_name(), cooker.get_age())
cooker.cook_rise()
cooker.stir_fry()

class Person:
    __name = ""
    __sex = 0
    __age = 0
    def set_name(self, brand):
        self.__name = brand

    def get_name(self):
        return self.__name
    def set_age(self, age):
        self.__age = age
    def get_age(self):
        return self.__age
    def set_sex(self, sex):
        self.__sex = sex
    def get_sex(self):
        return self.__sex

class Worker(Person):
    def work(self):
        print("正在干活")
class student(Person):
    def study(self):
        print("正在学习")
    def sing(self):
        print("正在唱歌")

worker = Worker()
student = student()
worker.work()
student.study()
student.sing()