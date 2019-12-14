from util import *

def test_level_6():
    print("Testing w^w.py")
    assert looks_like_omega_to_omega(ord_file("w^w"))

    print("Testing w^w+1.py")
    assert looks_like_omega_to_omega(ord_file("w^w+1")-1)
