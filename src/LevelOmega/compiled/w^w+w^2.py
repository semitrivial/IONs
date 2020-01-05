TEMPLATE = """
TEMPLATE = \"\"\"
X0=\\\"\\\"
output(X0)
\"\"\".replace(\'=\\\"\"\', \'=\\\"\"\"X1\"\"\"\')

X1=\"\"

while True:
    output(X1)
    X1 = TEMPLATE.replace(\"X1\", escape(X1))
""".replace('=\""', '=\"""X2"""')

X2="""
X=\"\"\"
X0=\\\"\\\"
output(X0)
\"\"\"

TEMPLATE=\"\"\"
TEMPLATE = \'\'\'XX\'\'\'.replace(\'=\\\\\"\"\', \'=\\\\\\\"\\\"\\\"Xi\\\"\\\"\\\"\')

Xi=\"\"

while True:
    output(Xi)
    Xi = TEMPLATE.replace(\\\"Xi\\\", escape(Xi))
\"\"\"

i = 0
while True:
    output(X)
    i += 1
    Xi = \"X\" + str(i)
    X = TEMPLATE.replace(\'XX\', escape(X)).replace(\'Xi\', Xi)
"""

while True:
    output(X2)
    X2 = TEMPLATE.replace("X2", escape(X2))