# Для списка реализовать обмен значений соседних элементов, т.е. Значениями обмениваются элементы с индексами 0 и 1,
# 2 и 3 и т.д. При нечетном количестве элементов последний сохранить на своем месте. Для заполнения списка элементов
# необходимо использовать функцию input().

def task2(user_input):
    user_list = user_input.split()
    for i in range(0, len(user_list) - 1, 2):
        user_list[i], user_list[i+1] = user_list[i+1], user_list[i]
    return user_list


if __name__ == "__main__":
    input_1 = '1 2 3 4 5 6 7'
    input_2 = '1 2 3 4 5 6'
    input_3 = '1'
    input_4 = 'False True'
    input_5 = ''
    print(task2(input_1))
    print(task2(input_2))
    print(task2(input_3))
    print(task2(input_4))
    print(task2(input_5))
