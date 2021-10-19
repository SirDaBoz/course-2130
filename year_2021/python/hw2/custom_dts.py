from __future__ import annotations

from typing import List, Any

import json


class CycledList:
    """
    Реализуйте список фиксированой длины, в котором новые элементы перезаписываются

    ```
    cycled_list = CycledList(5)
    cycled_list.append(1)
    cycled_list.append(2)
    cycled_list.append(3)
    cycled_list.append(4)
    cycled_list.append(5)
    cycled_list.append(6)
    ```

    Expected Output:
    ```
    [6, 2, 3, 4, 5]
    ```
    """
    def __init__(self, size: int):
        self._data = []
        self.size = size
        self.count = 0

    def append(self, item):
        if len(self._data) < self.size:
            self._data.append(item)
            self.count += 1
        else:
            self._data[self.count % self.size] = item
            self.count += 1


class Fraction:
    """
    Написать класс чисел с бесконечной точностью. Дроби.
    Определите следующие операции:
    1. a / b
    2. a + b
    3. a * b
    4. a - b

    Вы можете найти больше здесь https://docs.python.org/3/reference/datamodel.html#emulating-numeric-types

    В каждый момент времени дробь должна быть правильной

    """

    def __init__(self, nominator, denominator):
        a = nominator
        b = denominator
        r = a % b
        while r:
            a = b
            b = r
            r = a % b
        self.nominator = nominator // b
        self.denominator = denominator // b

    def __truediv__(self, other: Fraction):
        return Fraction(self.nominator*other.denominator, self.denominator*other.nominator)

    def __add__(self, other: Fraction):
        return Fraction(self.nominator*other.denominator+self.denominator*other.nominator,
                        self.denominator*other.denominator)

    def __mul__(self, other: Fraction):
        return Fraction(self.nominator*other.nominator, self.denominator*other.denominator)

    def __sub__(self, other: Fraction) -> Fraction:
        return Fraction(self.nominator*other.denominator-self.denominator*other.nominator,
                        self.denominator*other.denominator)

    def __repr__(self):
        return f'{self.nominator}/{self.denominator}'

    def __eq__(self, other: Fraction):
        return (self.nominator == other.nominator) and (self.denominator == other.denominator)


class MyCounter:
    """
    Реализовать тип данных `Counter`, аналогично типу из `collections`
    https://docs.python.org/3/library/collections.html#collections.Counter

    Достаточно поддерживать только два метода

    """

    def __init__(self, iterable):
        counter = {}
        for item in iterable:
            counter[item] = counter.get(item, 0) + 1
        self._data = counter

    def append(self, item):
        if item in self._data:
            self._data[item] += 1
        else:
            self._data[item] = 0

    def remove(self, item):
        if item in self._data:
            del self._data[item]


class Figure:
    def __init__(self, name):
        self.name = name

    def perimeter(self):
        return None

    def square(self):
        return None

    def __repr__(self):
        return f'Figure({self.name})'


class Square(Figure):
    """
    Реализуйте класс квадрат и два метода для него
    """
    def __init__(self, a, b):
        self.first = a
        self.sec = b

    def perimeter(self):
        return self.first*4

    def square(self):
        return self.first*self.sec


class Container:
    def __init__(self, data):
        self.data = data

    def __delitem__(self, key):
        del self.data[key]

    def __getitem__(self, item):
        return self.data[item]

    def append(self, item):
        self.data.append(item)


class PersistentList:
    """
    Реализуйте список где передаваемый список записывается в файл
    Любая операция удаления/добавления должна изменять файл

    Формат файла - json
    """
    def __init__(self, iterable: List[Any], path_to_file: str):
        self.iterable = iterable
        self.path_to_file = path_to_file
        with open(self.path_to_file, 'w') as outfile:
            outfile.write(json.dumps(self.iterable))

    def append(self, item) -> None:
        """add item to list"""
        self.iterable.append(item)
        with open(self.path_to_file, 'w') as outfile:
            outfile.write(json.dumps(self.iterable))

    def __getitem__(self, index):
        """ return item by index """
        return self.iterable[index]

    def delete(self, index: int) -> None:
        """ delete item by index

            if index greater then length of list back to start and repeat
                [1, 2, 3] -> delete(4) -> [1, 3]

            if index lower then delete from end of list

        """
        if len(self.iterable) < abs(index) + 1:
            index = index % len(self.iterable)
            self.iterable.pop(index)
        else:
            self.iterable.pop(index)
        with open(self.path_to_file, 'w') as outfile:
            outfile.write(json.dumps(self.iterable))

    def __repr__(self):
        return json.dumps(self.iterable, default=lambda x: str(x))
