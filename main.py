"""Главный файл проекта"""
import sys
import cProfile
# from memory_profiler import profile


def __doc__():
    return "Главная программа проекта"



# @profile
def file_operations() -> list:
    """Чтение файла и запись данных в массив"""
    with open("test.txt", encoding="utf-8") as file:
        currency_information = []
        while True:
            exchange = []
            for _i in range(4):
                buffer = file.readline()
                if buffer == "":
                    break
                if buffer[-1] == '\n':
                    buffer = buffer.rstrip('\n')
                exchange.append(buffer)

            if exchange:
                try:
                    currency_information.append(Currency(exchange))
                except RuntimeError as error:
                    print(error)
                    sys.exit()
            else:
                break

    return currency_information

# @profile
def information(currency_information: list) -> None:
    """Вывод информации на консоль"""
    for i in currency_information:
        print(f"Курс {i.second_rate} на {i.first_rate} "
              f"составляет {i.rate} на {i.data}")


information(file_operations())

cProfile.run('file_operations()')
