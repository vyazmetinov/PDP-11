import sys
sys.path.append('C:/proekt/PDP-11')


"""
Реализация команд эмулятора процессора.

Список команд:
- MOV: перенос данных между операндами.
- ADD: арифметическое сложение.
- HALT: завершение работы с выводом состояния регистров.


Формат обработки:
Каждая команда содержит маску, код операции, мнемонику и функцию-обработчик.
Параметры команд (ss, dd и др.) определяют режимы адресации.
"""

from virtual_executor.mem import w_read, w_write, reg, b_write,NZVC
from virtual_executor.args import ArgsProcessor
import sys

def setNZ(value):
    """Устанавливает флаги Negative (N) и Zero (Z) на основе 16-битного значения."""
    global NZVC
    NZVC[0] = (value >> 15) & 1  # N: старший бит (знак)
    NZVC[1] = 1 if (value & 0xFFFF) == 0 else 0  # Z: ноль

def setC(result):
    """Устанавливает флаги Carry (C) и Overflow (V) на основе 32-битного результата."""
    global NZVC
    NZVC[3] = (result >> 16) & 1  # C: перенос за пределы 16 бит
    # Overflow (V): переполнение знака при сложении
    NZVC[2] = 1 if ((result ^ (result >> 1)) & 0x8000) else 0

def do_mov(args):
    """Обработчик MOV: копирование из источника в приемник с обновлением флагов."""
    if args.dd and args.ss:
        value = args.ss.value
        args.dd.write(value)
        setNZ(value)  # Установка N и Z на основе значения
    else:
        raise ValueError("Ошибка аргументов MOV")

def do_add(args):
    """Обработчик ADD: сложение с обновлением флагов."""
    global NZVC

    if args.dd and args.ss:
        src = args.ss.value
        dst = args.dd.value
        result = src + dst  # 32-битный результат (учитывает переполнение)

        # Запись результата в приемник (16 бит)
        args.dd.write(result & 0xFFFF)

        # Установка флагов
        setNZ(result & 0xFFFF)  # N и Z на основе 16-битного результата
        setC(result)            # C и V на основе 32-битного результата

    else:
        raise ValueError("Ошибка аргументов ADD")

def do_halt(args):
    """Обработчик HALT: завершение работы с дампом регистров."""
    print("\n---------------- halted ---------------")
    reg_dump(reg)

def do_unknown(args):
    """Обработчик неизвестной команды."""
    print("\nUNKNOWN COMMAND")
    reg_dump(reg)


commands = [
    {'mask': 0o177777, 'opcode': 0o000000, 'name': 'halt', 'handler': lambda _args: do_halt(_args), 'params': ()},
    {'mask': 0o170000, 'opcode': 0o010000, 'name': 'mov', 'handler': lambda _args: do_mov(_args), 'params': ('ss', 'dd')},
    {'mask': 0o170000, 'opcode': 0o060000, 'name': 'add', 'handler': lambda _args: do_add(_args), 'params': ('ss', 'dd')},
    {'mask': 0o177777, 'opcode': 0o177777, 'name': 'unknown', 'handler': lambda _args: do_unknown(_args), 'params': ()}
]


def reg_dump(reg):
    print(f"r0={reg[0]:06o} r2={reg[2]:06o} r4={reg[4]:06o} sp={reg[6]:06o}")
    print(f"r1={reg[1]:06o} r3={reg[3]:06o} r5={reg[5]:06o} pc={reg[7]:06o}")

def execute_instruction() -> bool:
    """Выполнение инструкции с трассировкой."""
    args_processor = ArgsProcessor()
    pc = reg[7]
    try:
        instr = w_read(pc)
        print(f"{pc:06o}: {instr:06o}", end=' ')
        reg[7] += 2  # Увеличение PC после чтения инструкции
    except Exception as e:
        print(f"\nОшибка чтения инструкции: {e}")
        return False

    # Поиск подходящей команды
    cmd = next((c for c in commands if (instr & c['mask']) == c['opcode']), commands[-1])
    print(cmd['name'], end=' ')

    # Обработка аргументов
    try:
        args_processor.process(cmd['params'], instr)
        cmd['handler'](args_processor)
    except Exception as e:
        print(f"\nОшибка выполнения: {e}")
        return False

    print()  # Перевод строки после команды
    return True