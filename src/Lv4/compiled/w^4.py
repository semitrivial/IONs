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