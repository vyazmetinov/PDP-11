"""
Модуль эмуляции памяти и регистров PDP-11.

Реализует:
- Байт-адресуемую память объемом 64 КБ
- 8 регистров общего назначения (R0-R7)
- Базовые операции для работы с памятью (чтение/запись слов и байтов)

Особенности архитектуры:
- Слово состоит из двух байтов, требует выровненных по четным адресам операций
- Регистры хранят 16-битные значения в формате little-endian
"""

MEMSIZE = 64 * 1024  # Объем памяти в байтах

mem = [0] * MEMSIZE  # Основной массив памяти
reg = [0] * 8        # Регистры общего назначения R0-R7
NZVC = [0, 0, 0, 0]  # Negative, Zero, Overflow, Carry


def b_write(adr, value):
    """
    Записывает младший байт значения по указанному адресу памяти.

    Args:
        adr (int): Целевой адрес (0 <= adr < MEMSIZE)
        value (int): Записываемое значение (используется младший байт)

    Raises:
        IndexError: При выходе за границы памяти
    """
    mem[adr] = value & 0xFF


def b_read(adr):
    """
    Возвращает байт из памяти по указанному адресу.

    Args:
        adr (int): Адрес для чтения (0 <= adr < MEMSIZE)

    Returns:
        int: Значение байта в диапазоне 0-255

    Raises:
        IndexError: При выходе за границы памяти
    """
    return mem[adr]


def w_write(adr, value):
    """
    Записывает 16-битное слово в память по четному адресу (little-endian).

    Args:
        adr (int): Четный адрес для записи (0 <= adr < MEMSIZE-1)
        value (int): Значение для записи (используется младшие 16 бит)

    Raises:
        ValueError: При нечетном адресе
        IndexError: При выходе за границы памяти
    """
    if adr % 2 != 0:
        raise ValueError("Word address must be even")
    mem[adr] = value & 0xFF          # Младший байт
    mem[adr + 1] = (value >> 8) & 0xFF  # Старший байт


def w_read(adr):
    """
    Читает 16-битное слово из памяти по четному адресу (little-endian).

    Args:
        adr (int): Четный адрес для чтения (0 <= adr < MEMSIZE-1)

    Returns:
        int: 16-битное значение в диапазоне 0-65535

    Raises:
        ValueError: При нечетном адресе
        IndexError: При выходе за границы памяти
    """
    if adr % 2 != 0:
        raise ValueError("Word address must be even")
    return mem[adr] | (mem[adr + 1] << 8)