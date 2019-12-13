from util import *

def test_level_3():
    print("Testing w.py")
    assert looks_like_omega(ord_file("w"))

    def looks_like_omega_times2(x):
        assert looks_like_omega(x[0])
        assert looks_like_omega(x[1]-1)
        assert looks_like_omega(x[2]-2)
        return True

    def looks_like_omega_times3(x):
        assert looks_like_omega_times2(x[0])
        assert looks_like_omega_times2(x[1]-1)
        assert looks_like_omega_times2(x[2]-2)
        return True

    print("Testing w^2.py")
    assert looks_like_omegasquared(ord_file("w^2"))

    print("Testing w^2+w.py")
    def looks_like_omegasquared_plus_omega(x):
        assert looks_like_omegasquared(x[0])
        assert looks_like_omegasquared(x[1]-1)
        assert looks_like_omegasquared(x[2]-2)
        return True
    assert looks_like_omegasquared_plus_omega(ord_file("w^2+w"))

    print("Testing w^2+w*2.py")
    def looks_like_omegasquared_plus_omegatimes2(x):
        assert looks_like_omegasquared_plus_omega(x[0])
        assert looks_like_omegasquared_plus_omega(x[1]-1)
        assert looks_like_omegasquared_plus_omega(x[2]-2)
        return True
    assert looks_like_omegasquared_plus_omegatimes2(ord_file("w^2+w*2"))

    print("Testing w^2*2.py")
    def looks_like_omegasquared_times2(x):
        assert looks_like_omegasquared(x[0])
        assert looks_like_omegasquared_plus_omega(x[1])
        assert looks_like_omegasquared_plus_omegatimes2(x[2])
        return True
    assert looks_like_omegasquared_times2(ord_file("w^2*2"))

    print("Testing w^2*3.py")
    def looks_like_omegasquared_times3(x):
        assert resembles(x[0], ord_file("w^2*2"))
        assert resembles(x[1], add_omega(x[0]))
        assert resembles(x[2], add_omega(x[1]))
        return True
    assert looks_like_omegasquared_times3(ord_file("w^2*3"))

    print("Testing w^3.py")
    def looks_like_omegacubed(x):
        assert is_zero(x[0])
        assert resembles(x[1], ord_file("w^2"))
        assert resembles(x[2], ord_file("w^2*2"))
        assert resembles(x[3], ord_file("w^2*3"))
        return True
    assert looks_like_omegacubed(ord_file("w^3"))