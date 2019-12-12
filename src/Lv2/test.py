from util import *

def test_level_2():
    print("Testing w.py")
    assert looks_like_omega(ord_file("w"))

    print("Testing w+1.py, w+2.py, w+3.py")
    assert looks_like_omega(ord_file("w+1")-1)
    assert looks_like_omega(ord_file("w+2")-2)
    assert looks_like_omega(ord_file("w+3")-3)

    print("Testing w*2.py, w*2+1.py")
    def looks_like_omega_times2(x):
        assert looks_like_omega(x[0])
        assert looks_like_omega(x[1]-1)
        assert looks_like_omega(x[2]-2)
        return True
    assert looks_like_omega_times2(ord_file("w*2"))
    assert looks_like_omega_times2(ord_file("w*2+1")-1)

    print("Testing w*3.py")
    def looks_like_omega_times3(x):
        assert looks_like_omega_times2(x[0])
        assert looks_like_omega_times2(x[1]-1)
        assert looks_like_omega_times2(x[2]-2)
        return True
    assert looks_like_omega_times3(ord_file("w*3"))

    print("Testing w^2.py")
    def looks_like_omegasquared(x):
        assert is_zero(x[0])
        assert looks_like_omega(x[1])
        assert looks_like_omega_times2(x[2])
        assert looks_like_omega_times3(x[3])
        return True
    assert looks_like_omegasquared(ord_file("w^2"))