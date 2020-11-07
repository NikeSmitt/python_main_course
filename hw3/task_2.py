# 2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя: имя, фамилия,
# год рождения, город проживания, email, телефон. Функция должна принимать параметры как именованные аргументы.
# Реализовать вывод данных о пользователе одной строкой.

def show_user_info(name, surname, year_of_birth, town, email, phone_number):
    """Функция показывает информацию о пользователе"""
    print(
        f"имя: {name}, "
        f"фамилия: {surname}, "
        f"год рождения: {year_of_birth}, "
        f"город проживания: {town}, "
        f"email: {email}, "
        f"телефон: {phone_number}")


show_user_info(phone_number="555-55-55",
               email="mail@bk.ru",
               town="Moscow",
               year_of_birth="1987",
               surname="Popov",
               name="Petr")
