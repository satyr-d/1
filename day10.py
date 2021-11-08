class Cup:
    __high = 0
    __volume = 0
    __color = ""
    __material = ""

    def hold(self):
        print("高度为", self.__high, "容积为", self.__volume, "颜色为", self.__color, "材质为", self.__material, "的水杯正在存水")

    def set_high(self, high):
        self.__high = high

    def set_volume(self, volume):
        self.__volume = volume

    def set_color(self, color):
        self.__color = color

    def set_material(self, material):
        self.__material = material

    def get_high(self):
        return self.__high

    def get_volume(self):
        return self.__volume

    def get_color(self):
        return self.__color

    def get_material(self):
        return self.__material


cup = Cup()
cup.set_high(10)
cup.set_volume(500)
cup.set_color("黑色")
cup.set_material("不锈钢")
cup.hold()


class Laptop:
    __screen = 0
    __price = 0
    __cpu = ""
    __memory = 0
    __time = 0

    def set_screen(self, screen):
        self.__screen = screen

    def set_price(self, price):
        self.__price = price

    def set_cpu(self, cpu):
        self.__cpu = cpu

    def set_memory(self, memory):
        self.__memory = memory

    def set_time(self, time):
        self.__time = time

    def get_screen(self):
        return self.__screen

    def get_price(self):
        return self.__price

    def get_cpu(self):
        return self.__cpu

    def get_memory(self):
        return self.__memory

    def get_time(self):
        return self.__time

    def play_game(self):
        print("正在用", self.__screen, "寸的电脑玩游戏")

    def typing(self):
        print("正在用", self.__screen, "寸的电脑打字")

    def watch_video(self):
        print("正在用", self.__screen, "寸的电脑看视频")


laptop = Laptop()
laptop.set_cpu("intel")
laptop.set_screen(15)
laptop.set_price(5000)
laptop.set_memory(16)
laptop.set_time(10)
laptop.play_game()
laptop.watch_video()
laptop.typing()
