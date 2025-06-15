from app.type_checking.strict import strict


@strict
def sum_two_int(a: int, b: int) -> int:
    """Суммирование целых аргументов"""
    return a + b


@strict
def sum_two_float(a: float, b: float) -> float:
    """Суммирование с плавающей точкой"""
    return a + b
