import sys
sys.path.append('C:/proekt/PDP-11')


"""
Модуль загрузки данных и диагностики памяти.

Функционал:
- Загрузка бинарных данных в память эмулятора из текстового файла
- Визуализация содержимого памяти в формате дампа
"""

from virtual_executor.mem import b_write, w_read


def load_data(filename):
    print("LOAD...")
    """
    Загружает данные в память из файла специального формата.

    Формат файла:
        Блоки данных, каждый содержит:
        1. Строка с начальным адресом и размером данных (hex)
        2. Последовательность байтов (hex)

    Args:
        filename (str): Путь к файлу с данными

    Example:
        [Адрес] [Размер]
        1A
        FF
        ...
    """
    with open(filename, 'r') as file:
        while True:
            header = file.readline().strip()
            if not header:
                break  # Конец файла
            
            address, count = map(lambda x: int(x, 16), header.split())
            for offset in range(count):
                byte = int(file.readline().strip(), 16)
                b_write(address + offset, byte)
    print("SUCCESS")


def mem_dump(address, size):
    """
    Выводит форматированный дамп памяти.

    Формат вывода для каждого слова:
        [Адрес(oct)]: [Значение(oct)] [Значение(hex)]

    Args:
        address (int): Стартовый адрес в байтах
        size (int): Количество выводимых байт (округляется до четного)
    """
    # Выравнивание размера до четного числа
    size = size + 1 if size % 2 else size
    
    for offset in range(0, size, 2):
        current_addr = address + offset
        word = w_read(current_addr)
        print(f"{current_addr:06o}: {word:06o} {word:04x}")