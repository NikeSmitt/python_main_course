# 7. Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме: название,
# форма собственности, выручка, издержки.
#
# Пример строки файла: firm_1 ООО 10000 5000.
#
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль. Если фирма
# получила убытки, в расчет средней прибыли ее не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней
# прибылью. Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
#
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
#
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
# Пример json-объекта:
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
# Подсказка: использовать менеджеры контекста.
import json


FILE_NAME = 'task_7_src_data.txt'
OUTPUT_FILE_NAME = 'task_7_output.json'

firms_dict = {}

with open(FILE_NAME, 'r', encoding='utf-8') as f:
    # [['Yandex', 'ООО', '15000', '5000',]]
    firm_info_lists = [line.split() for line in f.readlines()]

# прибыль
profits = 0
# счетчик фирм с прибылью
firms_with_profit = 0

# line_num нужна для отслеживания читаемой строки для вывода исключения
for line_num, firm_info in enumerate(firm_info_lists, 1):
    try:
        # имя фирмы, выручка, издержки
        name, proceeds, costs = firm_info[0], int(firm_info[2]), int(firm_info[3])
    except ValueError as e:
        print(f'Неверный формат в строке {line_num}')
    else:
        current_firm_profit = proceeds - costs
        firms_dict[name] = current_firm_profit
        if current_firm_profit > 0:
            profits += current_firm_profit
            firms_with_profit += 1

# среднее значение прибыли для фирм с прибылью
average_profit = profits / firms_with_profit
with open(OUTPUT_FILE_NAME, 'w', encoding='utf-8') as f:
    json.dump([firms_dict, {'average_profit': average_profit}], f)
