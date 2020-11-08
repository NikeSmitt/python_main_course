# 5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами. Программа
# должна подсчитывать сумму чисел в файле и выводить ее на экран.

FILE_NAME = 'task_5_data.txt'
with open(FILE_NAME, 'w+', encoding='utf-8') as f:
    f.write(' '.join([str(n) for n in range(11)]))

    # чтобы заново не открывать файл
    f.seek(0)
    values_sum = 0
    for value in [int(n) for n in f.read().split()]:
        values_sum += value
    print(values_sum)

