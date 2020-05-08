# w^w.py
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
X0=\"\"
output(X0)
"""

TEMPLATE="""
TEMPLATE = '''XX'''.replace('=\\""', '=\\\"\"\"Xi\"\"\"')

Xi=""

while True:
    output(Xi)
    Xi = TEMPLATE.replace(\"Xi\", escape(Xi))
"""

i = 0
while True:
    output(X)
    i += 1
    Xi = "X" + str(i)
    X = TEMPLATE.replace('XX', escape(X)).replace('Xi', Xi)