import unittest

from app.type_checking.funcs import sum_two_int


class DecoratorStrict(unittest.TestCase):
    """Проверка декоратора @strict"""

    def test_add(self):
        """Верный тип аргументов"""
        self.assertEqual(sum_two_int(1, 2), 3)

    def test_bad_float(self):
        """Неверный float"""
        with self.assertRaises(TypeError):
            sum_two_int(1, 1.)

    def test_bad_bool(self):
        """Неверный bool"""
        with self.assertRaises(TypeError):
            sum_two_int(1, True)

    def test_bad_str(self):
        """Неверный str"""
        with self.assertRaises(TypeError):
            sum_two_int(1, 'string')

if __name__ == '__main__':
    unittest.main()
