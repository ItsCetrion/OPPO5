from data import Data
class Currency:
    """Информация о валюте в рублях"""
    def __init__(self, valut) -> None:
        self.FirstRate, self.SecondRate, self.rate, self.data = valut[0], valut[1], valut[2], Data(valut[3])
        self.check_currency()
        self.check_rate()

    def check_currency(self) -> None:
        with open("Currency") as file:
            first_rate, second_rate = False, False

            while True:
                counter = file.readline()

                if first_rate is True and second_rate is True:
                    break
                elif counter != "" and counter[-1] == "\n":
                    counter = counter[:-1]

                if counter == self.FirstRate:
                    first_rate = True
                elif counter == self.SecondRate:
                    second_rate = True

                if counter == "" and (first_rate is False or second_rate is False):
                    raise TypeError(f"Такой валюты в файле нет! (неверно указанные валюта -> "
                                    f"{self.FirstRate if first_rate == False else ''}"
                                    f"{', ' if first_rate == False and second_rate == False else ''}"
                                    f"{self.SecondRate if second_rate == False else ''})")

    def check_rate(self) -> None:
        if not(self.rate.replace('.', '', 1).isdigit()):
            raise TypeError(f"Курс указана не числом!(валюта указана как -> {self.rate}):"
                            f"\nЧастая ошибка - указана ',' вместо'.'")
        else:
            try:
                int(self.rate[0])
                int(self.rate[-1])
            except ValueError:
                raise TypeError(f"Курс указана не числом!(валюта указана как -> {self.rate})")

            if self.rate.count(".") == 1:
                self.rate = float(self.rate)
            else:
                self.rate = int(self.rate)