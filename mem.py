"""
Модуль работы с памятью PDP-11
"""

MEMSIZE = 65536  # 64KB памяти
mem = [0] * MEMSIZE
reg = [0] * 8     # Регистры R0-R7
psw = 0           # Регистр статуса (NZVC)

def b_write(address: int, value: int):
    if address < 0 or address >= MEMSIZE:
        raise IndexError("Memory address out of range")
    mem[address] = value & 0xFF

def b_read(address: int) -> int:
    if address < 0 or address >= MEMSIZE:
        raise IndexError("Memory address out of range")
    return mem[address]

def w_write(address: int, value: int):
    if address % 2 != 0:
        raise ValueError("Word address must be even")
    if address < 0 or address >= MEMSIZE - 1:
        raise IndexError("Memory address out of range")
    mem[address] = value & 0xFF
    mem[address + 1] = (value >> 8) & 0xFF

def w_read(address: int) -> int:
    if address % 2 != 0:
        raise ValueError("Word address must be even")
    if address < 0 or address >= MEMSIZE - 1:
        raise IndexError("Memory address out of range")
    return mem[address] | (mem[address + 1] << 8)