"""
Модуль обработки команд PDP-11
"""

from mem import reg, w_read, w_write

commands = [
    {'mask': 0o177777, 'opcode': 0o000000, 'name': 'halt'},
    {'mask': 0o177000, 'opcode': 0o010000, 'name': 'mov'},
    {'mask': 0o177000, 'opcode': 0o060000, 'name': 'add'}
]

def execute_instruction() -> bool:
    """Выполнение инструкции с выводом"""
    pc = reg[7]
    try:
        instr = w_read(pc)
    except:
        return False
    
    cmd = next((c for c in commands if (instr & c['mask']) == c['opcode']), None)
    
    # Вывод инструкции
    if cmd:
        if cmd['name'] == 'mov':
            src_mode = (instr >> 9) & 0o7
            src_reg = (instr >> 6) & 0o7
            dst_reg = instr & 0o7
            
            if src_mode == 2:
                value = w_read(pc + 2)
                print(f"{pc:06o}:   mov  #{value}, R{dst_reg}")
                reg[7] += 2  # Пропуск дополнительного слова
            else:
                print(f"{pc:06o}:   mov  R{src_reg}, R{dst_reg}")
        
        elif cmd['name'] == 'add':
            src_reg = (instr >> 6) & 0o7
            dst_reg = instr & 0o7
            print(f"{pc:06o}:   add  R{src_reg}, R{dst_reg}")
        
        elif cmd['name'] == 'halt':
            print(f"{pc:06o}:   halt")
            return False
    
    reg[7] += 2
    return True
