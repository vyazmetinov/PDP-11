from mem import b_write, mem, w_read
def load_data():
    """Загрузка данных из формата S-record из стандартного ввода."""
    import sys
    lines = []
    while True:
        line = sys.stdin.readline()
        if not line:
            break
        line = line.strip()
        if line:
            lines.append(line)
    ptr = 0
    while ptr < len(lines):
        header = lines[ptr]
        ptr += 1
        addr_hex, n_hex = header.split()
        address = int(addr_hex, 16)
        n = int(n_hex, 16)
        for i in range(n):
            if ptr >= len(lines):
                raise ValueError("Unexpected end of file")
            byte_str = lines[ptr].strip()
            ptr += 1
            byte = int(byte_str, 16)
            b_write(address + i, byte)

def mem_dump(adr, size):
    """Печать части памяти в формате PDP-11."""
    start = adr & ~1  # Выравнивание адреса на чётный
    end = adr + size
    end_aligned = (end + 1) & ~1  # Выравнивание конца на чётный

    current = start
    while current < end_aligned:
        try:
            word = w_read(current)
        except ValueError:
            break  # Выход за пределы памяти
        # Форматирование вывода: адрес (8-ричн.), слово (8-ричн. и 16-ричн.)
        print(f"{current:06o}: {word:06o} {word:04x}")
        current += 2