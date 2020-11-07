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
    firm_info_lists = [line.split() for line in f.readlines()]

profits = 0
firms_with_profit = 0
for firm_info in firm_info_lists:
    name, proceeds, costs = firm_info[0], int(firm_info[2]), int(firm_info[3])
    current_firm_profit = proceeds - costs
    firms_dict[name] = current_firm_profit
    if current_firm_profit > 0:
        profits += current_firm_profit
        firms_with_profit += 1

average_profit = profits / firms_with_profit
# print([firms_dict, {'average_profit': average_profit}])

with open(OUTPUT_FILE_NAME, 'w', encoding='utf-8') as f:
    json.dump([firms_dict, {'average_profit': average_profit}], f)
