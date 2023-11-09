import unittest
from data import Data
from currency import Currency


class MyTestCase(unittest.TestCase):
    def test_day(self):
        self.assertEqual(Data("22.02.2021").day, 22)
        with self.assertRaises(TypeError):
            Data("-1.02.2021")
            Data("33.02.2021")
            Data("0.02.2021")
            Data("dfsdf.02.2021")
            Data("True.02.2021")

    def test_month(self):
        self.assertEqual(Data("23.02.2021").month, 2)
        with self.assertRaises(TypeError):
            Data("23.-1.2021")
            Data("23.0.2021")
            Data("23.13.2021")
            Data("23.'08'.2021")
            Data("23.True.2021")

    def test_year(self):
        self.assertEqual(Data("24.02.2021").year, 2021)
        with self.assertRaises(TypeError):
            Data("24.02.2025")
            Data("24.02.0")
            Data("24.02.-1")
            Data("24.02.fdsf")
            Data("24.02.True")

    def test_LeapYear(self):
        self.assertEqual(Data("28.02.2021").day, 28)
        self.assertEqual(Data("29.02.2020").day, 29)
        with self.assertRaises(TypeError):
            Data("29.02.2021")

        self.assertEqual(Data("28.02.2021").is_leap_year(2022), True)
        self.assertEqual(Data("28.02.2021").is_leap_year(2020), False)

    def test_Currency(self):
        self.assertEqual(Currency("USD", "EUR", "97.5", Data("22.02.2021")).FirstRate, "USD")
        self.assertEqual(Currency("USD", "EUR", "97.5", Data("22.02.2021")).SecondRate, "EUR")
        with self.assertRaises(TypeError):
            Currency("FDFD", "EUR", "97.5", Data("22.02.2021"))
            Currency("USD", "FDFD", "97.5", Data("22.02.2021"))

    def test_Rate(self):
        self.assertEqual(Currency("USD", "EUR", "97.5", Data("22.02.2021")).rate, 97.5)
        with self.assertRaises(TypeError):
            Currency("USD", "EUR", ".123", Data("22.02.2021"))
            Currency("USD", "EUR", "123.", Data("22.02.2021"))
            Currency("USD", "EUR", "12..3", Data("22.02.2021"))


if __name__ == '__main__':
    unittest.main()
