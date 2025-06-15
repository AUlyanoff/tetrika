# -*- coding: utf-8 -*-
import logging

logger = logging.getLogger(__name__)


def get_beasts():
    with open('beasts.csv', 'w', encoding='utf-8') as f:
        pass
        f.write("Количество животных на каждую букву алфавита.\n")
