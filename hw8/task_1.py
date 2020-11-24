# 1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата
# «день-месяц-год». В рамках класса реализовать два метода. Первый, с декоратором @classmethod, должен извлекать
# число, месяц, год и преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod, должен проводить
# валидацию числа, месяца и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных
# данных.

class MyDate:

    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

    def __str__(self):
        return f'{self.day:02}-{self.month:02}-{self.year:4d}'

    @classmethod
    def create_date(cls, date_str):
        try:
            date_list = list(map(int, date_str.split('-')))
            if MyDate.is_date_valid(*date_list):
                return cls(*date_list)
        except ValueError as e:
            print(f'Date format error: {e}')

    @staticmethod
    def is_date_valid(day, month, year):

        """
        if (year is not divisible by 4) then (it is a common year)
else if (year is not divisible by 100) then (it is a leap year)
else if (year is not divisible by 400) then (it is a common year)
else (it is a leap year)
"""

        is_leap_year = year % 400 == 0 or (year % 100 != 0 and year % 4 == 0)
        if month == 2:
            month_days = 29 if is_leap_year else 28
        else:
            month_days = 31 if (month % 2 == 1 and month < 8) or (month % 2 == 0 and month >= 8) else 30

        try:
            if day > month_days:
                raise ValueError('Invalid day quantity')
            if month > 12:
                raise ValueError('Invalid month quantity')

        except ValueError as e:
            print(f"Date format error: {e}")

        else:
            print('Date valid')
            return True


date1 = MyDate.create_date('1-02-2011')
print(date1)

