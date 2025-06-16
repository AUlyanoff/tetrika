# -*- coding: utf-8 -*-
import logging
from functools import wraps

from app.study_time.solution import logger

logger = logging.getLogger(__name__)


def strict(func):
    """Проверка соответствия типов данных их аннотации"""
    # Приведение типов не учитывается

    @wraps(func)
    def wrap(*args, **kwargs):
        """Логика декоратора"""

        for arg, annotated_type in zip(args, func.__annotations__.values()):
            if type(arg) != annotated_type:
                raise TypeError(f'{func.__name__} ({func.__doc__}): {arg} ({type(arg)}) is not {annotated_type}')

        logger.debug(f"{func.__name__} with {args} started...")
        return func(*args, **kwargs)  # вызов декорированной функции

    return wrap
