from util import *

def test_level_omega():
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
    assert looks_like_omegasquared(ord_file("w^2"))

    print("Testing w^3.py")
    assert looks_like_omegacubed(ord_file("w^3"))

    print("Testing w^4.py")
    assert looks_like_omega_to4(ord_file("w^4"))

    print("Testing w^w.py")
    assert looks_like_omega_to_omega(ord_file("w^w"))
