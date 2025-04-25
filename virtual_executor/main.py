import sys
sys.path.append('C:/proekt/PDP-11')

"""
Основной модуль эмулятора PDP-11.

Содержит точку входа и цикл выполнения инструкций.
"""

from virtual_executor.mem import w_read, reg, NZVC, mem
from virtual_executor.commands import commands, ArgsProcessor
from virtual_executor.data_load import load_data


def main():
    load_data("pdp_11.o")
    reg[7] = 0o1000
    print("---------------- running --------------")
    args = ArgsProcessor()

    while True:
        changes = execute_and_track(args)
        print("Изменения:", changes)
    return changes

def execute_and_track(args):
    """Выполняет команду и возвращает изменения в mem, reg, NZVC."""
    # Сохраняем исходные состояния
    old_mem = mem.copy()
    old_reg = reg.copy()
    old_NZVC = NZVC.copy()

    # Выполняем команду
    do_command(args)

    # Находим изменения
    mem_changes = [i for i in range(len(mem)) if mem[i] != old_mem[i]]
    reg_changes = [i for i in range(len(reg)) if reg[i] != old_reg[i]]
    nzvc_changes = [i for i in range(4) if NZVC[i] != old_NZVC[i]]

    return {
        "mem": mem_changes,
        "reg": reg_changes,
        "nzvc": nzvc_changes
    }


def do_command(args):
    """Обрабатывает одну команду."""
    # Чтение инструкции и увеличение PC
    word = w_read(reg[7])
    print(f"{reg[7]:06o}:", end=" ")
    reg[7] += 2

    # Поиск и выполнение команды
    for cmd in commands:
        if (word & cmd["mask"]) == cmd["opcode"]:
            print(cmd["name"], end=" ")
            args.process(cmd["params"], word)
            cmd["handler"](args)
            print()
            break


if __name__ == "__main__":
    main()