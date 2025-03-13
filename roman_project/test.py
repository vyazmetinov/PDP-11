from mem import mem, reg, w_read, w_write, b_read, b_write
import pytest

@pytest.fixture(autouse=True)
def reset_memory():
    global mem, reg
    mem = [0] * 65536
    reg = [0] * 8

def test_w_read_valid_address():
    """Тест чтения слова по чётному адресу."""
    w_write(0x1000, 0x1234)
    value = w_read(0x1000)
    assert value == 0x1234

def test_w_read_invalid_address():
    """Тест чтения слова по нечётному адресу."""
    with pytest.raises(ValueError, match="Word address must be even"):
        w_read(0x1001)  

def test_w_write_valid_address():
    """Тест записи слова по чётному адресу."""
    w_write(0x2000, 0x5678)
    assert mem[0x2000] == 0x56
    assert mem[0x2001] == 0x78

def test_w_write_invalid_address():
    """Тест записи слова по нечётному адресу."""
    with pytest.raises(ValueError, match="Word address must be even"):
        w_write(0x2001, 0x5678)

def test_b_read():
    """Тест чтения байта."""
    b_write(0x3000, 0xAB)

    value = b_read(0x3000)
    assert value == 0xAB

def test_b_write():
    """Тест записи байта."""
    b_write(0x4000, 0xCD)
    assert mem[0x4000] == 0xCD

def test_w_read_after_b_write():
    """Тест чтения слова после записи байтов."""
    b_write(0x5000, 0x12)
    b_write(0x5001, 0x34)
    value = w_read(0x5000)
    assert value == 0x1234

def test_b_read_after_w_write():
    """Тест чтения байтов после записи слова."""
    w_write(0x6000, 0x5678)
    assert b_read(0x6000) == 0x56
    assert b_read(0x6001) == 0x78

def test_w_read_max_value():
    """Тест чтения максимального значения слова (0xFFFF)."""
    w_write(0x7000, 0xFFFF)
    value = w_read(0x7000)
    assert value == 0xFFFF

def test_b_write_max_value():
    """Тест записи максимального значения байта (0xFF)."""
    b_write(0x8000, 0xFF)
    assert mem[0x8000] == 0xFF

def test_w_read_zero_address():
    """Тест чтения слова по нулевому адресу."""
    w_write(0x0000, 0x1234)
    value = w_read(0x0000)
    assert value == 0x1234

def test_b_write_zero_address():
    """Тест записи байта по нулевому адресу."""
    b_write(0x0000, 0xAB)
    assert mem[0x0000] == 0xAB

def test_w_read_last_address():
    """Тест чтения слова по последнему допустимому адресу."""
    w_write(0xFFFE, 0x5678)
    value = w_read(0xFFFE)
    assert value == 0x5678

def test_b_write_last_address():
    """Тест записи байта по последнему допустимому адресу."""
    b_write(0xFFFF, 0xCD)
    assert mem[0xFFFF] == 0xCD