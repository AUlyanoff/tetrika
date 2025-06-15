import unittest

from app.study_time.counting import appearance
from tests.resource import lessons_right, lessons_odd, lessons_bad

class StudyTime(unittest.TestCase):
    """Проверка вычисления времени присутствия учителя и ученика"""

    def test_right(self):
        """Подсчитано верно"""
        for lesson_right in lessons_right:
            calculated = appearance(lesson_right['intervals'])
            self.assertEqual(calculated, lesson_right["answer"], "неверно высчитано суммарное время присутствия")

    def test_bad(self):
        """Подсчитано неверно"""
        for lesson_bad in lessons_bad:
            calculated = appearance(lesson_bad['intervals'])
            self.assertNotEquals(calculated, lesson_bad["answer"], "неверно высчитано суммарное время присутствия")

    def test_odd(self):
        """Нечётное количество таймштампов"""
        for lesson_odd in lessons_odd:
            calculated = appearance(lesson_odd['intervals'])
            self.assertEqual(calculated, -1, "неверно высчитано суммарное время присутствия")


if __name__ == '__main__':
    unittest.main()
