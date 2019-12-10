# _*_ coding: utf _*_

output_counter = -1
output_was_called = False
output_limit = -1
captured_output = None

def output(x):
    global output_counter
    global output_was_called
    global captured_output

    output_was_called = True
    output_counter += 1
    captured_output = x.strip()
    if output_counter == output_limit:
        raise StopIteration("Done")

def escape(s):
    return s.replace('\\', '\\\\').replace('"', '\\"')

def get_file(filename):
    with open(filename, "r") as fp:
        return fp.read().strip()

def get_nth_output(str, n):
    global output_counter
    global output_limit
    global output_was_called

    output_counter = -1
    output_limit = n
    output_was_called = False

    try:
        exec(str)
    except StopIteration:
        pass

    assert output_was_called
    assert output_counter == output_limit
    return captured_output

def count_outputs(str, upper_limit=99):
    global output_counter
    global output_limit

    output_limit = upper_limit
    output_counter = -1
    exec(str)

    if output_counter == upper_limit:
        raise ValueError("Count_outputs called on an apparently infinite sequence")

    return output_counter + 1

def get_sole_output(str):
    assert count_outputs(str) == 1
    return get_nth_output(str, 0)

def test_after_decrements(str, test_fnc, num_decrements):
    if num_decrements == 0:
        return test_fnc(str)
    else:
        return test_after_decrements(get_sole_output(str), test_fnc, num_decrements - 1)

def looks_like_zero(str):
    return count_outputs(str) == 0

print("Testing 0.py")
assert looks_like_zero(get_file("0.py"))

print("Testing 1.py, 2.py, 3.py")
assert test_after_decrements(get_file("1.py"), looks_like_zero, 1)
assert test_after_decrements(get_file("2.py"), looks_like_zero, 2)
assert test_after_decrements(get_file("3.py"), looks_like_zero, 3)

def looks_like_omega(str):
    i = 0
    while i < 5:
        x = get_nth_output(str, i)
        if not test_after_decrements(x, looks_like_zero, i):
            return False
        i += 1
    return True

print("Testing w.py")
assert looks_like_omega(get_file("w.py"))

print("Testing w+1.py, w+2.py, w+3.py")
assert test_after_decrements(get_file("w+1.py"), looks_like_omega, 1)
assert test_after_decrements(get_file("w+2.py"), looks_like_omega, 2)
assert test_after_decrements(get_file("w+3.py"), looks_like_omega, 3)

def looks_like_omega_times2(str):
    i = 0
    while i < 5:
        x = get_nth_output(str, i)
        if not test_after_decrements(x, looks_like_omega, i):
            return False
        i += 1
    return True

print("Testing w*2.py, w*2+1.py, w*2+2.py, w*2+3.py")
assert looks_like_omega_times2(get_file("w*2.py"))
assert test_after_decrements(get_file("w*2+1.py"), looks_like_omega_times2, 1)
assert test_after_decrements(get_file("w*2+2.py"), looks_like_omega_times2, 2)
assert test_after_decrements(get_file("w*2+3.py"), looks_like_omega_times2, 3)

def looks_like_omega_times3(str):
    i = 0
    while i < 5:
        x = get_nth_output(str, i)
        if not test_after_decrements(x, looks_like_omega_times2, i):
            return False
        i += 1
    return True


print("Testing w*3.py")
assert looks_like_omega_times3(get_file("w*3.py"))

def looks_like_omegasquared(str):
    assert looks_like_omega(get_nth_output(str, 0))
    assert looks_like_omega_times2(get_nth_output(str, 1))
    assert looks_like_omega_times3(get_nth_output(str, 2))
