class IncorrectVinNumber(Exception):
    def __init__(self, message):
        self.message = message


class IncorrectCarNumbers(Exception):
    def __init__(self, message):
        self.message = message


class Car:
    def __init__(self, model, vin_number,  numbers):
        self.model = model
        self.vin_number = vin_number
        self.numbers =  numbers
        self.__is_valid_vin(vin_number)
        self.__is_valid_numbers(numbers)


    def __is_valid_vin(self, vin_number):
        if isinstance(vin_number, int) != 1:
            raise IncorrectVinNumber('Некорректный тип vin номер')
        elif not vin_number >= 1000000 and vin_number <= 9999999:
            raise IncorrectVinNumber('Неверный диапазон для vin номера')
        else:
            True

    def __is_valid_numbers(self, numbers):
        if isinstance(numbers, str) != 1:
            raise IncorrectCarNumbers('Некорректный тип данных для номеров')
        elif len(numbers) != 6:
            raise IncorrectCarNumbers('Неверная длина номера')
        else:
            True



try:
  first = Car('Model1', 1000000, 'f123dj')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumbers as exc:
  print(exc.message)
else:
  print(f'{first.model} успешно создан')

try:
  second = Car('Model2', 300, 'т001тр')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumbers as exc:
  print(exc.message)
else:
  print(f'{second.model} успешно создан')

try:
  third = Car('Model3', 2020202, 'нет номера')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumbers as exc:
  print(exc.message)
else:
  print(f'{third.model} успешно создан')