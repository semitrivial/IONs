# _*_ coding: utf _*_

class Notation:
    def __init__(self, txt):
        self.txt = txt
    def __getitem__(self, key):
        global output_counter
        global output_limit
        global output_was_called

        output_counter = -1
        output_limit = key
        output_was_called = False

        try:
            try_exec(self)
        except StopIteration:
            pass

        assert output_was_called
        assert output_counter == output_limit
        return captured_output
    def __sub__(self, subtractand):
        if subtractand == 0:
            return self
        else:
            return get_sole_output(self) - (subtractand-1)

output_counter = -1
output_was_called = False
output_limit = -1
captured_output = None

def try_exec(x):
    try:
        exec(x.txt)
    except StopIteration:
        raise
    except Exception as e:
        print("---")
        print(x.txt)
        print("---")
        raise e

def output(x):
    global output_counter
    global output_was_called
    global captured_output

    output_was_called = True
    output_counter += 1
    captured_output = Notation(x)
    if output_counter == output_limit:
        raise StopIteration("Done")

def escape(s):
    return s.replace('\\', '\\\\').replace('"', '\\"').replace("'", "\\'")

def get_file(filename):
    with open(filename, "r") as fp:
        return fp.read()

def ord_file(filename):
    return Notation(get_file(filename))

def count_outputs(x, upper_limit=9):
    global output_counter
    global output_limit

    output_limit = upper_limit
    output_counter = -1
    try_exec(x)

    if output_counter == upper_limit:
        raise ValueError("Count_outputs called on an apparently infinite sequence")

    return output_counter + 1

def get_sole_output(x):
    assert count_outputs(x) == 1
    return x[0]

def is_zero(x):
    return count_outputs(x) == 0

print("Testing 0.py")
assert is_zero(ord_file("0.py"))

print("Testing 1.py, 2.py, 3.py")
assert is_zero(ord_file("1.py")-1)
assert is_zero(ord_file("2.py")-2)
assert is_zero(ord_file("3.py")-3)

def looks_like_omega(x):
    assert is_zero(x[0])
    assert is_zero(x[1]-1)
    assert is_zero(x[2]-2)
    assert is_zero(x[3]-3)
    assert is_zero(x[4]-4)
    return True

print("Testing w.py")
assert looks_like_omega(ord_file("w.py"))

print("Testing w+1.py, w+2.py, w+3.py")
assert looks_like_omega(ord_file("w+1.py")-1)
assert looks_like_omega(ord_file("w+2.py")-2)
assert looks_like_omega(ord_file("w+3.py")-3)

print("Testing w*2.py, w*2+1.py")
def looks_like_omega_times2(x):
    assert looks_like_omega(x[0])
    assert looks_like_omega(x[1]-1)
    assert looks_like_omega(x[2]-2)
    return True
assert looks_like_omega_times2(ord_file("w*2.py"))
assert looks_like_omega_times2(ord_file("w*2+1.py")-1)

print("Testing w*3.py")
def looks_like_omega_times3(x):
    assert looks_like_omega_times2(x[0])
    assert looks_like_omega_times2(x[1]-1)
    assert looks_like_omega_times2(x[2]-2)
    return True
assert looks_like_omega_times3(ord_file("w*3.py"))

print("Testing w^2.py")
def looks_like_omegasquared(x):
    assert is_zero(x[0])
    assert looks_like_omega(x[1])
    assert looks_like_omega_times2(x[2])
    assert looks_like_omega_times3(x[3])
    return True
assert looks_like_omegasquared(ord_file("w^2.py"))

print("Testing w^2+w.py")
def looks_like_omegasquared_plus_omega(x):
    assert looks_like_omegasquared(x[0])
    assert looks_like_omegasquared(x[1]-1)
    assert looks_like_omegasquared(x[2]-2)
    return True
assert looks_like_omegasquared_plus_omega(ord_file("w^2+w.py"))

print("Testing w^2+w*2.py")
def looks_like_omegasquared_plus_omegatimes2(x):
    assert looks_like_omegasquared_plus_omega(x[0])
    assert looks_like_omegasquared_plus_omega(x[1]-1)
    assert looks_like_omegasquared_plus_omega(x[2]-2)
    return True
assert looks_like_omegasquared_plus_omegatimes2(ord_file("w^2+w*2.py"))

print("Testing w^2*2.py")
def looks_like_omegasquared_times2(x):
    assert looks_like_omegasquared(x[0])
    assert looks_like_omegasquared_plus_omega(x[1])
    assert looks_like_omegasquared_plus_omegatimes2(x[2])
    return True
assert looks_like_omegasquared_times2(ord_file("w^2*2.py"))
