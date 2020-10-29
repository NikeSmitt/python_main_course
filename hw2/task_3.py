# 3. Пользователь вводит месяц в виде целого числа от 1 до 12. Сообщить к какому времени года относится месяц (зима,
# весна, лето, осень). Напишите решения через list и через dict.

def task_3_dict(user_input):
    seasons = {0: 'зима', 1: 'весна', 2: 'лето', 3: 'осень'}

    error_message = 'Ошибка ввода. Введите число от 1 до 12'
    try:
        month_num = int(user_input)
        if not 0 < month_num < 13:
            raise IndexError

        return seasons.get(month_num // 3 % 4)
    except (IndexError, ValueError):
        print(error_message)


def task_3_list(user_input):
    periods = ['зима', 'весна', 'лето', 'осень']
    error_message = 'Ошибка ввода. Введите число от 1 до 12'
    try:
        month_num = int(user_input)
        if not 0 < month_num < 13:
            raise IndexError

        return periods[month_num // 3 % 4]
    except (ValueError, IndexError):
        print(error_message)


if __name__ == "__main__":
    input_1 = '1'
    input_2 = '2'
    input_3 = '12'

    print(task_3_list(input_1))
    print(task_3_list(input_2))
    print(task_3_list(input_3))

    print(task_3_dict(input_1))
    print(task_3_dict(input_2))
    print(task_3_dict(input_3))
