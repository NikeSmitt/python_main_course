# 3. Пользователь вводит месяц в виде целого числа от 1 до 12. Сообщить к какому времени года относится месяц (зима,
# весна, лето, осень). Напишите решения через list и через dict.

def task_3_dict(user_input):
    periods = {1: 'зима', 2: 'зима', 3: 'весна', 4: 'весна', 5: 'весна', 6: 'лето',
               7: 'лето', 8: 'лето', 9: 'осень', 10: 'осень', 11: 'осень', 12: 'зима'}

    error_message = 'Ошибка ввода. Введите число от 1 до 12'
    try:
        return periods.get(int(user_input), error_message)
    except ValueError:
        print(error_message)


def task_3_list(user_input):
    periods = ['зима', 'зима', 'весна', 'весна', 'весна', 'лето',
               'лето', 'лето', 'осень', 'осень', 'осень', 'зима']
    try:
        return periods[int(user_input) - 1]
    except (ValueError, IndexError):
        print('Ошибка ввода. Введите число от 1 до 12')


if __name__ == "__main__":
    input_1 = '1'
    input_2 = '9'
    input_3 = 'f'

    print(task_3_list(input_1))
    print(task_3_list(input_2))
    print(task_3_list(input_3))

    print(task_3_dict(input_1))
    print(task_3_dict(input_2))
    print(task_3_dict(input_3))
