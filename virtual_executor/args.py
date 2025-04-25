"""
Реализация обработки аргументов команд и режимов адресации для эмулятора.

Ключевые компоненты:
- ModeRegistrArg: хранит адрес, значение и тип аргумента (регистр/память).
- ArgsProcessor: определяет режимы адресации и извлекает параметры команд.

Поддерживаемые режимы:
0: Прямая регистровая (R)
1: Косвенная регистровая (R)
2: Автоувеличение (R)+
3: Косвенный автоувеличение @(R)+
4: Автоуменьшение -(R)
5: Косвенный автоуменьшение @-(R)
6: Индексная X(R)
7: Косвенная индексная @X(R)
"""

from mem import reg, w_write, b_write, w_read

class ModeNotIplementedError(Exception):
    """Исключение при попытке использовать неподдерживаемый режим адресации."""
    pass


class ModeRegistrArg:
    """Хранит данные аргумента команды: адрес, значение и тип (регистр/память)."""

    def __init__(self, address: int, value: int, is_register: bool = False):
        self.address = address
        self.value = value
        self.is_register = is_register

    def write(self, value: int, is_word: bool = True):
        """Запись значения в регистр или память с учетом размера (слово/байт)."""
        if self.is_register:
            reg[self.address] = value & 0xFFFF
        else:
            if is_word:
                w_write(self.address, value)
            else:
                b_write(self.address, value)


class ArgsProcessor:
    """Обработчик аргументов команд, включая режимы адресации."""
    def __init__(self):
        self.ss = None
        self.dd = None
        self.nn = None
        self.xx = None
        self.r = None

    def clear(self):
        """Сброс всех параметров."""
        self.ss = None
        self.dd = None
        self.nn = None
        self.xx = None
        self.r = None

    @staticmethod
    def get_mr(w) -> ModeRegistrArg:
        """
        Анализирует слово команды, определяя режим адресации и регистр.
        
        Возвращает:
            ModeRegistrArg: объект с адресом, значением и типом аргумента.
        Исключения:
            ModeNotIplementedError: если режим не реализован.
            ValueError: при неверном выравнивании адреса.
        """
        r = w & 7
        mode = (w >> 3) & 7
        addr, value = 0, 0
        is_register = False

        if mode == 0:  # Регистровый
            addr = r
            value = reg[r]
            is_register = True
            print(f'r{r}', end=' ')

        elif mode == 1:  # Косвенный регистровый
            addr = reg[r]
            if addr % 2 != 0:
                raise ValueError(f"Unaligned word address {addr:06o}")
            value = w_read(addr)
            print(f'(r{r})', end=' ')

        elif mode == 2:  # Автоинкрементный
            addr = reg[r]
            if r == 7:  # Непосредственная адресация для PC
                value = w_read(addr)
                print(f'#{value:06o}', end=' ')
            else:
                value = w_read(addr)
                print(f'(r{r})+', end=' ')
            reg[r] += 2

        elif mode == 3:  # Автоинкрементный косвенный
            addr = reg[r]
            ptr = w_read(addr)
            value = w_read(ptr)
            reg[r] += 2
            print(f'@(r{r})+', end=' ')

        elif mode == 4:  # Автодекрементный
            reg[r] -= 2
            addr = reg[r]
            value = w_read(addr)
            print(f'-(r{r})', end=' ')

        elif mode == 5:  # Автодекрементный косвенный
            reg[r] -= 2
            addr = reg[r]
            ptr = w_read(addr)
            value = w_read(ptr)
            print(f'@-(r{r})', end=' ')

        elif mode == 6:  # Индексный
            offset = w_read(reg[7])
            reg[7] += 2
            addr = reg[r] + offset
            value = w_read(addr)
            print(f'{offset}(r{r})', end=' ')

        elif mode == 7:  # Индексный косвенный
            offset = w_read(reg[7])
            reg[7] += 2
            ptr = reg[r] + offset
            addr = w_read(ptr)
            value = w_read(addr)
            print(f'@{offset}(r{r})', end=' ')

        else:
            raise ModeNotIplementedError(f"Unsupported mode {mode}")

        return ModeRegistrArg(addr, value, is_register)

    def process(self, params: tuple, word: int):
        """
        Обрабатывает слово команды, извлекая аргументы в глобальный словарь args.

        Args:
            params (tuple): кортеж с типами параметров ('ss', 'dd' и т.д.)
            word (int): слово команды
        """
        self.clear()
        for param in params:
            if param == 'ss':
                self.ss = ArgsProcessor.get_mr(word >> 6)
            elif param == 'dd':
                self.dd = ArgsProcessor.get_mr(word & 0o77)
            elif param == 'r':
                self.r = (word >> 6) & 0o7
                print(f'r{self.r}', end=' ')
            elif param == 'nn':
                self.nn = word & 0o77
                print(f'{self.nn:o}', end=' ')
            else:
                raise ValueError(f'Unknown argument type {param}')

        return self.ss, self.dd