from mem import mem, w_read, w_write, b_write, load_data 
from data_load import mem_dump
from cpu import unknown_handler, get_operand, set_operand
from collections import defaultdict

pc = 0o1000
reg = [0] * 8
psw = 0
labels = defaultdict(str) 
comments = defaultdict(str)

commands = [
    {'mask': 0o177777, 'opcode': 0o000000, 'name': 'halt', 'handler': lambda: False},
    {'mask': 0o170000, 'opcode': 0o010000, 'name': 'mov', 'handler': lambda: mov_handler()},
    {'mask': 0o170000, 'opcode': 0o060000, 'name': 'add', 'handler': lambda: add_handler()},
    {'mask': 0o000000, 'opcode': 0o177777, 'name': 'unknown', 'handler': lambda: unknown_handler()}
]

def load_data_with_metadata():
    """Загрузка данных с метками и комментариями"""
    import sys
    lines = []
    addr_map = {}

    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        
        if line.startswith('#'):
            parts = line[1:].split(':', 1)
            if len(parts) == 2:
                addr = int(parts[0].strip(), 8)
                comments[addr] = parts[1].strip()
            continue
        
        if line.endswith(':'):
            label = line[:-1]
            addr = int(lines[-1].split()[0], 16) if lines else 0o1000
            labels[addr] = label
            continue
            
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
                break
            byte_str = lines[ptr].strip()
            ptr += 1
            byte = int(byte_str, 16)
            b_write(address + i, byte)

def print_state():
    """Вывод полного состояния системы"""
    print("\n——- Текущее состояние ——-")
    
    print("\nРегистры:")
    for i in range(8):
        print(f"R{i}: {reg[i]:06o} ({reg[i]:5d})")

    n = (psw >> 3) & 1
    z = (psw >> 2) & 1
    v = (psw >> 1) & 1
    c = (psw >> 0) & 1
    print(f"\nФлаги: N={n} Z={z} V={v} C={c}")
    

    print("\nПамять (стек и данные):")
    mem_dump(0o1000, len(mem) - 0o1000)
    
    print("——-" * 20 + "\n")

def execute_instruction():
    global pc
    try:
        instruction = w_read(pc)
    except (ValueError, IndexError):
        print(f"{pc:06o}: {'??????':6} : memory_error")
        return False

    cmd = next((c for c in commands if (instruction & c['mask']) == c['opcode']), commands[-1])
    
    args = ""
    if cmd['name'] == 'mov':
        src_mode = (instruction >> 6) & 0o7
        src_reg = (instruction >> 9) & 0o7
        dst_mode = (instruction >> 0) & 0o7
        dst_reg = (instruction >> 3) & 0o7
        args = f"R{src_reg}, R{dst_reg}"

    print(f"\n0) Метка: {labels.get(pc, '')}")
    print(f"1) Адрес: {pc:06o}")
    print(f"2) Слово команды: {instruction:06o}")
    print(f"3) Аргументы: {args}")
    print(f"4) Комментарий: {comments.get(pc, '')}")
    

    result = cmd['handler']()
    

    print_state()
    
    return result

def mov_handler():
    global pc
    instruction = w_read(pc)
    src_mode = (instruction >> 6) & 0o7
    src_reg = (instruction >> 9) & 0o7
    dst_mode = (instruction >> 0) & 0o7
    dst_reg = (instruction >> 3) & 0o7
    
    src = get_operand(src_mode, src_reg)
    set_operand(dst_mode, dst_reg, src)
    
    pc += 2
    return True

def add_handler():
    global pc, psw
    instruction = w_read(pc)
    src_mode = (instruction >> 6) & 0o7
    src_reg = (instruction >> 9) & 0o7
    dst_reg = (instruction >> 0) & 0o7
    
    src = get_operand(src_mode, src_reg)
    dst = reg[dst_reg]
    res = (dst + src) & 0xFFFF
    

    psw = 0
    psw |= (res >> 15) << 3
    psw |= (res == 0) << 2
    
    reg[dst_reg] = res
    pc += 2
    return True
