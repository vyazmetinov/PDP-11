from mem import mem, w_read, w_write, b_write, load_data 
from data_load import mem_dump
from cpu import unknown_handler, get_operand, set_operand, mov_handler, add_handler
from collections import defaultdict
 
reg = [0] * 8  # reg[7] используется как PC
psw = 0
labels = defaultdict(str)
comments = defaultdict(str)
 
commands = [
     {'mask': 0o177777, 'opcode': 0o000000, 'name': 'halt', 'handler': lambda: False},
     {'mask': 0o170000, 'opcode': 0o010000, 'name': 'mov', 'handler': mov_handler},
     {'mask': 0o170000, 'opcode': 0o060000, 'name': 'add', 'handler': add_handler},
     {'mask': 0o000000, 'opcode': 0o177777, 'name': 'unknown', 'handler': unknown_handler}
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
     try:
         instruction = w_read(reg[7])
     except (ValueError, IndexError):
         print(f"{reg[7]:06o}: {'??????':6} : memory_error")
         return False
 
     cmd = next((c for c in commands if (instruction & c['mask']) == c['opcode']), commands[-1])
     
     # Универсальный разбор аргументов
     args = []
     arg_types = [
         ('ss', 6, 0o7, 9, 0o7),
         ('dd', 0, 0o7, 3, 0o7),
     ]
     
     arg_info = []
     for arg_name, mode_shift, mode_mask, reg_shift, reg_mask in arg_types:
         mode = (instruction >> mode_shift) & mode_mask
         reg_num = (instruction >> reg_shift) & reg_mask
         if mode != 0 or reg_num != 0:
             args.append((mode, reg_num))
             arg_info.append(f"{arg_name}(mode={mode}, R{reg_num})")
 
     print(f"\n0) Метка: {labels.get(reg[7], '')}")
     print(f"1) Адрес: {reg[7]:06o}")
     print(f"2) Слово команды: {instruction:06o}")
     print(f"3) Аргументы: {', '.join(arg_info)}")
     print(f"4) Комментарий: {comments.get(reg[7], '')}")
 
     # Выполнение команды
     result = cmd['handler'](*args)
     
     # Увеличение PC после выполнения
     reg[7] += 2
     
     print_state()
     return result
 
def setNZ(value):
     global psw
     psw &= ~0b1100
     psw |= ((value & 0x8000) >> 12) | ((value == 0) << 2)
 
def mov_handler(*args):
     if len(args) != 2:
         return False
     
     src_mode, src_reg = args[0]
     dst_mode, dst_reg = args[1]
     
     src_val = get_operand(src_mode, src_reg)
     set_operand(dst_mode, dst_reg, src_val)
     return True
 
def add_handler(*args):
     if len(args) != 2:
         return False
     
     src_mode, src_reg = args[0]
     dst_mode, dst_reg = args[1]
     
     src_val = get_operand(src_mode, src_reg)
     dst_val = get_operand(dst_mode, dst_reg)
     res = (dst_val + src_val) & 0xFFFF
     
     setNZ(res)
     set_operand(dst_mode, dst_reg, res)
     return True