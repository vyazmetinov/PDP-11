"""
Модуль загрузки программ в память
"""

from mem import w_write, w_read

def load_data(filename: str) -> list:
    """Загрузка программы из файла в формате PDP-11"""
    with open(filename, 'r') as f:
        lines = [line.strip() for line in f if line.strip()]
    
    loaded = []
    ptr = 0
    
    while ptr < len(lines):
        # Пропуск S-записей
        if lines[ptr].startswith('S'):
            ptr += 1
            continue
        
        # Обработка строки с адресом и количеством слов
        if ' ' in lines[ptr]:
            addr_part, n_part = lines[ptr].split()
            ptr += 1
        else:
            addr_part = lines[ptr]
            n_part = lines[ptr + 1]
            ptr += 2
        
        address = int(addr_part, 8)
        n_words = int(n_part, 8)
        
        # Загрузка слов
        for _ in range(n_words):
            word = int(lines[ptr], 8)
            w_write(address, word)
            loaded.append(address)
            address += 2
            ptr += 1
    
    return loaded

def disassemble(start: int, end: int) -> None:
    """Дизассемблирование памяти"""
    addr = start
    while addr <= end:
        try:
            instr = w_read(addr)
        except:
            break
        
        cmd = None
        for c in commands:
            if (instr & c['mask']) == c['opcode']:
                cmd = c
                break
        
        output = f"{addr:06o}:   "
        words = [instr]
        
        if cmd:
            if cmd['name'] == 'mov':
                src_mode = (instr >> 9) & 0o7
                src_reg = (instr >> 6) & 0o7
                dst_reg = instr & 0o7
                
                if src_mode == 2:
                    value = w_read(addr + 2)
                    words.append(value)
                    output += f"mov  #{value}, R{dst_reg}"
                else:
                    output += f"mov  R{src_reg}, R{dst_reg}"
            
            elif cmd['name'] == 'add':
                src_reg = (instr >> 6) & 0o7
                dst_reg = instr & 0o7
                output += f"add  R{src_reg}, R{dst_reg}"
            
            elif cmd['name'] == 'halt':
                output += "halt"
        
        # Вывод машинных кодов
        print(output)
        for word in words:
            print(f"  {word:06o}")
        
        addr += 2 * len(words)

# Импорт таблицы команд
from command import commands
