from util import *

def test_level_1():
    print("Testing test infrastructure")
    assert resembles(ord_file("w^2*3"), ord_file("w^2*3"))
    assert not resembles(ord_file("w^2*3"), ord_file("w^2*2"))

    print("Testing 0.py")
    assert is_zero(ord_file("0"))

    print("Testing 1.py, 2.py, 3.py")
    assert is_zero(ord_file("1")-1)
    assert is_zero(ord_file("2")-2)
    assert is_zero(ord_file("3")-3)

    def looks_like_omega(x):
        assert is_zero(x[0])
        assert is_zero(x[1]-1)
        assert is_zero(x[2]-2)
        assert is_zero(x[3]-3)
        assert is_zero(x[4]-4)
        return True

    print("Testing w.py")
    omega = ord_file("w")
    assert looks_like_omega(omega)