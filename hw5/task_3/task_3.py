# 2. Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет количества строк,
# количества слов в каждой строке.


FILE_NAME = 'task_3_src_data.txt'
with open(FILE_NAME, 'r', encoding='utf-8') as f:
    file_content = f.read().splitlines()

employee_less_20000_name = []
salary_sum = 0
employee_quantity = len(file_content)

for item in file_content:
    employee_salary_list = item.split()
    employee, salary = employee_salary_list[0], int(employee_salary_list[1])
    salary_sum += salary
    if salary < 20000:
        employee_less_20000_name.append(employee)

print(f'Сотрудники с окладом менее 20000: ', end='')
print(*employee_less_20000_name, sep=', ')
print(f'Средняя величина дохода сотрудников: {salary_sum / employee_quantity: .2f}')
