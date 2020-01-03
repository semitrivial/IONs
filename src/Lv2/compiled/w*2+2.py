# w*2+2.py
output("""
output(\"\"\"
X=\\\"\\\"\\\"
X=\\\\\\\"\\\\\\\"

while True:
    output(X)
    X = \\\\\\\"output(\\\\\\\'\\\\\\\" + escape(X) + \\\\\\\"\\\\\\\')\\\\\\\"
\\\"\\\"\\\"

while True:
    output(X)
    X = \\\"output(\\\'\\\'\\\'\\\" + escape(X) + \\\"\\\'\\\'\\\')\\\"
\"\"\")
""")