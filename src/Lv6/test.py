from util import *

zero = Notation("")

def test_level_6():
    print("Testing X->X+1.py")
    assert is_zero(apply_file('X->X+1', zero)-1)
    assert looks_like_omega(apply_file('X->X+1', add_omega(zero))-1)
