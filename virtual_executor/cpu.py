from mem import w_read, w_write
 
reg = [0] * 8  # reg[7] используется как PC
psw = 0
 
def trace(message: str):
     """Функция трассировки для отладки"""
     print(f"[TRACE] {message}")
 
def get_operand(mode: int, reg_num: int) -> int:
     """Получение операнда с использованием match-case"""
     match mode:
         case 0:  
             trace(f'r{reg_num}')
             return reg[reg_num]
         case 1:  
             addr = reg[reg_num]
             return w_read(addr)
         case _:
             raise ValueError(f"Неизвестный режим адресации: {mode}")
 
def set_operand(mode: int, reg_num: int, value: int):
     """Установка значения операнда с использованием match-case"""
     match mode:
         case 0: 
             reg[reg_num] = value
         case 1: 
             addr = reg[reg_num]
             w_write(addr, value)
         case _:
             raise ValueError(f"Неизвестный режим адресации: {mode}")
 
def unknown_handler() -> bool:
     """Обработчик неизвестных команд с использованием reg[7]"""
     print(f"Неизвестная команда по адресу {reg[7]:06o}")
     reg[7] += 2
     return True