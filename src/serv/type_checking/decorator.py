# -*- coding: utf-8 -*-
from functools import wraps
# import logging

# logger = logging.getLogger(__name__)

def strict(func):
    """Проверка фактических типов данных аннотированным"""
    @wraps(func)
    def wrap(*args, **kwargs):
        print(args)
        for k, v in func.__annotations__.items():
            print(f'{k} = {v.__name__}')

        for v, t in zip(args, func.__annotations__.values()):
            print(f'{v} = {t.__name__}')
            if type(v) != t: raise TypeError

        return func(*args, **kwargs)

    return wrap
