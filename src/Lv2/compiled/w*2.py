# We could write programs like w+1.py, w+2.py, w+3.py all day, but we're
# more intelligent than that. The pattern is easy to figure out.
#
# Think about what the following code outputs. First, it will output a
# program which we used to notate ω. Then, it will output a program
# we used to notate ω+1. Then, a program we used to notate ω+2. Then,
# ω+3. And so on forever. So the following program is an ION (all its
# outputs are IONs), notating the ordinal after ω, ω+1, ω+2, ...,
# namely: ω+ω, i.e., ω*2.
X="""
X=\"\"

while True:
    output(X)
    X = \"output(\'\" + escape(X) + \"\')\"
"""

while True:
    output(X)
    X = "output('''" + escape(X) + "''')"