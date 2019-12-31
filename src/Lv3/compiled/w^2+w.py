# The program below is the resulting of taking w.py and changing the
# initial value of X so that instead of starting as the empty string,
# X starts as the contents of w^2.py. Convince yourself that this
# program outputs ordinals notating ω^2, ω^2+1, ω^2+2, etc.,
# so this program itself notates ω^2+ω. NOTE: If you see "get_file",
# that's a utility function we use to compile an ION. The fully
# compiled ION is obtained by replacing the get_file with an escaped
# copy of the contents of w^2.py.
X="""
# We review the program we used to notate ω^2.
# What if we took this program and used it as the
# initial value for X in w.py?
TEMPLATE=\"\"\"
X=\'\'\'___\'\'\'

while True:
    output(X)
    X=\'output(\\\"\"\"\' + escape(X) + \'\\\"\"\")\'
\"\"\"

X=\"\"

while True:
    output(X)
    X = TEMPLATE.replace(\'___\', escape(X))
"""

while True:
    output(X)
    X = "output('''" + escape(X) + "''')"