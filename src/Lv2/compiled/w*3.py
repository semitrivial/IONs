X="""
X=\"\"\"
X=\\\"\\\"

while True:
    output(X)
    X = \\\"output(\\\'\\\" + escape(X) + \\\"\\\')\\\"
\"\"\"

while True:
    output(X)
    X = \"output(\'\'\'\" + escape(X) + \"\'\'\')\"
"""

while True:
    output(X)
    X = "output(\"\"\"\n" + escape(X) + "\n\"\"\")"