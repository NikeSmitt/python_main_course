# 2. Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет количества строк,
# количества слов в каждой строке.


FILE_NAME = 'task_2_src_data.txt'
try:
    with open(FILE_NAME, 'r', encoding='utf-8') as f:
        line_list = f.read().splitlines()
except FileNotFoundError as e:
    print('Ошибка чтения файла:', e)
else:
    print(f'Количество строк: {len(line_list)}')
    for position, line in enumerate(line_list, 1):
        print(f'{position} : {line: <40} - {len(line.split(" "))} слов(а)')
