# _*_ coding: utf _*_

class Notation:
    def __init__(self, txt):
        self.txt = txt
    def __getitem__(self, key):
        return get_nth_output(self, key)

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

def get_nth_output(x, n):
    global output_counter
    global output_limit
    global output_was_called

    output_counter = -1
    output_limit = n
    output_was_called = False

    try:
        try_exec(x)
    except StopIteration:
        pass

    assert output_was_called
    assert output_counter == output_limit
    return captured_output

def count_outputs(x, upper_limit=99):
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
    return get_nth_output(x, 0)

def test_after_decrements(x, test_fnc, num_decrements):
    if num_decrements == 0:
        return test_fnc(x)
    else:
        return test_after_decrements(get_sole_output(x), test_fnc, num_decrements - 1)

def looks_like_zero(x):
    return count_outputs(x) == 0

print("Testing 0.py")
assert looks_like_zero(ord_file("0.py"))

print("Testing 1.py, 2.py, 3.py")
assert test_after_decrements(ord_file("1.py"), looks_like_zero, 1)
assert test_after_decrements(ord_file("2.py"), looks_like_zero, 2)
assert test_after_decrements(ord_file("3.py"), looks_like_zero, 3)

def looks_like_omega(x):
    i = 0
    while i < 5:
        y = get_nth_output(x, i)
        if not test_after_decrements(y, looks_like_zero, i):
            return False
        i += 1
    return True

print("Testing w.py")
assert looks_like_omega(ord_file("w.py"))

print("Testing w+1.py, w+2.py, w+3.py")
assert test_after_decrements(ord_file("w+1.py"), looks_like_omega, 1)
assert test_after_decrements(ord_file("w+2.py"), looks_like_omega, 2)
assert test_after_decrements(ord_file("w+3.py"), looks_like_omega, 3)

def looks_like_omega_times2(x):
    i = 0
    while i < 5:
        y = get_nth_output(x, i)
        if not test_after_decrements(y, looks_like_omega, i):
            return False
        i += 1
    return True

print("Testing w*2.py, w*2+1.py")
assert looks_like_omega_times2(ord_file("w*2.py"))
assert test_after_decrements(ord_file("w*2+1.py"), looks_like_omega_times2, 1)

def looks_like_omega_times3(x):
    i = 0
    while i < 5:
        y = get_nth_output(x, i)
        if not test_after_decrements(y, looks_like_omega_times2, i):
            return False
        i += 1
    return True


print("Testing w*3.py")
assert looks_like_omega_times3(ord_file("w*3.py"))

def looks_like_omegasquared(x):
    assert looks_like_omega(get_nth_output(x, 0))
    assert looks_like_omega_times2(get_nth_output(x, 1))
    assert looks_like_omega_times3(get_nth_output(x, 2))
    return True

print("Testing w^2.py")
assert looks_like_omegasquared(ord_file("w^2.py"))

def looks_like_omegasquared_plus_omega(x):
    assert test_after_decrements(get_nth_output(x, 0), looks_like_omegasquared, 0)
    assert test_after_decrements(get_nth_output(x, 1), looks_like_omegasquared, 1)
    assert test_after_decrements(get_nth_output(x, 2), looks_like_omegasquared, 2)
    return True

print("Testing w^2+w.py")
assert looks_like_omegasquared_plus_omega(ord_file("w^2+w.py"))

print("Testing w^2+w*2.py")
assert looks_like_omegasquared_plus_omega(get_nth_output(ord_file("w^2+w*2.py"), 0))
assert test_after_decrements(get_nth_output(ord_file("w^2+w*2.py"), 1), looks_like_omegasquared_plus_omega, 1)
assert test_after_decrements(get_nth_output(ord_file("w^2+w*2.py"), 2), looks_like_omegasquared_plus_omega, 2)
assert test_after_decrements(get_nth_output(ord_file("w^2+w*2.py"), 3), looks_like_omegasquared_plus_omega, 3)
