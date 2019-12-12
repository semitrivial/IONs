from util import *

def test_level_1():
    print("Testing 0.py")
    assert is_zero(ord_file("0"))

    print("Testing 1.py, 2.py, 3.py")
    assert is_zero(ord_file("1")-1)
    assert is_zero(ord_file("2")-2)
    assert is_zero(ord_file("3")-3)

    print("Testing w.py")
    assert looks_like_omega(ord_file("w"))