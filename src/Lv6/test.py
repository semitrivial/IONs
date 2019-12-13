from util import *

def test_level_6():
    print("Testing w^w.py")
    assert looks_like_omega_to_omega(ord_file("w^w"))

    print("Testing w^w*2.py")
    def looks_like_wtow_times2(x):
        import pdb; pdb.set_trace()
        assert looks_like_omega_to_omega(x[0])
        assert resembles(x[1], add_omega(x[0]))
        return True
    assert looks_like_wtow_times2(ord_file("w^w*2"))