# w^2.py
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

X2=""

while True:
    output(X2)
    X2 = TEMPLATE.replace("X2", escape(X2))