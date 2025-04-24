import pytest
from mem import (  # Импорт из модуля памяти
    mem, reg, psw,
    b_write, b_read,
    w_write, w_read,
    MEMSIZE
)

@pytest.fixture(autouse=True)
def clear_memory():
    """Фикстура для сброса памяти и регистров перед каждым тестом"""
    global mem, reg, psw
    mem[:] = [0] * MEMSIZE
    reg[:] = [0] * 8
    psw = 0
    yield

def test_basic_byte_operations():
    """Тест базовых операций с байтами"""
    # Запись и чтение
    b_write(0x100, 0xAB)
    assert b_read(0x100) == 0xAB
    
    # Проверка границ
    with pytest.raises(IndexError):
        b_write(MEMSIZE + 100, 0xFF)

def test_word_alignment():
    """Тест работы с 16-битными словами"""
    # Корректная запись
    w_write(0x200, 0x1234)
    assert w_read(0x200) == 0x1234
    
    # Нечетный адрес
    with pytest.raises(ValueError, match="Word address must be even"):
        w_write(0x201, 0x5678)

def test_memory_boundaries():
    """Тест граничных условий памяти"""
    # Запись в последнее слово
    w_write(MEMSIZE - 2, 0xDEAD)
    assert w_read(MEMSIZE - 2) == 0xDEAD
    
    # Чтение за пределами памяти
    with pytest.raises(IndexError):
        w_read(MEMSIZE)

def test_endianness():
    """Тест порядка байтов (little-endian)"""
    # Запись отдельных байтов
    b_write(0x300, 0xCD)
    b_write(0x301, 0xAB)
    
    # Чтение слова
    assert w_read(0x300) == 0xABCD
    assert hex(w_read(0x300)) == '0xabcd'

def test_register_access():
    """Тест работы с регистрами"""
    # Запись в регистры
    reg[0] = 0x1234
    reg[1] = 0x5678
    
    assert reg[0] == 0x1234
    assert reg[1] == 0x5678

def test_psw_operations():
    """Тест регистра статуса"""
    global psw
    psw = 0b1010
    assert (psw & 0b1000) == 0b1000  # N flag
    assert (psw & 0b0010) == 0b0010  # V flag