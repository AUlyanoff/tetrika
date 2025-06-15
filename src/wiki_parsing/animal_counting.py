# -*- coding: utf-8 -*-
import logging

import wikipediaapi

logger = logging.getLogger(__name__)


def get_beasts(article: str, agent: str = 'Tetrika (junir@tetrika.com)'):
    """Подсчёт количества животных на каждую букву алфавита"""

    wiki = wikipediaapi.Wikipedia(user_agent=agent, language="ru")
    page = wiki.page(article)
    if not page.exists():
        logger.error(f"Wikipedia page '{article}' not found")
        return None

    logger.debug(f"Getting animal list started, waiting...")
    animal_list = sorted(page.categorymembers.keys())
    logger.debug(f"Animals list received: {animal_list.__len__()}\n")

    with open('beasts.csv', 'w', encoding='utf-8') as f:
        f.write("Количество животных на каждую букву алфавита:\n")
        count = total = 0
        current_letter = animal_list[0][0]                  # текущая буква = первая буква первого животного
        for animal in animal_list:
            if animal[0] == current_letter:                 # если первая буква не изменилась
                count += 1
            else:
                f.write(f"{current_letter}: {count}\n")     # дописываем текущую букву и счётчик повторений
                logger.debug(f"'{current_letter}' completed: {count}")
                total += count
                current_letter = animal[0]                  # текущая буква = первая буква текущего животного
                count = 1                                   # потому что первая буква текущего животного изменилась
        f.write(f"{current_letter}: {count}\n")             # дописываем последнюю букву и счётчик повторений
        logger.debug(f"'{current_letter}' completed: {count}")
        total += count

        if animal_list.__len__() != total:
            logger.warning('Total animals number not equal animals list length')

    logger.debug(f"Counting completed: {total}")
    return True
