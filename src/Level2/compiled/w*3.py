# w*3.py
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
    X = "output(\"\"\"" + escape(X) + "\"\"\")"