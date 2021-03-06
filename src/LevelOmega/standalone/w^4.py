# w^4.py
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

TEMPLATE = """
TEMPLATE = \"\"\"
TEMPLATE = \\\"\\\"\\\"
TEMPLATE = \\\\\\\"\\\\\\\"\\\\\\\"
X0=\\\\\\\\\\\\\\\"\\\\\\\\\\\\\\\"
output(X0)
\\\\\\\"\\\\\\\"\\\\\\\".replace(\\\\\\\'=\\\\\\\\\\\\\\\"\\\\\\\"\\\\\\\', \\\\\\\'=\\\\\\\\\\\\\\\"\\\\\\\"\\\\\\\"X1\\\\\\\"\\\\\\\"\\\\\\\"\\\\\\\')

X1=\\\\\\\"\\\\\\\"

while True:
    output(X1)
    X1 = TEMPLATE.replace(\\\\\\\"X1\\\\\\\", escape(X1))
\\\"\\\"\\\".replace(\\\'=\\\\\\\"\\\"\\\', \\\'=\\\\\\\"\\\"\\\"X2\\\"\\\"\\\"\\\')

X2=\\\"\\\"

while True:
    output(X2)
    X2 = TEMPLATE.replace(\\\"X2\\\", escape(X2))
\"\"\".replace(\'=\\\"\"\', \'=\\\"\"\"X3\"\"\"\')

X3=\"\"

while True:
    output(X3)
    X3 = TEMPLATE.replace(\"X3\", escape(X3))
""".replace('=\""', '=\"""X4"""')

X4=""

while True:
    output(X4)
    X4 = TEMPLATE.replace("X4", escape(X4))