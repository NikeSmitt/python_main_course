# 5. Запросите у пользователя значения выручки и издержек фирмы. Определите, с каким финансовым результатом работает
# фирма (прибыль — выручка больше издержек, или убыток — издержки больше выручки). Выведите соответствующее
# сообщение. Если фирма отработала с прибылью, вычислите рентабельность выручки (соотношение прибыли к выручке).
# Далее запросите численность сотрудников фирмы и определите прибыль фирмы в расчете на одного сотрудника.


def task5(revenue_user_input, costs_user_input, staff_quantity_user_input):
    revenue = int(revenue_user_input)  # выручка
    costs_user_input = int(costs_user_input)
    staff = int(staff_quantity_user_input)  # количество сотрудников
    profitability = 0  # рентабельность выручки
    profit = revenue - costs_user_input  # прибыль
    staff_profit = 0  # прибыль на одного сотрудника

    if profit < 0:
        print('Ваша фирма убыточна')
    elif profit == 0:
        print('Ваша фирма имеет нулевую прибыль')
    else:
        print('Ваша фирма прибыльна')
        profitability = profit / revenue
        print(f'Рентабельность выручки составляет {profitability * 100:.2f}%')
        staff_profit = profit / staff
        print(f'Прибыль фирмы в расчете на одного сотрудника: {staff_profit:.2f}')


if __name__ == "__main__":
    task5(1000, 900, 4)
