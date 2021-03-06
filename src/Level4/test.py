from util import *

def test_level_4():
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

    print("Testing w^3+w^2.py")
    def looks_like_omegacubed_plus_omegasquared(x):
        assert resembles(x[0], ord_file("w^3"))
        assert resembles(x[1], add_omega(x[0]))
        assert resembles(x[2], add_omega(x[1]))
        return True
    assert looks_like_omegacubed_plus_omegasquared(ord_file("w^3+w^2"))

    print("Testing w^3+w^2*2.py")
    def looks_like_omegacubed_plus_omegasquared_times2(x):
        assert resembles(x[0], ord_file("w^3+w^2"))
        assert resembles(x[1], add_omega(x[0]))
        assert resembles(x[2], add_omega(x[1]))
        return True
    assert looks_like_omegacubed_plus_omegasquared_times2(ord_file("w^3+w^2*2"))

    print("Testing w^3*2.py")
    def looks_like_omegacubed_times2(x):
        assert resembles(x[0], ord_file("w^3"))
        assert resembles(x[1], ord_file("w^3+w^2"))
        assert resembles(x[2], ord_file("w^3+w^2*2"))
        return True
    assert looks_like_omegacubed_times2(ord_file("w^3*2"))

    print("Testing w^3*2+w^2.py")
    def looks_like_omegacubed_times2_plus_omegasquared(x):
        assert looks_like_omegacubed_times2(x[0])
        assert resembles(x[1], add_omega(x[0]))
        assert resembles(x[2], add_omega(x[1]))
        return True
    assert looks_like_omegacubed_times2_plus_omegasquared(ord_file("w^3*2+w^2"))

    print("Testing w^3*2+w^2*2.py")
    def looks_like_omegacubed_times2_plus_omegasquared_times2(x):
        assert looks_like_omegacubed_times2_plus_omegasquared(x[0])
        assert resembles(x[1], add_omega(x[0]))
        assert resembles(x[2], add_omega(x[1]))
        return True
    assert looks_like_omegacubed_times2_plus_omegasquared_times2(ord_file("w^3*2+w^2*2"))

    print("Testing w^3*3.py")
    assert("Testing w^3*3.py")
    def looks_like_omegacubed_times3(x):
        assert looks_like_omegacubed_times2(x[0])
        assert looks_like_omegacubed_times2_plus_omegasquared(x[1])
        assert looks_like_omegacubed_times2_plus_omegasquared_times2(x[2])
        return True
    assert looks_like_omegacubed_times3(ord_file("w^3*3"))

    print("Testing w^4.py")
    assert looks_like_omega_to4(ord_file("w^4"))