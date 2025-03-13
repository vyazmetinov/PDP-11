mem = [0] * 65536 
reg = [0] * 8

def w_read(address):
    """Чтение слова по чётному адресу."""
    if address % 2 != 0:
        raise ValueError("Word address must be even")
    high = mem[address]
    low = mem[address + 1]
    return (high << 8) | low

def w_write(address, value):
    """Запись слова по чётному адресу."""
    if address % 2 != 0:
        raise ValueError("Word address must be even")
    mem[address] = (value >> 8) & 0xFF
    mem[address + 1] = value & 0xFF

def b_read(address):
    """Чтение байта."""
    return mem[address]

def b_write(address, value):
    """Запись байта."""
    mem[address] = value & 0xFF