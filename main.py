from currency import Currency
from data import Data


def file_operations() -> list:
    with open("test.txt") as file:
        currency_information = list()
        while True:
            first_rate = file.readline()
            if first_rate == "":
                break
            else:
                first_rate = first_rate[:-1]
            second_rate = file.readline()[:-1]
            rate = file.readline()[:-1]
            data = file.readline()
            if data[-1] == "\n":
                data = data[:-1]

            try:
                datas = Data(data)
            except ValueError as error:
                print(error)
                exit()

            try:
                currency_information.append(Currency(first_rate, second_rate, rate, datas))
            except RuntimeError as error:
                print(error)
                exit()

    return currency_information


def information(currency_information: list) -> None:
    for i in currency_information:
        print(f"Курс {i.SecondRate} на {i.FirstRate} составляет {i.rate} на {i.data}")


information(file_operations())