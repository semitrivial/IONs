# w^2+w.py
X="""
TEMPLATE=\"\"\"
X=\'\'\'___\'\'\'

while True:
    output(X)
    X=\'output(\\\"\"\"\' + escape(X) + \'\\\"\"\")\'
\"\"\"

X=\"\"

while True:
    output(X)
    X = TEMPLATE.replace(\'___\', escape(X))
"""

while True:
    output(X)
    X = "output('''" + escape(X) + "''')"