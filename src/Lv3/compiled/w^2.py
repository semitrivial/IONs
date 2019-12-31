# We review the program we used to notate ω^2.
# What if we took this program and used it as the
# initial value for X in w.py?
TEMPLATE="""
X='''___'''

while True:
    output(X)
    X='output(\"""' + escape(X) + '\""")'
"""

X=""

while True:
    output(X)
    X = TEMPLATE.replace('___', escape(X))