# -*- coding: utf-8 -*-
import logging
from itertools import count

import wikipediaapi

logger = logging.getLogger(__name__)


def get_beasts(article: str):

    wiki = wikipediaapi.Wikipedia(user_agent='Tetrika (ceo@tetrika.com)', language="ru",
                                  extract_format=wikipediaapi.ExtractFormat.WIKI)
    page = wiki.page(article)
    if not page.exists():
        logger.error(f"Wikipedia page '{article}' not found")
        return None

    logger.debug(f"Getting animal list started, waiting...")
    animal_list = sorted(page.categorymembers.keys())
    logger.debug(f"Animals list received: {animal_list.__len__()}\n")

    with open('beasts.csv', 'w', encoding='utf-8') as f:
        f.write("Количество животных на каждую букву алфавита:\n")

        """
        текущая буква = первая буква первого животного
        счётчик = 0
        Перебираем список животных
            если первая буква не изменилась
                счётчик += 1
            иначе
                текущую букву и счётчик дописываем в файл
                текущая буква = первая буква
                счётчик = 1
        текущую букву и счётчик дописываем в файл
        """
        count = 0
        current_letter = animal_list[0][0]
        for animal in animal_list:
            first_letter = animal[0]
            if animal[0] == current_letter:
                count += 1
            else:
                f.write(f"{current_letter}: {count}\n")
                current_letter = animal[0]
                count = 1
        f.write(f"{current_letter}: {count}\n")

