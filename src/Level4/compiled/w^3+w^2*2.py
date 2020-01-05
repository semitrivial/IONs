# w^3+w^2*2.py
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
X=\\\"\\\"
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