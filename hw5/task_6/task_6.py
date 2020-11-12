# 6. Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и наличие
# лекционных, практических и лабораторных занятий по этому предмету и их количество. Важно, чтобы для каждого
# предмета не обязательно были все типы занятий. Сформировать словарь, содержащий название предмета и общее
# количество занятий по нему. Вывести словарь на экран.
# Примеры строк файла:
#
# Информатика: 100(л) 50(пр) 20(лаб).
# Физика: 30(л) — 10(лаб)
# Физкультура: — 30(пр)

# Пример словаря:
# {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}

FILE_NAME = 'task_6_src_data.txt'
all_subjects_dict = {}

try:
    with open(FILE_NAME, 'r', encoding='utf-8') as f:
        file_content_list = f.read().splitlines()
except FileNotFoundError as e:
    print('Ошибка чтения файла:', e)
else:
    # бежим по каждому элементу списка, элемент - это строка файла
    for subject_info in file_content_list:

        # тут формируется лист с 2мя эл-ми str: имя предмета и количество занятий
        subject_info_list = subject_info.split(':')
        subject_name = subject_info_list[0]

        # счетчик для часов данного предмета
        subject_hours_sum = 0

        # делаем список из строки списка занятий и бежим по каждому типу занятий
        for hours_str in subject_info_list[1].split():
            # оставляем только строку с количеством часов
            hours = hours_str.rstrip("(л) пр лаб—")
            # строка может быть пустой из-за прочерка в строке занятий (-)
            if hours:
                try:
                    subject_hours_sum += int(hours)
                except ValueError as e:
                    print(f'Ошибка в данных о количестве занятий: {subject_name} -', e)

        # если имя предмета дублируется
        all_subjects_dict[subject_name] = all_subjects_dict.setdefault(subject_name, 0) + subject_hours_sum

    print(all_subjects_dict)
