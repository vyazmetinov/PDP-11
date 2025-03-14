from mem import w_read, w_write

pc = 0o1000
reg = [0] * 8
psw = 0

def get_operand(mode, reg_num):
    if mode == 0:  # Регистровый режим
        return reg[reg_num]
    elif mode == 1:  # Косвенный регистровый
        addr = reg[reg_num]
        return w_read(addr)
    else:
        raise ValueError(f"Неизвестный режим адресации: {mode}")

def set_operand(mode, reg_num, value):
    if mode == 0:
        reg[reg_num] = value
    elif mode == 1:
        addr = reg[reg_num]
        w_write(addr, value)
    else:
        raise ValueError(f"Неизвестный режим адресации: {mode}")

def unknown_handler():
    global pc
    print(f"Неизвестная команда по адресу {pc:06o}")
    pc += 2
    return True