class Currency:
    "Информация о валюте в рублях"
    def __init__(self, FirstRate: str, SecondRate: str, rate: str, data) -> None:
        self.FirstRate, self.SecondRate, self.rate, self.data = FirstRate, SecondRate, rate, data
        self.CheckCurrency()
        self.CheckRate()

    def CheckCurrency(self) -> None:
        with open("Currency") as file:
            FirstRate, SecondRate = False, False
            while True:
                counter = file.readline()
                if (FirstRate == True and SecondRate == True):
                    break
                elif counter != "" and counter[-1] == "\n":
                    counter = counter[:-1]
                if counter == self.FirstRate:
                    FirstRate = True
                elif counter == self.SecondRate:
                    SecondRate = True
                if counter == "" and (FirstRate == False or SecondRate == False):
                    print(f"Такой валюты в файле нет! (неверно указанные валюта -> {self.FirstRate if FirstRate == False else ''}{', ' if FirstRate == False and SecondRate == False else ''}{self.SecondRate if SecondRate == False else ''})")
                    exit()
    def CheckRate(self) -> None:
        if not(self.rate.replace('.', '', 1).isdigit()):
            print(f"Валюта указана не числом!(валюта указана как -> {self.rate}:\nЧастая ошибка - указана ',' вместо'.'")
            exit()