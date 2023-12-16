"""файл для проверки программы"""
import unittest
from currency import Currency
from data import Data


class MyTestCase(unittest.TestCase):
    """Тесты проекты"""
    def test_day(self):
        """Тест параметра 'день'"""
        self.assertEqual(Data("22.02.2021").day, 22)
        cases = ["-1.02.2021", "33.02.2021", "0.02.2021", "dfsdf.02.2021", "True.02.2021"]
        for cs in cases:
            with self.assertRaises(TypeError):
                Data(cs)

    def test_month(self):
        """Тест параметра 'месяц'"""
        self.assertEqual(Data("23.02.2021").month, 2)
        cases = ["23.-1.2021", "23.0.2021", "23.13.2021", "23.'08'.2021", "23.True.2021"]
        for cs in cases:
            with self.assertRaises(TypeError):
                Data(cs)

    def test_year(self):
        """Тест параметра 'год'"""
        self.assertEqual(Data("24.02.2021").year, 2021)
        cases = ["24.02.2025", "24.02.0", "24.02.-1", "24.02.fdsf", "24.02.True"]
        for cs in cases:
            with self.assertRaises(TypeError):
                Data(cs)

    def test_leap_year(self):
        """Тест параметра 'високосный год'"""
        self.assertEqual(Data("28.02.2021").day, 28)
        self.assertEqual(Data("29.02.2020").day, 29)
        with self.assertRaises(TypeError):
            Data("29.02.2021")

        self.assertEqual(Data("28.02.2021").is_leap_year(2022), True)
        self.assertEqual(Data("28.02.2021").is_leap_year(2020), False)

    def test_currency(self):
        """Тест параметра 'валюта'"""
        self.assertEqual(Currency(["USD", "EUR", "97.5", "22.02.2021"]).first_rate, "USD")
        self.assertEqual(Currency(["USD", "EUR", "97.5", "22.02.2021"]).second_rate, "EUR")
        with self.assertRaises(TypeError):
            Currency(["FDFD", "EUR", "97.5", "22.02.2021"])
            Currency(["USD", "FDFD", "97.5", "22.02.2021"])

    def test_rate(self):
        """Тест параметра 'курс валюты'"""
        self.assertEqual(Currency(["USD", "EUR", "97.5", "22.02.2021"]).rate, 97.5)
        with self.assertRaises(TypeError):
            Currency(["USD", "EUR", ".123", "22.02.2021"])
            Currency(["USD", "EUR", "123.", "22.02.2021"])
            Currency(["USD", "EUR", "12..3", "22.02.2021"])

    def test_data_init_err(self):
        """Общий тест класса 'data.py'"""
        cases = ["30.02.1992", "32.11.2014", "15.09.2000.200"]
        for cs in cases:
            with self.assertRaises(TypeError):
                Data(cs)

    def test_strip(self):
        """Тест функции разделения даты на составляющие """
        cases = ["23,11.2011", "23,3,2001", "11.11.2004.332.323.434.21", "22", "21.11"]
        for cs in cases:
            with self.assertRaises(TypeError):
                Data(cs)


if __name__ == '__main__':
    unittest.main()
