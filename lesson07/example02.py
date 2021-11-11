class Одежда:
    def __init__(self, размер, рост):
        self.размер = размер
        self.рост = рост

    def расход_пальто(self):
        return self.размер / 6.5 + 0.5

    def расход_костюм(self):
        return self.рост * 2 + 0.3

    @property
    def общий_расход(self):
        return f'Общий расход ткани \n{((self.расход_пальто()) + (self.расход_костюм())):.2f}'


class Пальто(Одежда):
    def __init__(self, размер, рост):
        super().__init__(размер, рост)
        self.square_c = self.расход_пальто()

    def __str__(self):
        return f'Расход на пальто {self.square_c:.2f}'


class Костюм(Одежда):
    def __init__(self, размер, рост):
        super().__init__(размер, рост)
        self.square_j = self.расход_костюм()

    def __str__(self):
        return f'Расход на костюм {self.square_j:.2f}'

пальто = Пальто(5, 9)
костюм = Костюм(2, 3)
Общий_расход = пальто.расход_пальто() + костюм.расход_костюм()
print(пальто)
print(костюм)
print(Общий_расход)




