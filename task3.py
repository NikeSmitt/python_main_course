# 3. Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn.
# Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369 


def task3(user_input):
    value = int(user_input)
    sum_result = 0
    candidate = 0  # элемент ряда (3,33,333)
    for i in range(value):
        # увеличиваем разряд (т.е 3 -> 30)
        candidate *= 10
        # добавляется единицы (т.е. 30 -> 33)
        candidate += value
        sum_result += candidate

    return sum_result


# для себя покрыл тестами
def test_task3():
    # тестируем до 9 включительно

    # формируем строки для тестов потом копируем из консоли
    # for value in range(1,10):
    #     s = f"{value}"
    #     for i in range(2,value+1):
    #         s += ' + '
    #         s += f'{value}' * i
    #     print(s)

    tests_results = [0,
                     1,
                     2 + 22,
                     3 + 33 + 333,
                     4 + 44 + 444 + 4444,
                     5 + 55 + 555 + 5555 + 55555,
                     6 + 66 + 666 + 6666 + 66666 + 666666,
                     7 + 77 + 777 + 7777 + 77777 + 777777 + 7777777,
                     8 + 88 + 888 + 8888 + 88888 + 888888 + 8888888 + 88888888,
                     9 + 99 + 999 + 9999 + 99999 + 999999 + 9999999 + 99999999 + 999999999]

    for i, test in enumerate(tests_results):
        if task3(str(i)) != test:
            print(f'Test {i} failed')
            return
    print('Tests OK!')


if __name__ == '__main__':
    test_task3()
    print(task3('3'))
