# 2. Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина). Значения данных
# атрибутов должны передаваться при создании экземпляра класса. Атрибуты сделать защищенными. Определить метод
# расчета массы асфальта, необходимого для покрытия всего дорожного полотна. Использовать формулу: длина * ширина *
# масса асфальта для покрытия одного кв метра дороги асфальтом, толщиной в 1 см * число см толщины полотна.
# Проверить работу метода.
#
# Например: 20м * 5000м * 25кг * 5см = 12500 т


class Road:

    def __init__(self, length, width):
        self.length = length
        self.width = width

    def calc_asphalt_mass(self, meter_area_road_mass, road_width_sm):
        return self.length * self.width * meter_area_road_mass * road_width_sm


village_road = Road(2000, 5)
print(f'Road mass: {village_road.calc_asphalt_mass(25, 5) / 1000:.1f} tons')
