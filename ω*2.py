X="""
X=\"\"
while True:
    output(X)
    X = \"\\\"\" + escape(X) + \"\\\"\"
"""

while True:
    output(X)
    X = "\"" + escape(X) + "\""