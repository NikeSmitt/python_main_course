FILE_NAME = 'task_1_data.txt'

with open(FILE_NAME, 'w', encoding='utf-8') as f:
    while True:
        current_input = input('Type to save to file: ')
        if current_input:
            f.write(f'{current_input}\n')
        else:
            break