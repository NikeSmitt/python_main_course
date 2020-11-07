import os


FILE_NAME = 'task_2_src_data.txt'
with open(FILE_NAME, 'r', encoding='utf-8') as f:
    line_list = f.read().split('\n')


# print(line_list)
print(f'Количество строк: {len(line_list)}')
for pos, line in enumerate(line_list, 1):
    print(f'{pos} : {line: <40} - {len(line.split(" "))} слов(а)')