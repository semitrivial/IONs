from util import *

zero = Notation("")

def test_level_6():
    print("Testing X->X+1.py")
    assert is_zero(apply_file('X->X+1', 'fnc', zero)-1)
    assert looks_like_omega(apply_file('X->X+1', 'fnc', add_omega(zero))-1)

    print("Testing X->X+w.py")
    assert looks_like_omega(apply_file('X->X+w', 'fnc2', zero))