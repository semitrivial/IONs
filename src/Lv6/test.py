from util import *

def test_level_6():
    def looks_like_omega(x):
        assert is_zero(x[0])
        assert is_zero(x[1]-1)
        assert is_zero(x[2]-2)
        assert is_zero(x[3]-3)
        assert is_zero(x[4]-4)
        return True

    print("Testing w.py")
    assert looks_like_omega(ord_file("w"))

    print("Testing w^w.py")
    assert looks_like_omega_to_omega(ord_file("w^w"))

    print("Testing w^w+1.py")
    assert looks_like_omega_to_omega(ord_file("w^w+1")-1)

    print("Testing w^w+w.py")
    assert resembles(add_omega(ord_file("w^w")), ord_file("w^w+w"))

    print("Testing w^w+w^2.py")
    assert resembles(add_omega_squared(ord_file("w^w")), ord_file("w^w+w^2"))

    print("Testing w^w+w^3.py")
    assert resembles(add_omega_cubed(ord_file("w^w")), ord_file("w^w+w^3"))

    print("Testing w^w*2.py")
    def looks_like_omega_to_omega_times2(x):
        assert resembles(x[0], ord_file("w^w+w"))
        assert resembles(x[1], ord_file("w^w+w^2"))
        assert resembles(x[2], ord_file("w^w+w^3"))
        return True
    assert looks_like_omega_to_omega_times2(ord_file("w^w*2"))

    print("Testing w^w*2+1.py")
    assert looks_like_omega_to_omega_times2(ord_file("w^w*2+1")-1)

    print("Testing w^w*2+w.py")
    assert resembles(add_omega(ord_file("w^w*2")), ord_file("w^w*2+w"))

    print("Testing w^w*2+w^2.py")
    assert resembles(add_omega_squared(ord_file("w^w*2")), ord_file("w^w*2+w^2"))