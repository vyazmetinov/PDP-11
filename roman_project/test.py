import pytest
from bwr_brr import*
def test_b_write_and_read():
  
    b_write(0x1000, 0xAB)
    
    assert b_read(0x1000) == 0xAB


    with pytest.raises(ValueError):
        b_write(MEMSIZE, 0x12)
    with pytest.raises(ValueError):
        b_read(MEMSIZE)

def test_w_write_and_read():
 
    
    w_write(0x2000, 0xABCD)
    assert w_read(0x2000) == 0xABCD


    with pytest.raises(ValueError):
        w_write(0x2001, 0x1234)
    with pytest.raises(ValueError):
        w_read(0x2001)

   
    with pytest.raises(ValueError):
        w_write(MEMSIZE - 1, 0x1234)
    with pytest.raises(ValueError):
        w_read(MEMSIZE - 1)

def test_boundary_conditions():
  
    b_write(0, 0xFF)
    assert b_read(0) == 0xFF

    b_write(MEMSIZE - 1, 0xAA)
    assert b_read(MEMSIZE - 1) == 0xAA

    w_write(0, 0xFFFF)
    assert w_read(0) == 0xFFFF

    w_write(MEMSIZE - 2, 0x1234)
    assert w_read(MEMSIZE - 2) == 0x1234

if __name__ == "__main__":
    pytest.main()
