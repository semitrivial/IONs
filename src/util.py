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

test_level = -1
output_counter = -1
output_was_called = False
output_limit = -1
captured_output = None

def set_test_level(lv):
    global test_level
    test_level = lv

def try_exec(x):
    try:
        exec(x.txt)
    except StopIteration:
        pass
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
    filename = "Lv" + str(test_level) + "/" + filename
    with open(filename, "r") as fp:
        return fp.read()

def ord_file(filename):
    return Notation(get_file(filename + ".py"))

def count_outputs(x, upper_limit=4):
    global output_counter
    global output_limit

    output_limit = upper_limit
    output_counter = -1
    try_exec(x)

    return output_counter + 1

def get_sole_output(x):
    assert count_outputs(x, upper_limit=1) == 1
    return x[0]

def is_zero(x):
    return count_outputs(x, upper_limit=1) == 0

def resembles(x, y):
    if (x.txt == y.txt):
        return True

    if is_zero(x):
        return is_zero(y)
    if is_zero(y):
        return False

    if count_outputs(x, upper_limit=1) == 1:
        if count_outputs(y, upper_limit=1) != 1:
            return False
        else:
            return resembles(x[0], y[0])

    if count_outputs(y, upper_limit=1) == 1:
        return False

    return resembles(x[0],y[0]) and resembles(x[1],y[1]) and resembles(x[2],y[2])

def looks_like_omega(x):
    assert is_zero(x[0])
    assert is_zero(x[1]-1)
    assert is_zero(x[2]-2)
    assert is_zero(x[3]-3)
    assert is_zero(x[4]-4)
    return True

def add_omega(x):
    return Notation("""
X='''"""+escape(x.txt)+"""'''
while True:
    output(X)
    X = "output('''" + escape(X) + "''')"
""")

def add_omega_squared(x):
    return Notation("""
TEMPLATE=\"""
X='''{}'''

while True:
    output(X)
    X='output(\\\"""' + escape(X) + '\\\""")'
\"""

X='''"""+escape(x.txt)+"""'''

while True:
    output(X)
    X = TEMPLATE.format(escape(X))
""")