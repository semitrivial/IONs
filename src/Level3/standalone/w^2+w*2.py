# w^2+w*2.py
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

X="""
X=\"\"\"
TEMPLATE=\\\"\\\"\\\"
X=\\\'\\\'\\\'___\\\'\\\'\\\'

while True:
    output(X)
    X=\\\'output(\\\\\\\"\\\"\\\"\\\' + escape(X) + \\\'\\\\\\\"\\\"\\\")\\\'
\\\"\\\"\\\"

X=\\\"\\\"

while True:
    output(X)
    X = TEMPLATE.replace(\\\'___\\\', escape(X))
\"\"\"

while True:
    output(X)
    X = \"output(\'\'\'\" + escape(X) + \"\'\'\')\"
"""

while True:
    output(X)
    X = "output('''" + escape(X) + "''')"