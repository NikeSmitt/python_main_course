# 1. Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
# Атрибут реализовать как приватный. В рамках метода реализовать переключение светофора в режимы: красный, желтый,
# зеленый. Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды,
# третьего (зеленый) — на ваше усмотрение. Переключение между режимами должно осуществляться только в указанном
# порядке (красный, желтый, зеленый). Проверить работу примера, создав экземпляр и вызвав описанный метод.
#
# Задачу можно усложнить, реализовав проверку порядка режимов, и при его нарушении выводить соответствующее сообщение
# и завершать скрипт.
from time import sleep


class TrafficLight:
    __colors_and_wait_times_sequence = [('red', 7), ('yellow', 2), ('green', 3), ('yellow', 2)]

    def __init__(self):
        self.__color = None

    def running(self):
        idx_to_get_color = -1

        while True:
            idx_to_get_color = (idx_to_get_color + 1) % len(self.__colors_and_wait_times_sequence)
            self.__color, wait_time = self.__colors_and_wait_times_sequence[idx_to_get_color]
            print(self.__color)
            sleep(wait_time)


if __name__ == '__main__':
    traffic_light = TrafficLight()
    traffic_light.running()
