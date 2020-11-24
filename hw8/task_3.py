# 3. Создайте собственный класс-исключение, который должен проверять содержимое списка на наличие только чисел.
# Проверить работу исключения на реальном примере. Необходимо запрашивать у пользователя данные и заполнять список.
# Класс-исключение должен контролировать типы данных элементов списка.


class NotNumberError(Exception):
    pass


user_list = []
while True:
    user_input = input('Input number to add the list or type "stop" to stop adding: ')

    if user_input == 'stop':
        break

    try:
        if not user_input.isdigit():
            raise NotNumberError('Not number typed!!! Try again')
        number = float(user_input)
        user_list.append(number)

    except NotNumberError as e:
        print(f'Error! - {e}')


print(user_list)



# a = "5.2"
#
# if isinstance(a, (int, float)):
#     print("number")
# else:
#     print('not a number')
#
