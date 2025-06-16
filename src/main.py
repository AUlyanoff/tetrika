# -*- coding: utf-8 -*-
import logging

from app import init
from app.study_time.solution import appearance
from app.study_time.data import lessons
from app.type_checking.funcs import sum_two_int, sum_two_float
from app.wiki_parsing.solution import get_beasts

logger = logging.getLogger(__name__)

logger.info(init.tetrika)

# Задание 1
for func in (sum_two_int, sum_two_float):
    try:
        result = func(1, 1.)
    except TypeError as e:
        logger.error(e)
    except Exception as e:
        logger.error(f"Unexpected error: {e}")
    else:
        logger.debug(f"{func.__name__}, result = {result}")

# Задание 2
get_beasts("Категория:Животные по алфавиту")

# Задание 3
for i, lesson in enumerate(lessons):
    calculated = appearance(lesson['intervals'])
    if calculated != lesson['answer']:
        logger.error(f'Error on test case {i}, got {calculated}, expected {lesson["answer"]}')
