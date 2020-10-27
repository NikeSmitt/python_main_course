# 4. Пользователь вводит целое положительное число. Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции.

def task4(user_input):
    value = int(user_input)
    max_digit = 0

    while value != 0:
        max_digit = max(value % 10, max_digit)  # через if не стал делать, так хорошо выглядит
        value //= 10

    return max_digit


# tests
def tests_task4():
    tests = [('0', 0), ('1', 1), ('12', 2), ('28', 8), ('10000002', 2), ('98765321', 9), ('192345', 9)]
    for i, test in enumerate(tests):
        if task4(test[0]) != test[1]:
            print(f'Test {i} failed: {test[0]} -> {task4(test[0])} instead of {test[1]}')
            return
    print('Tests OK!')


if __name__ == "__main__":
    tests_task4()
    print(task4('12345'))
