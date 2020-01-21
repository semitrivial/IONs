# w^4.py
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

TEMPLATE="""
TEMPLATE=\'\'\'
TEMPLATE=\"\"\"
X=\\\'\'\'___\\\'\'\'
while True:
    output(X)
    X=\'output(\\\\\\\"\"\"\' + escape(X) + \'\\\\\\\"\"\")\'
\"\"\"
X=\\\'\'\'***\\\'\'\'
while True:
    output(X)
    X = TEMPLATE.replace(\'___\', escape(X))
\'\'\'
X=\"\"
while True:
    output(X)
    X = TEMPLATE.replace(\'***\', escape(X))
"""
TEMPLATE=TEMPLATE.replace('X=""', "X='''!!!'''")
X=""
while True:
    output(X)
    X = TEMPLATE.replace("!!!", escape(X))