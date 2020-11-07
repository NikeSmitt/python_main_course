# 6. Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и возвращающую его же,
# но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text. Продолжить работу над заданием. В
# программу должна попадать строка из слов, разделенных пробелом. Каждое слово состоит из латинских букв в нижнем
# регистре. Сделать вывод исходной строки, но каждое слово должно начинаться с заглавной буквы. Необходимо
# использовать написанную ранее функцию int_func().

def int_func(word):
    return chr(ord(word[0]) - 32) + word[1:]


def task_6(user_input):

    # список для временного хранения 'исправленных' свло
    result_str_array = []
    for word in user_input.split():
        result_str_array.append(int_func(word))
    return ' '.join(result_str_array)


s = 'push yourself because no one else is going to do it for you'
print(task_6(s))
