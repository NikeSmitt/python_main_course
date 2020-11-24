# 2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль. Проверьте его работу на данных,
# вводимых пользователем. При вводе пользователем нуля в качестве делителя программа должна корректно обработать эту
# ситуацию и не завершиться с ошибкой.

class MyZeroDivisionError(Exception):
    pass


def task_2(user_input):
    a, b = list(map(int, user_input.split()))
    try:
        if b < 0:
            raise MyZeroDivisionError('Trying divide by zero!!')
        else:
            print(a / b)
    except MyZeroDivisionError as e:
        print(f'Error occurred: {e}')


task_2('2 5')
task_2('2 0')
