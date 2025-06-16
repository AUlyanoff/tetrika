import unittest
from unittest.mock import patch

from app.wiki_parsing.solution import get_beasts


class WikiParse(unittest.TestCase):
    """Проверка парсинга Википедии"""

    def setUp(self):
        self.existing_article = 'Категория:Животные по алфавиту'
        self.non_existent_article = 'Кверти Фывапролджэ Ячсмитьбю'
        self.wiki_output = {'Аардоникс': 0, 'Абботины': 0, 'Баран': 0, 'Бегемот': 0, 'Junior': 0}

    def test_ok(self):
        """Статья существует"""
        # Замокаем самую дорогую операцию - получение всех категорий страницы
        with patch('wikipediaapi.WikipediaPage.categorymembers', new=self.wiki_output):
            result = get_beasts(self.existing_article)
        self.assertTrue(result, f"Ожидалось существование статьи {self.existing_article}")

    def test_not_exist(self):
        """Статья не существует"""
        result = get_beasts(self.non_existent_article)
        self.assertFalse (result, f"Ожидалось отсутствие статьи {self.non_existent_article}")


if __name__ == '__main__':
    unittest.main()
