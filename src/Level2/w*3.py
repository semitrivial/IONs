## w*3.py
# We could write programs like w*2.py, w*2+1.py, w*2+2.py all day, but
# we're more intelligent than that. The pattern is easy to figure out.
#
# What does the following code output? First, a program we used to
# notate ω*2. Then, a program we used to notate ω*2+1. Then, a program
# we used to notate ω*2+2. And so on forever. So the following program
# is an ION (all its outputs are IONs), notating the ordinal after
# ω*2, ω*2+1, ω*2+2, ..., namely: ω*2+ω, i.e., ω*3.
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