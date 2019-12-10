output("""
X=\"\"\"
X=\\\"\\\"\\\"
\\\"\\\"\\\".strip()

while True:
    output(X)
    X = \\\"output(\\\\\\\"\\\" + escape(X) + \\\"\\\\\\\")\\\"
\"\"\".strip()

while True:
    output(X)
    X = \"output(\\\"\\\"\\\"\\n\" + escape(X) + \"\\n\\\"\\\"\\\")\"
""")