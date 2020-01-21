# w^3.py
PREAMBLE = """
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
TEMPLATE = \"\"\"
TEMPLATE = \\\"\\\"\\\"
X0=\\\\\\\"\\\\\\\"
output(X0)
\\\"\\\"\\\".replace(\\\'=\\\\\\\"\\\"\\\', \\\'=\\\\\\\"\\\"\\\"X1\\\"\\\"\\\"\\\')

X1=\\\"\\\"

while True:
    output(X1)
    X1 = TEMPLATE.replace(\\\"X1\\\", escape(X1))
\"\"\".replace(\'=\\\"\"\', \'=\\\"\"\"X2\"\"\"\')

X2=\"\"

while True:
    output(X2)
    X2 = TEMPLATE.replace(\"X2\", escape(X2))
""".replace('=\""', '=\"""X3"""')

X3=""

while True:
    output(X3)
    X3 = TEMPLATE.replace("X3", escape(X3))