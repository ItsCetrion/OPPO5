from datetime import datetime

dict_month = {1: "Января", 2: "Февраля", 3: "Марта", 4: "Апреля", 5: "Мая", 6: "Июня", 7: "Июля", 8: "Августа", 9: "Сентября", 10: "Октября", 11: "Ноября", 12: "Декабря"}
dict_days_in_month = {"Января": 31, "Февраля": (28, 29), "Марта": 31, "Апреля": 30, "Мая": 31, "Июня": 30, "Июля": 31, "Августа": 31, "Сентября": 30, "Октября": 31, "Ноября": 30, "Декабря": 31}

class Data:
    def __init__(self, data: str):
        data = data.split(".")
        self.flag = True
        self.FullData = data
        self.year = data[2]
        self.month = data[1]
        self.day = data[0]

    @staticmethod
    def ErrorInformation(value: str, regim: int, FullData: list) -> None:
        if regim == 1:
            print(f"указанный {value} некорректен в {FullData[0]}.{FullData[1]}.{FullData[2]}")
            exit()
        elif regim == 2:
            print(f"указынный {value} не является положительным целым числом в {FullData[0]}.{FullData[1]}.{FullData[2]}")
            exit()
    @property
    def year(self):
        return self._year

    @year.setter
    def year(self, value: str) -> None:
        if value.isdigit():
            value = int(value)
            self.LeapYear = False if (value % 4 == 0 and value % 100 != 0) or value % 400 == 0 else True
            if value <= datetime.today().year:
                self._year = value
            else:
                self.ErrorInformation("год", 1, self.FullData)
        else:
            self.ErrorInformation("год", 2, self.FullData)
    @property
    def month(self):
        return self._month

    @month.setter
    def month(self, value: str) -> None:
        if value.isdigit():
            if 1 <= int(value) <= 12:
                self._month = int(value)
            else:
                self.ErrorInformation("месяц", 1, self.FullData)
        else:
            self.ErrorInformation("месяц", 2, self.FullData)

    @property
    def day(self):
        return self._day

    @day.setter
    def day(self, value) -> None:
        if value.isdigit():
            if self.LeapYear == True and self.month == 2:
                if 1 <= int(value) <= dict_days_in_month.get(dict_month.get(self.month))[0]:
                    self._day = int(value)
                else:
                    self.ErrorInformation("день", 1, self.FullData)
            elif self.LeapYear == False and self._month == 2:
                if 1 <= int(value) <= dict_days_in_month.get(dict_month.get(self.month))[1]:
                    self._day = int(value)
                else:
                    self.ErrorInformation("день", 1, self.FullData)
            elif 1 <= int(value) <= dict_days_in_month.get(dict_month.get(self.month)):
                self._day = int(value)
            else:
                self.ErrorInformation("день", 1, self.FullData)
        else:
            self.ErrorInformation("день", 2, self.FullData)

    def __str__(self) -> str:
        return f"{self.day} {dict_month.get(self.month)} {self.year}"