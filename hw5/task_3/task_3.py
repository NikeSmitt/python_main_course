# 3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
# Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников. Выполнить подсчет
# средней величины дохода сотрудников.



FILE_NAME = 'task_3_src_data.txt'
with open(FILE_NAME, 'r', encoding='utf-8') as f:
    file_content = f.read().splitlines()

employee_less_20000_name = []
salary_sum = 0
employee_quantity = len(file_content)

for line in file_content:
    line_list = line.split()
    employee, salary = line_list[0], int(line_list[1])
    salary_sum += salary
    if salary < 20000:
        employee_less_20000_name.append(employee)

print(f'Сотрудники с окладом менее 20000: ', end='')
print(*employee_less_20000_name, sep=', ')
print(f'Средняя величина дохода сотрудников: {salary_sum / employee_quantity:.2f}')
