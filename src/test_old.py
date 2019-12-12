from util import *

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

def add_omega(x):
    return Notation("""
X='''"""+escape(x.txt)+"""'''
while True:
    output(X)
    X = "output('''" + escape(X) + "''')"
""")

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