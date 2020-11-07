# 4. Программа принимает действительное положительное число x и целое отрицательное число y. Необходимо выполнить
# возведение числа x в степень y. Задание необходимо реализовать в виде функции my_func(x, y). При решении задания
# необходимо обойтись без встроенной функции возведения числа в степень. Подсказка: попробуйте решить задачу двумя
# способами. Первый — возведение в степень с помощью оператора **. Второй — более сложная реализация без оператора
# **, предусматривающая использование цикла.


def task_4(x, y):
    return x ** y


def task_4_mod(x, y):
    divisor = 1
    for _ in range(abs(y)):
        divisor *= x
    return 1 / divisor


print(task_4(5, -1))
print(task_4_mod(5, -1))
