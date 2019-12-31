# In w^2*2.py, we changed the initial value of X in w^2.py to be
# the contents of w^2.py. What if instead, we change the initial
# value of X in w^2.py to be the contents of w^2*2.py?
# Exercise: convince yourself the below program outputs notations
# for for (ω^2)*2, (ω^2)*2+ω, (ω^2)*2+ω*2, (ω^2)*2+ω*3, ...
# Therefore, it notates (ω^2)*2+ω^2, i.e., (ω^2)*3.
# NOTE: If you see "get_file", that's a utility function for
# compiling an ION. The compiled ION is obtained by replacing the
# "get_file" with an escaped copy of w^2.py.
TEMPLATE="""
X='''___'''

while True:
    output(X)
    X='output(\"""' + escape(X) + '\""")'
"""

X="""
# In w^2+w.py and w^2+w*2.py, we changed the initial value of X
# in w.py. What if we change the initial value of X in w^2.py?
# Exercise: convince yourself the below program outputs notations
# for for ω^2, ω^2+ω, ω^2+ω*2, ω^2+ω*3, ...
# Therefore, it notates ω^2+ω^2, i.e., (ω^2)*2.
#
# NOTE: If you see \"get_file\", that\'s a utility function for
# compiling an ION. The compiled ION is obtained by replacing the
# \"get_file\" with an escaped copy of w^2.py.
TEMPLATE=\"\"\"
X=\'\'\'___\'\'\'

while True:
    output(X)
    X=\'output(\\\"\"\"\' + escape(X) + \'\\\"\"\")\'
\"\"\"

X=\"\"\"
# We review the program we used to notate ω^2.
# What if we took this program and used it as the
# initial value for X in w.py?
TEMPLATE=\\\"\\\"\\\"
X=\\\'\\\'\\\'___\\\'\\\'\\\'

while True:
    output(X)
    X=\\\'output(\\\\\\\"\\\"\\\"\\\' + escape(X) + \\\'\\\\\\\"\\\"\\\")\\\'
\\\"\\\"\\\"

X=\\\"\\\"

while True:
    output(X)
    X = TEMPLATE.replace(\\\'___\\\', escape(X))
\"\"\"

while True:
    output(X)
    X = TEMPLATE.replace(\'___\', escape(X))
"""

while True:
    output(X)
    X = TEMPLATE.replace('___', escape(X))