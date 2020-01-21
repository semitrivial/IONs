# w.py
# This version of the file is completely standalone.# You can actually run it in python, completely on its own,# and you can run its outputs, and their outputs, etc.PREAMBLE = """
def escape(s):
    return s.replace(\'\\\\\', \'\\\\\\\\\').replace(\'\"\', \'\\\\\"\').replace(\"\'\", \"\\\\\'\")
def output(x):
    print(\'PREAMBLE=\\\"\\\"\\\"\')
    print(escape(PREAMBLE).strip())
    print(\'\\\"\\\"\\\"\')
    print(\'exec(PREAMBLE)\')
    print(x)
    raw_input(\"---- (Press enter to continue) ----\")
"""
exec(PREAMBLE)

TEMPLATE = """
X0=\"\"
output(X0)
""".replace('=\""', '=\"""X1"""')

X1=""

while True:
    output(X1)
    X1 = TEMPLATE.replace("X1", escape(X1))