# 4. Пользователь вводит строку из нескольких слов, разделённых пробелами. Вывести каждое слово с новой строки.
# Строки необходимо пронумеровать. Если в слово длинное, выводить только первые 10 букв в слове.

def task_4(user_input):
    user_input_list = user_input.split()
    for i, item in enumerate(user_input_list):
        print(f'{i + 1}: {item[:10]}')


if __name__ == "__main__":
    task_4('Lorem ipsum dolor sit amet consectetur adipiscing elit')
