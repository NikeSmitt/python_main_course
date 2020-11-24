# 4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А также класс «Оргтехника»,
# который будет базовым для классов-наследников. Эти классы — конкретные типы оргтехники (принтер, сканер,
# ксерокс). В базовом классе определить параметры, общие для приведенных типов. В классах-наследниках реализовать
# параметры, уникальные для каждого типа оргтехники.
# 5. Продолжить работу над первым заданием. Разработать методы,
# отвечающие за приём оргтехники на склад и передачу в определенное подразделение компании. Для хранения данных о
# наименовании и количестве единиц оргтехники, а также других данных, можно использовать любую подходящую структуру,
# например словарь.
# 6. Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем
# данных. Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.

class Store:
    """
    Класс, описывающий склад
    """
    def __init__(self):
        # {
        # 'printer' : {'ABC123': 2}
        # }
        self._storage = {}

    def add_item_to_storage(self, item, quantity=1):
        try:
            Store.check_input_quantity(quantity)
        except ValueError as e:
            print(f'User input error: {e}')
        else:
            model_quantity_dict = self._storage.get(item.equip_type, {})
            saved_quantity = model_quantity_dict.setdefault(item.model_number, 0)
            model_quantity_dict[item.model_number] = saved_quantity + quantity
            self._storage[item.equip_type] = model_quantity_dict

    def __str__(self):
        return str(self._storage)

    def send_item_to_department(self, type_of_item, model, quantity=1):
        try:
            if type_of_item not in self._storage:
                raise ValueError(f'There is not your type <{type_of_item}> of equipment')

            if model not in self._storage[type_of_item]:
                raise ValueError(f'There is not your model <{model}> of equipment')

            stored_quantity = self._storage[type_of_item][model] - quantity
            if stored_quantity < 0:
                raise ValueError('There are not enough items of your equipment')
            elif stored_quantity == 0:
                del self._storage[type_of_item][model]
            else:
                self._storage[type_of_item][model] = stored_quantity
        except ValueError as e:
            print(f'Warning from storage!!! {e}')

    @staticmethod
    def check_input_quantity(user_input):
        if not isinstance(user_input, int):
            raise ValueError('Quantity format error')


class OfficeEquipment:
    equip_type = None
    """
    Базовай класс для оргтехники
    """
    def __init__(self, brand, model_number):
        self.brand = brand
        self.model_number = model_number

    def __str__(self):
        return f'Manufacture: {self.brand}\nModel: {self.model_number}'


class Printer(OfficeEquipment):
    equip_type = 'printer'

    def __init__(self, brand, model_number, print_technology=None):
        super().__init__(brand, model_number)
        self.print_technology = print_technology


class Scanner(OfficeEquipment):
    equip_type = 'scanner'

    def __init__(self, brand, model_number, size=None):
        super().__init__(brand, model_number)
        self.resolution = size


class Shredder(OfficeEquipment):
    equip_type = 'shredder'

    def __init__(self, brand, model_number, bin_capacity=None):
        super().__init__(brand, model_number)
        self.bin_capacity = bin_capacity


printer = Printer('Brother', 'M2020', 'laser')
printer2 = Printer('HP', 'N33DS', 'laser')
store = Store()
store.add_item_to_storage(printer, 2)
store.add_item_to_storage(printer2)
store.add_item_to_storage(Scanner('Xerox', 'Z5011', 'A4'), 2)
store.add_item_to_storage(Scanner('Xerox', 'AS33S', 'A4'), '2')
store.add_item_to_storage(Shredder('Kensington', 'K52075AM', 10), 5)

print(store)
store.send_item_to_department('printer', 'N33DS', 1)
print(store)
