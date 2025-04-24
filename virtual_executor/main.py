"""
Главный модуль эмулятора
"""

from mem import reg
from data_load import load_data, disassemble
from command import execute_instruction

def main():
    print("000000:   . = 1000")
    reg[7] = 0o1000  # Инициализация PC
    
    print("\nЗагрузка программы...")
    loaded_addrs = load_data("01_sum.pdp.o")
    
    if loaded_addrs:
        start = min(loaded_addrs)
        end = max(loaded_addrs) + 2
        print("\nДизассемблирование программы:")
        disassemble(start, end)
    
    print("\nВыполнение программы:")
    while execute_instruction():
        pass

if __name__ == "__main__":
    main()
