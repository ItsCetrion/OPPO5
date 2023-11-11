from currency import Currency


def file_operations() -> list:
    with open("test.txt") as file:
        currency_information = list()
        while True:
            exchange = list()
            for i in range(4):
                buffer = file.readline()
                if buffer == "":
                    break
                if buffer[-1] == '\n':
                    buffer = buffer[:-1]
                exchange.append(buffer)

            if len(exchange) != 0:
                try:
                    currency_information.append(Currency(exchange))
                except RuntimeError as error:
                    print(error)
                    exit()
            else:
                break

    return currency_information


def information(currency_information: list) -> None:
    for i in currency_information:
        print(f"Курс {i.SecondRate} на {i.FirstRate} составляет {i.rate} на {i.data}")


information(file_operations())