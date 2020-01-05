# w*2+1.py
output("""
X=\"\"\"
X=\\\"\\\"

while True:
    output(X)
    X = \\\"output(\\\'\\\" + escape(X) + \\\"\\\')\\\"
\"\"\"

while True:
    output(X)
    X = \"output(\'\'\'\" + escape(X) + \"\'\'\')\"
""")