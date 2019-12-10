output("""
output(\"\"\"
X=\"\"
while True:
    output(X)
    X = \"\\\"\" + escape(X) + \"\\\"\"
\"\"\")
""")