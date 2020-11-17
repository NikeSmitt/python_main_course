# 5. Реализовать класс Stationery (канцелярская принадлежность). Определить в нем атрибут title (название) и метод
# draw (отрисовка). Метод выводит сообщение “Запуск отрисовки.” Создать три дочерних класса Pen (ручка),
# Pencil (карандаш), Handle (маркер). В каждом из классов реализовать переопределение метода draw. Для каждого из
# классов методы должен выводить уникальное сообщение. Создать экземпляры классов и проверить, что выведет описанный
# метод для каждого экземпляра.

class Stationery:

    def __init__(self, title):
        self.title = title

    def draw(self):
        print("Запуск отрисовки.", end=' ')

class Pen(Stationery):

    def draw(self):
        super().draw()
        print(f'Используется ручка {self.title}')


class Pencil(Stationery):

    def draw(self):
        super().draw()
        print(f'Применяем карандаш {self.title}')


class Handle(Stationery):

    def draw(self):
        super().draw()
        print(f'Используется маркер {self.title}')


pen = Pen('Biq')
pen.draw()

pencil = Pencil('Faber Castell')
pencil.draw()

handle = Handle('Touch')
handle.draw()

