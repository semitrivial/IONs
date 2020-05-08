# w^3*2+w^2*2.py
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

TEMPLATE="""
X='''___'''

while True:
    output(X)
    X='output(\"""' + escape(X) + '\""")'
"""

X="""
TEMPLATE=\"\"\"
X=\'\'\'___\'\'\'

while True:
    output(X)
    X=\'output(\\\"\"\"\' + escape(X) + \'\\\"\"\")\'
\"\"\"

X=\"\"\"
TEMPLATE=\\\'\\\'\\\'
TEMPLATE=\\\"\\\"\\\"
X=\\\\\\\'\\\'\\\'___\\\\\\\'\\\'\\\'
while True:
    output(X)
    X=\\\'output(\\\\\\\\\\\\\\\"\\\"\\\"\\\' + escape(X) + \\\'\\\\\\\\\\\\\\\"\\\"\\\")\\\'
\\\"\\\"\\\"
X=\\\\\\\'\\\'\\\'***\\\\\\\'\\\'\\\'
while True:
    output(X)
    X = TEMPLATE.replace(\\\'___\\\', escape(X))
\\\'\\\'\\\'
X=\\\"\\\"\\\"
TEMPLATE=\\\\\\\'\\\\\\\'\\\\\\\'
TEMPLATE=\\\\\\\"\\\\\\\"\\\\\\\"
X=\\\\\\\\\\\\\\\'\\\\\\\'\\\\\\\'___\\\\\\\\\\\\\\\'\\\\\\\'\\\\\\\'
while True:
    output(X)
    X=\\\\\\\'output(\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\"\\\\\\\"\\\\\\\"\\\\\\\' + escape(X) + \\\\\\\'\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\"\\\\\\\"\\\\\\\")\\\\\\\'
\\\\\\\"\\\\\\\"\\\\\\\"
X=\\\\\\\\\\\\\\\'\\\\\\\'\\\\\\\'***\\\\\\\\\\\\\\\'\\\\\\\'\\\\\\\'
while True:
    output(X)
    X = TEMPLATE.replace(\\\\\\\'___\\\\\\\', escape(X))
\\\\\\\'\\\\\\\'\\\\\\\'
X=\\\\\\\"\\\\\\\"
while True:
    output(X)
    X = TEMPLATE.replace(\\\\\\\'***\\\\\\\', escape(X))
\\\"\\\"\\\"
while True:
    output(X)
    X = TEMPLATE.replace(\\\'***\\\', escape(X))
\"\"\"

while True:
    output(X)
    X = TEMPLATE.replace(\'___\', escape(X))
"""

while True:
    output(X)
    X = TEMPLATE.replace('___', escape(X))