# The pattern continues. To go from ω+1 to ω+2, we write
# a program which simply outputs the program which we
# used to notate ω+1.
output("""
output(\"\"\"
X=\\\"\\\"

while True:
    output(X)
    X = \\\"output(\\\'\\\" + escape(X) + \\\"\\\')\\\"
\"\"\")
""")