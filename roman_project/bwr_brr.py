
MEMSIZE = 1024*64

mem = [0] * MEMSIZE

def b_write(adr, value):

    if adr < 0 or adr >= MEMSIZE:
        raise ValueError("Адрес выходит за пределы памяти")
    mem[adr] = value & 0xFF 

def b_read(adr):

    if adr < 0 or adr >= MEMSIZE:
        raise ValueError("Адрес выходит за пределы памяти")
    return mem[adr]


def w_write(adr, value):

    if adr < 0 or adr >= MEMSIZE - 1:
        raise ValueError("Адрес выходит за пределы памяти")
    if adr % 2 != 0:
        raise ValueError("Адрес слова должен быть четным")

    mem[adr] = value & 0xFF

    mem[adr + 1] = (value >> 8) & 0xFF


def w_read(adr):

    if adr < 0 or adr >= MEMSIZE - 1:
        raise ValueError("Адрес выходит за пределы памяти")
    if adr % 2 != 0:
        raise ValueError("Адрес слова должен быть четным")

    word = (mem[adr + 1] << 8) | mem[adr]
    return word & 0xFFFF  
