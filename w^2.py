LEFT="""
X=\"\"\"
"""

RIGHT="""
\"\"\"
while True:
    output(X)
    X = "\"" + escape(X) + "\""
"""

X=""

while True:
    X = LEFT + X + RIGHT
    output(X)
