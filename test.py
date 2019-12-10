output_counter = 0
output_was_called = False
output_limit = -1
captured_output = None

def output(x):
    global output_counter
    global output_was_called
    global captured_output

    output_was_called = True
    output_counter += 1
    captured_output = x
    if output_counter == output_limit:
        raise StopIteration("Done")

def get_nth_output(filename, n):
    with open(filename, "r") as fp:
        code = fp.read()
        try:
            exec(code)
        except StopIteration:
            pass
        return captured_output

print(get_nth_output("2.py", 1))