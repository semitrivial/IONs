# w^2+w*2.py
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