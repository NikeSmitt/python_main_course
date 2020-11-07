# 3. Реализовать функцию my_func(), которая принимает три позиционных аргумента, и возвращает сумму наибольших двух
# аргументов.

def my_func(a, b, c):
    values_sum = a
    min_value = a

    for value in b, c:
        values_sum += value
        min_value = min(value, min_value)

    return values_sum - min_value


print(my_func(1, 2, 3))
