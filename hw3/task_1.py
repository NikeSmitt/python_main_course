# 1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление. Числа запрашивать у
# пользователя, предусмотреть обработку ситуации деления на ноль.

def show_division(user_input_1, user_input_2):
    """Функция показывает результат деления первого агрумента на второй"""
    try:
        print(int(user_input_1) / int(user_input_2))
    except ValueError:
        print("Invalid user input!")
    except ZeroDivisionError:
        print("Zero division error!")


show_division("1", "2")
show_division("1", "2в")
show_division("1", "0")
