# -*- coding: utf-8 -*-
from functools import wraps

def strict(func):
    """Проверка соответствия типов данных их аннотации"""
    # Приведение типов не учитывается

    @wraps(func)
    def wrap(*args, **kwargs):
        """Логика декоратора"""
        for arg, annotated_type in zip(args, func.__annotations__.values()):
            if type(arg) != annotated_type:
                raise TypeError(f'{func.__name__} ({func.__doc__}): {arg} ({type(arg)}) is not {annotated_type}')

        return func(*args, **kwargs)

    return wrap
