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

from mem import w_read, w_write, reg, b_write, NZVC
from args import ArgsProcessor
import sys


def do_mov(args):
    """Обработчик MOV: копирование из источника в приемник."""
    if args.dd and args.ss:
        args.dd.write(args.ss.value)
    else:
        raise ValueError("Ошибка аргументов MOV")

def do_add(args):
    """Обработчик ADD: сложение с сохранением результата и обновлением флагов."""
    global NZVC  # Добавляем доступ к флагам

    if args.dd and args.ss:
        result = args.ss.value + args.dd.value
        args.dd.write(result & 0xFFFF)

        # Обновление флагов
        NZVC[0] = (result >> 15) & 1  # Negative (старший бит)
        NZVC[1] = 1 if (result & 0xFFFF) == 0 else 0  # Zero
        NZVC[2] = 1 if result > 0xFFFF else 0  # Overflow
        NZVC[3] = (result >> 16) & 1  # Carry
    else:
        raise ValueError("Ошибка аргументов ADD")

def do_halt(args):
    """Обработчик HALT: завершение работы с дампом регистров."""
    print("\n---------------- halted ---------------")
    reg_dump(reg)
    sys.exit(0)

def do_unknown(args):
    """Обработчик неизвестной команды."""
    print("\nUNKNOWN COMMAND")
    reg_dump(reg)
    sys.exit(1)


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