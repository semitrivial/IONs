# To obtain an ION that notates ω*2+1, we write a program which
# outputs nothing except a program that notates ω*2.
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