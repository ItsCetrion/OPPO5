"""Файл с классом, в котором храниться данные информация по дате"""
from datetime import datetime

dict_month = {1: "Января", 2: "Февраля", 3: "Марта", 4: "Апреля", 5: "Мая", 6: "Июня",
              7: "Июля", 8: "Августа", 9: "Сентября", 10: "Октября", 11: "Ноября", 12: "Декабря"}
dict_days_in_month = {"Января": 31, "Февраля": (28, 29), "Марта": 31, "Апреля": 30,
                      "Мая": 31, "Июня": 30, "Июля": 31,
                      "Августа": 31, "Сентября": 30, "Октября": 31, "Ноября": 30, "Декабря": 31}


class Data:
    """Информация о передаваемой дате"""
    def __init__(self, data: str):
        data = self.split(data)
        self.leap_year = False
        self.full_data = data
        self.year = data[2]
        self.month = data[1]
        self.day = data[0]

    @staticmethod
    def split(data: str) -> list:
        """Разбиение даты на составляющие"""
        string = data
        data = data.split(".")
        if len(data) != 3:
            raise TypeError(f"Дата указана неверно, дата указана как {string} "
                            f"(частая ошибка введено ',', a не '.')")
        return data

    @staticmethod
    def __error_information(value: str, regim: int, full_data: list) -> None:
        """Вывод ошибок"""
        if regim == 1:
            raise TypeError(f"указанный {value} некорректен в "
                            f"{full_data[0]}.{full_data[1]}.{full_data[2]}")
        if regim == 2:
            raise TypeError(f"указанный {value} не является положительным целым числом в "
                            f"{full_data[0]}.{full_data[1]}.{full_data[2]}")

    @property
    def year(self):
        """Получение атрибута 'год'"""
        return self._year

    @staticmethod
    def is_leap_year(value: int):
        """Определение високосного года"""
        return False if (value % 4 == 0 and value % 100 != 0) or value % 400 == 0 else True

    @year.setter
    def year(self, value: str) -> None:
        """Установка атрибута 'год'"""
        if value.isdigit():
            value = int(value)
            self.leap_year = self.is_leap_year(value)
            if 1 <= value <= datetime.today().year:
                self._year = value
            else:
                self.__error_information("год", 1, self.full_data)
        else:
            self.__error_information("год", 2, self.full_data)

    @property
    def month(self):
        """Получение атрибута 'месяц'"""
        return self._month

    @month.setter
    def month(self, value: str) -> None:
        """Установка атрибута 'месяц'"""
        if value.isdigit():
            if 1 <= int(value) <= 12:
                self._month = int(value)
            else:
                self.__error_information("месяц", 1, self.full_data)
        else:
            self.__error_information("месяц", 2, self.full_data)

    @property
    def day(self):
        """Получение атрибута 'день'"""
        return self._day

    @day.setter
    def day(self, value) -> None:
        """Установка атрибута 'день'"""
        if value.isdigit():
            if self.leap_year is True and self.month == 2:
                if 1 <= int(value) <= dict_days_in_month.get(dict_month.get(self.month))[0]:
                    self._day = int(value)
                else:
                    self.__error_information("день", 1, self.full_data)
            elif self.leap_year is False and self._month == 2:
                if 1 <= int(value) <= dict_days_in_month.get(dict_month.get(self.month))[1]:
                    self._day = int(value)
                else:
                    self.__error_information("день", 1, self.full_data)
            elif 1 <= int(value) <= dict_days_in_month.get(dict_month.get(self.month)):
                self._day = int(value)
            else:
                self.__error_information("день", 1, self.full_data)
        else:
            self.__error_information("день", 2, self.full_data)

    def __str__(self) -> str:
        return f"{self.day} {dict_month.get(self.month)} {self.year}"
