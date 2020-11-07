# 1. Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника. В расчете
# необходимо использовать формулу: (выработка в часах * ставка в час) + премия. Для выполнения расчета для конкретных
# значений необходимо запускать скрипт с параметрами.

import sys


def calc_salary(hours, hourly_rate, bonus):
    return hours * hourly_rate + bonus


args = sys.argv[1:]
if len(args) < 2:
    print('Введите выработку в часах, ставку в час и премию (если есть)')

else:
    bonus = int(args[2]) if len(args) > 2 else 0
    print(calc_salary(int(args[0]), int(args[1]), bonus))
