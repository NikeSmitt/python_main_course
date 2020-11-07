# 4. Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные. При этом английские
# числительные должны заменяться на русские. Новый блок строк должен записываться в новый текстовый файл.

SRC_FILE_NAME = 'task_4_src_data.txt'
OUTPUT_FILE_NAME = 'task_4_output_data.txt'

digits_vocab = {
    'One': 'Один',
    'Two': 'Два',
    'Three': 'Три',
    'Four': 'Четыре'
}

src_file = open(SRC_FILE_NAME, 'r', encoding='utf-8')
output_file = open(OUTPUT_FILE_NAME, 'w', encoding='utf-8')

for line in src_file.readlines():
    line_list = line.split()
    print(line_list)
    line_list[0] = digits_vocab.get(line_list[0], '***')

    output_file.write(f"{' '.join(line_list)}\n")

output_file.close()
src_file.close()
