# 4.Реализуйте базовый класс Car.
# У данного класса должны быть следующие атрибуты: # speed, color, name, is_police (булево).
# А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
# Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
# Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
# Для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов.
# Выполните доступ к атрибутам, выведите результат. Выполните вызов методов и также покажите результат.

class Car:
    is_police: bool

    def __init__(self, name, speed, color, is_police):
        self.name = name
        self.speed = speed
        self.color = color
        self.is_police = is_police

    def go(self):
        return f'\nАвтомобиль {self.name} цвет {self.color} поехал.'

    def stop(self):
        return f'\nАвтомобиль {self.name} остановился.'

    def turn(self, direction):
        return f'\nАвтомобиль {self.name} повернул {direction}'

    def show_speed(self):
        return f'\nСкорость составила {self.speed} км/ч'

    def show_is_police(self):
        if self.is_police:
            return f'\nЭто полицейская машина'
        else:
            return ''



class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            return f'\nВаша скорость ({self.speed} км/ч) превышена!'
        else:
            return f'\nВаша скорость ({self.speed} км/ч) в норме'


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            return f'\nВаша скорость ({self.speed} км/ч) превышена!'
        else:
            return f'\nВаша скорость ({self.speed} км/ч) в норме'


class PoliceCar(Car):
    pass


town = TownCar('Авто_1', 70, 'черный', False)
print('\n' + town.go(), town.show_speed(), town.turn('направо'), town.turn('налево'), town.stop(), town.show_is_police())

sport = SportCar('Авто_2', 170, 'белый', False)
print('\n' + sport.go(), sport.show_speed(), sport.turn('направо'), sport.stop(), sport.show_is_police())

work = WorkCar('Авто_3', 30, 'красный', False)
print('\n' + work.go(), work.show_speed(), work.turn('налево'), work.stop(), work.show_is_police())

police = PoliceCar('Авто_4', 100, 'голубой', True)
print('\n' + police.go(), police.show_speed(), police.turn('направо'), police.stop(), police.show_is_police())



