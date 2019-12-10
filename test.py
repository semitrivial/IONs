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

def get_nth_output(filename, n):
    global output_counter
    global output_limit
    global output_was_called

    output_counter = -1
    output_limit = n
    output_was_called = False

    try:
        exec(get_file(filename))
    except StopIteration:
        pass

    assert output_was_called
    assert output_counter == output_limit
    return captured_output

def count_outputs(filename):
    global output_counter
    global output_limit

    output_limit = -1
    output_counter = -1
    exec(get_file(filename))
    return output_counter + 1

def test_sole_output(filename, expected):
    assert count_outputs(filename) == 1
    assert get_nth_output(filename, 0) == expected

print("Testing 0.py")
assert count_outputs("0.py") == 0

print("Testing 1.py")
test_sole_output("1.py", get_file("0.py"))

print("Testing 2.py")
test_sole_output("2.py", get_file("1.py"))

print("Testing 3.py")
test_sole_output("3.py", get_file("2.py"))

print("Testing ω.py")
assert get_nth_output("ω.py", 0) == get_file("0.py")
assert get_nth_output("ω.py", 1) == get_file("1.py")
assert get_nth_output("ω.py", 2) == get_file("2.py")
assert get_nth_output("ω.py", 3) == get_file("3.py")

print("Testing ω+1.py")
test_sole_output("ω+1.py", get_file("ω.py"))

print("Testing ω+2.py")
test_sole_output("ω+2.py", get_file("ω+1.py"))

print("Testing ω+3.py")
test_sole_output("ω+3.py", get_file("ω+2.py"))

print("Testing ω*2.py")
assert get_nth_output("ω*2.py", 0) == get_file("ω.py")
assert get_nth_output("ω*2.py", 1) == get_file("ω+1.py")
assert get_nth_output("ω*2.py", 2) == get_file("ω+2.py")
assert get_nth_output("ω*2.py", 3) == get_file("ω+3.py")

print("Testing ω*2+1.py")
test_sole_output("ω*2+1.py", get_file("ω*2.py"))
