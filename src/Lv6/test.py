from util import *

zero = Notation("")

def test_level_6():
    print("Testing X->X+1.py")
    assert is_zero(apply_file('X->X+1', 'fnc', zero)-1)
    assert looks_like_omega(apply_file('X->X+1', 'fnc', add_omega(zero))-1)

    print("Testing X->X+w.py")
    assert looks_like_omega(apply_file('X->X+w', 'fnc2', zero))
    x = apply_file('X->X+w', 'fnc2', zero)
    x1 = apply_file('X->X+w', 'fnc2', x)
    x2 = add_omega(x)
    assert resembles(x1, x2)
    x11 = apply_file('X->X+w', 'fnc2', x1)
    x12 = add_omega(x1)
    x21 = apply_file('X->X+w', 'fnc2', x2)
    x22 = add_omega(x2)
    assert resembles(x11,x12)
    assert resembles(x11,x22)
    assert resembles(x12,x12)
    assert resembles(x12,x22)
