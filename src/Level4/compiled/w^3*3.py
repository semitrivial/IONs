# w^3*3.py
TEMPLATE='''
TEMPLATE="""
X=\'''___\'''
while True:
    output(X)
    X='output(\\\"""' + escape(X) + '\\\""")'
"""
X=\'''***\'''
while True:
    output(X)
    X = TEMPLATE.replace('___', escape(X))
'''
X="""
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
X=\\\"\\\"
while True:
    output(X)
    X = TEMPLATE.replace(\\\'***\\\', escape(X))
\"\"\"
while True:
    output(X)
    X = TEMPLATE.replace(\'***\', escape(X))
"""
while True:
    output(X)
    X = TEMPLATE.replace('***', escape(X))