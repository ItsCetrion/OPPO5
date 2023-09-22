from currensy import Currency
from data import Data
def file_operations() -> list:
    with open("test.txt") as file:
        CurrencyInformation = list()
        while True:
            FirstRate = file.readline()
            if FirstRate == "":
                break
            else:
                FirstRate = FirstRate[:-1]
            SecondRate = file.readline()[:-1]
            rate = file.readline()[:-1]
            data = file.readline()
            if data[-1] == "\n":
                data = data[:-1]

            datas = Data(data)
            CurrencyInformation.append(Currency(FirstRate, SecondRate, rate, datas))
    return CurrencyInformation
def information(CurrencyInformation: list) -> None:
    for i in CurrencyInformation:
        print(f"Курс {i.SecondRate} на {i.FirstRate} составляет {i.rate} на {i.data}")

information(file_operations())