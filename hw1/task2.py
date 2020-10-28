# 2. Пользователь вводит время в секундах. Переведите время в часы, минуты и
# секунды и выведите в формате чч:мм:сс. Используйте форматирование строк


def task2(user_input):
    time_in_sec = int(user_input)
    h = time_in_sec // 3600
    m = time_in_sec % 3600 // 60
    s = time_in_sec % 60
    return f"{h:02d}:{m:02d}:{s:02d}"


if __name__ == "__main__":
    print(task2('410000'))
    print(task2('3700'))
    print(task2('61'))
    print(task2('1'))
    print(task2('0'))
