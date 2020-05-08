# w*2.py
# This version of the file is completely standalone.
# You can actually run it in python, completely on its own,
# and you can run its outputs, and their outputs, etc.
PREAMBLE = """
def escape(s):
    return s.replace(\'\\\\\', \'\\\\\\\\\').replace(\'\"\', \'\\\\\"\').replace(\"\'\", \"\\\\\'\")
def output(x):
    print(\'PREAMBLE=\\\"\\\"\\\"\')
    print(escape(PREAMBLE).strip())
    print(\'\\\"\\\"\\\"\')
    print(\'exec(PREAMBLE)\')
    print(x)
    try:
        input(\"---- (Press enter to continue) ----\")
    except Exception:
        pass
"""
exec(PREAMBLE)

X="""
X=\"\"

while True:
    output(X)
    X = \"output(\'\" + escape(X) + \"\')\"
"""

while True:
    output(X)
    X = "output('''" + escape(X) + "''')"