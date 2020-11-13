# 3. Реализовать базовый класс Worker (работник), в котором определить атрибуты: name, surname, position (должность),
# income (доход). Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы: оклад и
# премия, например, {"wage": wage, "bonus": bonus}. Создать класс Position (должность) на базе класса Worker. В
# классе Position реализовать методы получения полного имени сотрудника (get_full_name) и дохода с учетом премии (
# get_total_income). Проверить работу примера на реальных данных (создать экземпляры класса Position,
# передать данные, проверить значения атрибутов, вызвать методы экземпляров).

class Worker:

    def __init__(self, name, surname, position, wage=0, bonus=0):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'wage': wage, 'bonus': bonus}

    def get_income(self):
        return self._income


class Position(Worker):

    def get_full_name(self):
        return f'{self.name}, {self.surname}'

    def get_total_income(self):
        income = super().get_income()
        try:
            wage = int(income.get('wage', 0))
            bonus = int(income.get('bonus', 0))
        except ValueError as e:
            print('Incorrect data in wage or bonus fields!!!', e)

        else:
            return f'{wage + bonus:.1f} rub'


technic = Position('Alex', 'Smith', 'Technic', 20000, 200)
print(technic.get_full_name())
print(technic.get_total_income())
