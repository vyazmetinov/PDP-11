# mem.py
mem = [0] * 65536

def w_read(address):
    if address % 2 != 0:
        raise ValueError("Нечётный адрес слова")
    return (mem[address + 1] << 8) | mem[address]

def w_write(address, value):
    if address % 2 != 0:
        raise ValueError("Нечётный адрес слова")
    mem[address] = value & 0xFF
    mem[address + 1] = (value >> 8) & 0xFF