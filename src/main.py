# -*- coding: utf-8 -*-
from serv.type_checking.decorator import strict

@strict
def sum_two_int(a: int, b: int) -> int:
    """Суммирование целых аргументов"""
    return a + b

@strict
def sum_two_float(a: float, b: float) -> float:
    """Суммирование с плавающей точкой"""
    return a + b

if __name__ == '__main__':
    print(sum_two_int(1, 1))
    print(sum_two_float(3.14, 1))
