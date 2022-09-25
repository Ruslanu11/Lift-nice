import logging


class ErrorCapacity(Exception):
    def __init__(self, text):
        self.txt = text


class ErrorFloor(Exception):
    def __init__(self, text):
        self.txt = text


class Lift:
    def __init__(self, floor_count, elevator_capacity):
        self.units = []
        self.units_kg = 0
        self.count_units = 0
        self.weight_units = 0
        self.floor_count = floor_count
        self.elevator_capacity = elevator_capacity
        self.floor_location = 1

    def move(self, floor_number):
        if floor_number <= self.floor_count:
            if self.units_kg <= self.elevator_capacity:
                self.floor_location = floor_number
                print(f'Мы прибыли на {floor_number} этаж\n')
            else:
                logging.warning("A WARNING")
                raise ErrorCapacity('Лифт не выдерживает данный груз')
        else:
            logging.critical("A message of CRITICAL severity")
            raise ErrorFloor('Данного этажа не существует')

    def add_unit(self, unit: list):
        floor = unit[0]
        weigth = unit[1]
        self.units.append(unit)
        self.units_kg += weigth
        self.count_units += 1
        print(f"Зашел человек!\n\nЭтаж на котором  выйдет: {floor} человек\nВес: {weigth}кг\n")

    def deleted_unit(self, i = 0):
        while i < self.count_units:
            if self.floor_location == self.units[i][0]:
                self.units_kg -= self.units[i][1]
                self.count_units -= 1
                self.units.pop(i)
                print('Человек вышел\n')
            i += 1

class Human:

    def call_elevator(self, unit_location):
        elevator.move(unit_location)

elevator = Lift(10, 500)
elevator.move(1)
human = Human()
human.call_elevator(2)
elevator.add_unit([1, 50])
elevator.add_unit([1, 75])
elevator.move(1)
elevator.deleted_unit()
elevator.deleted_unit()





