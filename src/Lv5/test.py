from util import *

def test_level_5():
    def looks_like_omega(x):
        assert is_zero(x[0])
        assert is_zero(x[1]-1)
        assert is_zero(x[2]-2)
        assert is_zero(x[3]-3)
        assert is_zero(x[4]-4)
        return True

    print("Testing w.py")
    assert looks_like_omega(ord_file("w"))

    print("Testing w^2.py")
    def looks_like_omegasquared(x):
        assert is_zero(x[0])
        assert looks_like_omega(x[1])
        assert resembles(x[2], add_omega(x[1]))
        assert resembles(x[3], add_omega(x[2]))
        return True
    assert looks_like_omegasquared(ord_file("w^2"))

    print("Testing w^3.py")
    def looks_like_omegacubed(x):
        assert is_zero(x[0])
        assert resembles(x[1], add_omega_squared(x[0]))
        assert resembles(x[2], add_omega_squared(x[1]))
        assert resembles(x[3], add_omega_squared(x[2]))
        return True
    assert looks_like_omegacubed(ord_file("w^3"))