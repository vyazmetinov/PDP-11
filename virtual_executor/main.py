"""
Основной модуль эмулятора PDP-11.

Содержит точку входа и цикл выполнения инструкций.
"""

from mem import w_read, reg
from commands import commands, ArgsProcessor
from data_load import load_data


def main():
    """
    Главная функция эмулятора.
    
    Этапы работы:
    1. Инициализация памяти и регистров
    2. Загрузка программы в память
    3. Цикл выборки-декодирования-выполнения команд
    """
    load_data("pdp_11.o")

    reg[7] = 0o1000
    print("---------------- running --------------")

    args = ArgsProcessor()
    while True:
        word = w_read(reg[7])
        print(f"{reg[7]:06o}:", end=" ")
        reg[7] += 2

        for cmd in commands:
            if (word & cmd["mask"]) == cmd["opcode"]:
                print(cmd["name"], end=" ")

                args.process(cmd["params"], word)

                cmd["handler"](args)
                print()
                break


if __name__ == "__main__":
    main()