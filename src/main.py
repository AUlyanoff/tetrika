# -*- coding: utf-8 -*-
import logging

import init
from study_time.counting import appearance
from study_time.data import lessons
from type_checking.strict import strict
from wiki_parsing.animal_counting import get_beasts

logger = logging.getLogger(__name__)

@strict
def sum_two_int(a: int, b: int) -> int:
    """Суммирование целых аргументов"""
    return a + b

@strict
def sum_two_float(a: float, b: float) -> float:
    """Суммирование с плавающей точкой"""
    return a + b

if __name__ == '__main__':

    get_beasts("Категория:Животные по алфавиту")

    # logger.info(f"result = {sum_two_int(1, 1)}")
    # logger.info(f"result = {sum_two_float(3.14, 1.)}")
    #
    # for i, lesson in enumerate(lessons):
    #     calculated = appearance(lesson['intervals'])
    #     assert calculated == lesson['answer'], f'Error on test case {i}, got {calculated}, expected {lesson["answer"]}'
