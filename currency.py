"""Файл с классом, в котором храниться данные информация по валюте и курсу валют"""
from data import Data


class Currency:
    """Информация о валюте в рублях"""
    def __init__(self, valut: list) -> None:
        self.first_rate, self.second_rate, self.rate, self.data = \
            valut[0], valut[1], valut[2], Data(valut[3])
        self.check_currency()
        self.check_rate()

    def check_currency(self) -> None:
        """Проверка валидности валюты"""
        with open("Currency", encoding='utf-8') as file:
            first_rate, second_rate = False, False

            while True:
                counter = file.readline()

                if first_rate is True and second_rate is True:
                    break
                if counter != "" and counter[-1] == "\n":
                    counter = counter[:-1]

                if counter == self.first_rate:
                    first_rate = True
                elif counter == self.second_rate:
                    second_rate = True

                if counter == "" and (first_rate is False or second_rate is False):

                    raise TypeError(f"Такой валюты в файле нет! (неверно указанные валюта -> "
                                    f"{self.first_rate if not first_rate else ''}"
                                    f"{', ' if not first_rate and not second_rate else ''}"
                                    f"{self.second_rate if not second_rate else ''})")

    def check_rate(self) -> None:
        """Проверка валидности ставки по курсу валют"""
        if not self.rate.replace('.', '', 1).isdigit():
            raise TypeError(f"Курс указана не числом!(валюта указана как -> {self.rate}):"
                            f"\nЧастая ошибка - указана ',' вместо'.'")
        try:
            int(self.rate[0])
            int(self.rate[-1])
        except ValueError as exc:
            raise TypeError(f"Курс указана не числом!(валюта указана как -> {self.rate})") from exc

        if self.rate.count(".") == 1:
            self.rate = float(self.rate)
        else:
            self.rate = int(self.rate)
