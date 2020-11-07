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
with open(FILE_NAME, 'r', encoding='utf-8') as f:
    file_content_list = [line for line in f.read().splitlines()]
    print(file_content_list)

for subject_info in file_content_list:
    subject_info_list = subject_info.split()
    subject_name = subject_info_list[0].replace(":", "")
    subject_hours = 0
    print(subject_name)
    for hours_str in subject_info_list[1:]:
        hours = hours_str.rstrip("(л) пр лаб—")
        if hours:
            subject_hours += int(hours)

    all_subjects_dict[subject_name] = all_subjects_dict.setdefault(subject_name, 0) + subject_hours

print(all_subjects_dict)