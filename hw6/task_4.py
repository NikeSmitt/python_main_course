# 4. Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (
# булево). А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась,
# повернула (куда). Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый
# класс метод show_speed, который должен показывать текущую скорость автомобиля. Для классов TownCar и WorkCar
# переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться
# сообщение о превышении скорости.
#
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
# Выполните вызов методов и также покажите результат.

class Car:

    def __init__(self, speed=0, color='white', name='car', is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go():
        print('Car has started to move.')

    def stop(self):
        print('Car has stopped.')

    def car(self, direction):
        print(f'Car has turned to the {direction}.')

    def show_speed(self):
        print(f'{self.color.title()} {self.name} current speed: {self.speed} km')

    def get_speed_warning_message(self):
        return f"{self.color.title()} {self.name} speed limit exceeded!!!"


class TownCar(Car):

    def show_speed(self):
        speed_limit = 60
        super().show_speed()
        if self.speed > speed_limit:
            print(self.get_speed_warning_message())


class SportCar(Car):
    pass


class WorkCar(Car):

    def show_speed(self):
        speed_limit = 40
        super().show_speed()
        if self.speed > speed_limit:
            print(self.get_speed_warning_message())     # дублирование кода, хотел все вывести в родительский класс

class PoliceCar(Car):

    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, True)


work_car = WorkCar(41, 'yellow', 'GAZ-53')
work_car.show_speed()

town_car = TownCar(60, 'red', 'Volga-3102')
town_car.show_speed()
